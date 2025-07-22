from typing import Optional
import aiosqlite
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from httpx_socks import AsyncProxyTransport
from src.logger import get_logger, get_message
import httpx
from httpx import ProxyError
import aiofiles
from tqdm.asyncio import tqdm

logger = get_logger()
DB_PATH = os.path.join("data", "SkinsRadar.db")
table_name = "proxies"

async def proxies_table_exits() -> bool:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            result = await cursor.fetchone()
            return result is not None
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "proxies_table_exits_db_error", str(e)))
        return False

async def init_proxies_db() -> None:
    try:
        if await proxies_table_exits():
            return
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("""
                        CREATE TABLE IF NOT EXISTS proxies (
                            proxy PRIMARY KEY,
                            added_at TEXT
                        )
                    """)
            await conn.commit()
            logger.info(get_message("proxies_manager", "init_proxies_db_success", DB_PATH))
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "init_proxies_db_error", str(e)))

async def add_proxies_db(proxies: list[str]) -> None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            total_inserted = 0
            current_time = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M:%S")
            for proxy in proxies:
                await cursor.execute(
                    "INSERT OR IGNORE INTO proxies (proxy, added_at) VALUES (?, ?)",
                    (proxy, current_time)
                )
                total_inserted += cursor.rowcount
            await conn.commit()
            logger.info(get_message("proxies_manager", "add_proxies_db_success", total_inserted))
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "add_proxies_db_error", str(e)))

async def wipe_all_proxies() -> None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("DELETE FROM proxies")
            await conn.commit()
            logger.info(get_message("proxies_manager", "wipe_all_proxies_success"))
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "wipe_all_proxies_error", str(e)))

async def update_proxies(working_proxies: list[str]) -> None:
    await init_proxies_db()
    if not working_proxies:
        logger.warning(get_message("proxies_manager", "update_proxies_no_new_proxies"))
    else:
        await add_proxies_db(working_proxies)

async def is_proxies_db_empty() -> bool:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute(f"SELECT COUNT(*) FROM proxies")
            result = await cursor.fetchone()
            count = result[0] if result else None
            return count == 0
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "is_proxies_db_empty_error", str(e)))
        return False

async def get_random_proxy() -> Optional[str]:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT proxy FROM proxies ORDER BY RANDOM() LIMIT 1")
            result = await cursor.fetchone()
            if result:
                logger.info(get_message("proxies_manager", "get_random_proxy_selected", result[0]))
                return result[0]
            else:
                logger.warning(get_message("proxies_manager", "get_random_proxy_not_found"))
                return None
    except aiosqlite.Error as e:
        logger.error(get_message("proxies_manager", "get_random_proxy_db_error", str(e)))
        return None

async def check_proxy(proxy: str, timeout: int = 5) -> bool:
    try:
        if proxy.startswith(("http://", "https://")):
            return False
        transport = AsyncProxyTransport.from_url(proxy, verify=False)
        async with httpx.AsyncClient(transport=transport, timeout=timeout, verify=False) as client:
            response = await client.get("https://api.ipify.org")
            return response.status_code == 200
    except (ProxyError, TimeoutError):
        return False

async def extract_proxies(file_path: str) -> list[str]:
    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as stream:
            all_proxies = []
            async for line in stream:
                all_proxies.append(line.strip())

            working_proxies = []
            tasks = [check_proxy(proxy) for proxy in all_proxies]
            results = await tqdm.gather(*tasks, desc=get_message("proxies_manager", "extract_proxies_checking", file_path), unit="proxy")
            for proxy, is_working in zip(all_proxies, results):
                if is_working:
                    working_proxies.append(proxy)
                else:
                    logger.debug(get_message("proxies_manager", "extract_proxies_proxy_failed", proxy))

            logger.info(get_message("proxies_manager", "extract_proxies_summary", len(all_proxies), len(working_proxies)))
            return working_proxies
    except FileNotFoundError:
        logger.error(get_message("proxies_manager", "extract_proxies_file_not_found", file_path))
        return []
    except Exception as e:
        logger.error(get_message("proxies_manager", "extract_proxies_general_error", file_path, str(e)))
        return []

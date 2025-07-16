from typing import Optional
import aiosqlite
import os
import asyncio
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from src.logger import logger

DB_PATH = os.path.join("data", "SkinsRadar.db")
table_name = "proxies"
DELETE_PROXY_INTERVAL = 120 # In minutes
UPDATE_PROXY_INTERVAL = 120 # In Seconds
UPDATE_PROXY_CYCLE = 5 # In seconds

async def proxies_table_exits() -> bool:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            result = await cursor.fetchone()
            return result is not None
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД прокси: {e}")
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
            logger.info(f"БД инициализирована: {DB_PATH}")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка инициализации БД прокси: {e}")

async def add_proxies_db(proxies: list) -> None:
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
            logger.info(f"Добавлено {total_inserted} новых прокси")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка обновлении БД прокси: {e}")

async def delete_old_proxies() -> None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            proxy_age = (datetime.now(ZoneInfo("UTC")) - timedelta(minutes=DELETE_PROXY_INTERVAL)).strftime("%Y-%m-%d %H:%M:%S")
            await cursor.execute("DELETE FROM proxies WHERE added_at < ?", (proxy_age,))
            await conn.commit()
            logger.info(f"Удалено {cursor.rowcount} прокси старше {DELETE_PROXY_INTERVAL} минут")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка удаления старых прокси из БД: {e}")

async def update_proxies() -> None:
    logger.info("Запуск обновления прокси")
    await init_proxies_db()
    proxies = await find_proxies()
    if not proxies:
        logger.warning("Не найдено новых прокси 🥺")
        return
    await add_proxies_db(proxies)
    await delete_old_proxies()
    logger.info("Прокси обновлены")

async def is_proxies_db_empty() -> bool:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute(f"SELECT COUNT(*) FROM proxies")
            result = await cursor.fetchone()
            count = result[0] if result else None
            return count == 0
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД прокси: {e}")
        return False

async def get_random_proxy() -> Optional[str]:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT proxy FROM proxies ORDER BY RANDOM() LIMIT 1")
            result = await cursor.fetchone()
            if result:
                logger.info(f"Выбран случайный прокси: {result[0]}")
                return result[0]
            else:
                logger.warning("Рабочие прокси не найдены в БД")
                return None
    except aiosqlite.Error as e:
        logger.error(f"Ошибка получения прокси из БД: {e}")
        return None

async def run_periodic_update(stop_event: asyncio.Event = None) -> None:
    await init_proxies_db()
    logger.info("Запущено периодическое обновление прокси")
    last_run = asyncio.get_event_loop().time()

    while not(stop_event and stop_event.is_set()):
        current_time = asyncio.get_event_loop().time()
        if current_time - last_run >= UPDATE_PROXY_INTERVAL:
            await update_proxies()
            last_run = current_time
        await asyncio.sleep(UPDATE_PROXY_CYCLE)

async def find_proxies() -> list[str]:
    # TODO
    return None
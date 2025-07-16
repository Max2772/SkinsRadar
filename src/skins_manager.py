import re
import httpx
import aiosqlite
import os

from src.utils import is_skin_supported
from src.logger import logger

DB_PATH = os.path.join("data", "SkinsRadar.db")

def fetch_and_process_skins():
    url = "https://raw.githubusercontent.com/somespecialone/steam-item-name-ids/master/data/cs2.json"

    try:
        response = httpx.get(url)
        response.raise_for_status()
        skins_data = response.json()
        return skins_data

    except httpx.RequestError as e:
        logger.error(f"Ошибка загрузки данных: {e}")
        return []
    except KeyError as e:
        logger.error(f"Ошибка в структуре JSON: отсутствует ключ {e}")
        return []
    except Exception as e:
        logger.error(f"Прочая ошибка: {e}")
        return []

async def create_and_populate_db(skins_data) -> None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("DROP TABLE IF EXISTS items")

            await cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    name TEXT PRIMARY KEY ,
                    item_nameid TEXT,
                    has_exterior INT DEFAULT 0
                )
            ''')

            pattern = re.compile(r'\((Factory New|Minimal Wear|Field-Tested|Well-Worn|Battle-Scarred)\)')

            size = 0
            for name, item_nameid in skins_data.items():
                has_exterior = 1 if pattern.search(name) else 0
                await cursor.execute('INSERT INTO items (name, item_nameid, has_exterior) VALUES (?, ?, ?)', (name, str(item_nameid), has_exterior))
                size += 1

            await conn.commit()
            logger.info(f"Успешно сохранено {size} скинов в БД")

    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД скинов: {e}")
    except KeyError as e:
        logger.error(f"Ошибка в JSON: отсутствует ключ {e}")
    except Exception as e:
        logger.error(f"Прочая ошибка: {e}")

async def get_item_nameid(full_skin_name: str):
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()

            query = "SELECT item_nameid FROM items WHERE name = ?"
            await cursor.execute(query, (full_skin_name,))

            result = await cursor.fetchone()
            if not result:
                logger.error("Скин не найден в БД")
                return None
            return result[0]
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД скинов: {e}")
        return None

async def get_full_skin_name_nameid(item_nameid: str):
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()

            query = "SELECT name FROM items WHERE item_nameid = ?"
            await cursor.execute(query, (item_nameid,))

            result = await cursor.fetchone()
            if not result:
                logger.error("Скин не найден в БД")
                return None
            return result[0]
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД скинов: {e}")
        return None

async def reset_search_state():
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("DROP TABLE IF EXISTS search_state")
            await cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_state (
                last_rowid INTEGER
            )
            """)
            await cursor.execute("INSERT OR REPLACE INTO search_state (last_rowid) VALUES (1)")
            await conn.commit()
            logger.info("Состояние поиска сброшено: таблица пересоздана с last_rowid = 1")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка при сбросе состояния поиска: {e}")

async def get_item_autosearch(souvenir: bool, stattrak: bool, knife: bool):
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT last_rowid FROM search_state")
            result = await cursor.fetchone()
            last_rowid = result[0] if result else 0

            await cursor.execute("""
                SELECT rowid, name, item_nameid 
                FROM items 
                WHERE rowid = ? 
            """, (last_rowid,))
            result = await cursor.fetchone()

            if result:
                current_rowid, name, item_nameid = result
                next_rowid = current_rowid + 1
                await cursor.execute("UPDATE search_state SET last_rowid = ?", (next_rowid,))
                await conn.commit()

                current_skin_souvenir, current_skin_stattrak, current_skin_knife = is_skin_supported(name)
                if current_skin_souvenir and not souvenir:
                    logger.info(f"Предмет {name} пропущен, т.к. является Souvenir")
                    return None, item_nameid

                if current_skin_stattrak and not stattrak:
                    logger.info(f"Предмет {name} пропущен, т.к. является StatTrak™")
                    return None, item_nameid

                if current_skin_knife and not knife:
                    logger.info(f"Предмет {name} пропущен, т.к. является Knife")
                    return None, item_nameid

                logger.info(f"Выбран item: name={name}, item_nameid={item_nameid}")
                return name, item_nameid
            else:
                logger.info(f"Строка с rowid={last_rowid} не найдена, сбрасываем на начало")
                await reset_search_state()
                await conn.commit()

                return None,None
    except aiosqlite.Error as e:
        logger.error(f"Ошибка получения скина из БД скинов: {e}")
        return None,None

async def get_max_rows() -> int | None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT MAX(rowid) FROM items")
            max_rows = await cursor.fetchone()
            if max_rows is None:
                logger.warning("Таблица скинов пуста")
                return None
            return max_rows[0]
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД скинов: {e}")
        return None

async def reset_max_rows():
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("UPDATE search_state SET last_rowid = ?", (1,))
            await conn.commit()
            logger.debug(f"last_rowid присвоено 1")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД с индексом последнего скина: {e}")
        return

async def get_current_row() -> int | None:
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT last_rowid FROM search_state")
            current_row = await cursor.fetchone()
            if current_row is None:
                logger.warning("Таблица с индексом последнего скина пуста")
                return None
            return current_row[0]
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД с индексом последнего скина: {e}")
        return None

async def decrement_current_row():
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute("SELECT last_rowid FROM search_state")
            result = await cursor.fetchone()
            current_row = result[0]
            if current_row <= 1:
                logger.warning("last_rowid уже минимален (1), декремент невозможен")
            new_rowid = current_row - 1
            await cursor.execute("UPDATE search_state SET last_rowid = ?", (new_rowid,))
            await conn.commit()
            logger.debug(f"last_rowid уменьшен с {current_row} до {new_rowid}")
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД с индексом последнего скина: {e}")

async def get_item_results(query: str):
    try:
        async with aiosqlite.connect(DB_PATH) as conn:
            cursor = await conn.cursor()
            await cursor.execute('''
                    SELECT name FROM items
                    WHERE name LIKE ?
                ''', (f'%{query}%',))
            results = await cursor.fetchall()
            return results
    except aiosqlite.Error as e:
        logger.error(f"Ошибка БД скинов: {e}")
        return None

async def update_skins():
    skins = fetch_and_process_skins()
    await create_and_populate_db(skins)
    await reset_search_state()

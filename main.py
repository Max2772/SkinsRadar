import asyncio
import httpx
from httpx_socks import AsyncProxyTransport
from python_socks import ProxyError, ProxyTimeoutError
import flet as ft
import urllib.parse
from typing import Dict, Any
from itertools import islice
import argparse

from src.ui import DEFAULT_SKIN, DEFAULT_AMOUNT_QUERY, DEFAULT_CURRENCY, DEFAULT_STEAM_FEE, DEFAULT_AMOUNT_PROFIT, DEFAULT_AMOUNT_SALES, DEFAULT_BOOST
from src.ui import main as ui_main

from src import (
    get_currency_symbol,
    clean_price, extract_stickers_info, extract_keychain_info, extract_history_prices, is_skin_boosted,
    get_random_proxy, is_proxies_db_empty,
    get_item_nameid, get_item_autosearch, get_full_skin_name_nameid,
    logger, get_message
)
from src.utils import split_item_name, get_total_sales

current_client = None
REQUEST_LIMITS = [10, 20, 100]

def get_nearest_request_limit(user_input: int) -> int:
    for limit in REQUEST_LIMITS:
        if limit >= user_input:
            return limit
    return REQUEST_LIMITS[-1]

async def create_client_with_proxy(proxy: str) -> httpx.AsyncClient:
        global current_client
        if current_client is not None:
            await current_client.aclose()
            current_client = None
        if not proxy:
            current_client = httpx.AsyncClient(timeout=10, verify=False)
            return current_client
        if proxy.startswith(("socks4://", "socks5://")):
            transport = AsyncProxyTransport.from_url(proxy, verify=False)
            current_client = httpx.AsyncClient(transport=transport, timeout=10, verify=False)
            return current_client
        else:
            raise ValueError(f"Неподдерживаемый формат прокси: {proxy}")

async def get_autobuy_data(client: httpx.AsyncClient, item_nameid: str, currency: int) -> str | None:
    url = f"https://steamcommunity.com/market/itemordershistogram?norender=1&country=NL&language=english&currency={currency}&item_nameid={item_nameid}&two_factor=0"
    try:
        response = await client.get(url)
        logger.info(get_message("main","get_autobuy_data_try_request", url))
        if response.status_code == 200:
            logger.info(get_message("main", "get_autobuy_data_success_response", url))
            return response.json()
        else:
            logger.warning(get_message("main","get_autobuy_data_http_error", response.status_code, url))
            global current_client
            current_client = None
            return None
    except httpx.HTTPStatusError as e:
        logger.warning(get_message("main", "get_autobuy_data_http_status_error", e))
        return None
    except httpx.RequestError as e:
        logger.warning(get_message("main", "get_autobuy_data_request_error", e))
        return None
    except (ProxyError, ProxyTimeoutError) as e:
        logger.warning(get_message("main", "get_autobuy_data_proxy_error", e))
        current_client = None
        return None

async def get_history_data(client: httpx.AsyncClient, full_skin_name: str, skip_boosted: bool, max_boost: float) -> str | int | None:
    url = f"https://steamcommunity.com/market/listings/730/{full_skin_name}"
    try:
        response = await client.get(url)
        logger.info(get_message("main","get_history_data_try_request", url))
        if response.status_code == 200:
            logger.info(get_message("main", "get_history_data_success_response", url))
            history_data = extract_history_prices(response.text)
            if skip_boosted and is_skin_boosted(history_data, max_boost):
                logger.info(get_message("main", "get_history_data_skip_boosted"))
                return -2
            return history_data
        else:
            logger.warning(get_message("main","get_history_data_http_error", response.status_code, url))
            global current_client
            current_client = None
            return None
    except httpx.HTTPStatusError as e:
        logger.warning(get_message("main", "get_history_data_http_status_error", e))
        return None
    except httpx.RequestError as e:
        logger.warning(get_message("main", "get_history_data_request_error", e))
        return None
    except (ProxyError, ProxyTimeoutError) as e:
        logger.warning(get_message("main", "get_history_data_proxy_error", e))
        current_client = None
        return None

async def fetch_market_data(client: httpx.AsyncClient, url_market: str, full_skin_name: str, currency: int, has_exterior: bool) -> Dict[str, Any]:
    try:
        global current_client
        logger.info(get_message("main", "fetch_market_data_try_request", url_market))
        response = await client.get(url_market)
        if response.status_code == 200:
            logger.info(get_message("main", "fetch_market_data_success_response", url_market))
            result = {"market_data": response.json()}
        elif response.status_code == 404:
            logger.warning(get_message("main", "fetch_market_item_not_found", full_skin_name))
            return {"market_data": None}
        else:
            logger.warning(get_message("main", "fetch_market_http_error", response.status_code, full_skin_name))
            current_client = None
            return {"market_data": None}

        item_nameid = await get_item_nameid(full_skin_name)
        result["item_nameid"] = item_nameid

        if item_nameid:
            result["autobuy_data"] = await get_autobuy_data(client, item_nameid, currency)
        else:
            result["autobuy_data"] = None

        result["has_exterior"] = True if has_exterior else False

        return result
    except (httpx.RequestError, httpx.ProxyError) as e:
        logger.warning(get_message("main", "fetch_market_request_error", full_skin_name, e))
        current_client = None
        return {"market_data": None, "item_nameid": None, "autobuy_data": None, "has_exterior": None}

async def fetch_market_json(currency: int, quality: str, amount: int, skin_name: str, souvenir: bool, stattrak: bool, knife: bool, skip_boosted: bool, max_boost: float, mode="DEFAULT"):
    global current_client

    if current_client is None or current_client.is_closed:
        proxy = await get_random_proxy() if not await is_proxies_db_empty() else None
        current_client = await create_client_with_proxy(proxy)  # Создаём новый клиент

    if mode == "RANDOM":
        name, item_nameid = await get_item_autosearch(souvenir, stattrak, knife)
        if name is None or item_nameid is None:
            return {
                "market_data": -1,
                "item_nameid": item_nameid
            }

        histogram_data = await get_autobuy_data(current_client, item_nameid, 1)
        if not histogram_data:
            return {
                "market_data": None,
                "history_data": None,
                "item_nameid": item_nameid
            }

        history_data = await get_history_data(current_client, name, skip_boosted, max_boost)
        if history_data == -2:
            return {
                "market_data": -2,
                "history_data": None,
                "item_nameid": item_nameid
            }
        if not history_data:
            return {
                "market_data": None,
                "history_data": None,
                "item_nameid": item_nameid
            }

        return {
            "market_data": histogram_data,
            "history_data": history_data,
            "item_nameid": item_nameid
        }

    else:
        encoded_skin = urllib.parse.quote(skin_name)
        base_url = f"https://steamcommunity.com/market/listings/730/{encoded_skin}"
        params= f"render?start=0&count={get_nearest_request_limit(amount)}&currency={currency}&format=json"
        parse_url = f"{base_url}%20({quality})/{params}" if quality else f"{base_url}/{params}"
        full_skin_name = f"{skin_name} ({quality})" if quality else f"{skin_name}"
        has_exterior = True if quality else False

        result = await fetch_market_data(current_client, parse_url, full_skin_name, currency, has_exterior)
        if not (result["market_data"] and result["item_nameid"] and result["autobuy_data"]):
            return None
        return result

async def process_autobuy_json_to_data(data) -> float:
    global current_client
    if not data:
        current_client = None
        logger.warning(get_message("main", "process_autobuy_json_to_data_json_unsuccessful"))
        return 0.0
    try:
        return clean_price(data.get("buy_order_price", "0"))
    except (KeyError, TypeError, AttributeError) as e:
        logger.warning(get_message("main", "process_autobuy_json_to_data_key_error", e))
        return 0.0

async def process_autosearch_json_to_data(json_data, fee: float, needed_profit: float, needed_sales: int):
    if not json_data.get("market_data") or not json_data.get("history_data"):
        global current_client
        current_client =  None
        logger.warning(get_message("main", "process_autosearch_json_to_data_json_unsuccessful"))
        return []
    try:
        market_data = json_data["market_data"]
        history_data = json_data["history_data"]

        autobuy_price = clean_price(market_data.get("buy_order_price"))
        selling_price = clean_price(market_data.get("sell_order_price"))
        if autobuy_price is None:
            logger.info(get_message("main", "process_autosearch_json_to_data_no_buyers"))
            return -1
        if selling_price is None:
            logger.info(get_message("main", "process_autosearch_json_to_data_no_sellers"))
            return -1

        if autobuy_price < 0.16 and fee == 13: # Steam hidden 0.02$ fee (Only for RadarMode as USD is the main and only currency)
            profit = selling_price - 0.02 - autobuy_price
            profit_percent = ((selling_price - 0.02) / autobuy_price - 1) * 100
        else:
            profit = selling_price * (1 - fee / 100) - autobuy_price
            profit_percent = (selling_price * (1 - fee / 100) / autobuy_price - 1) * 100

        if profit_percent < needed_profit:
            logger.info(get_message("main", "process_autosearch_json_to_data_less_profit", profit_percent, needed_profit))
            return -1

        total_sales_month = get_total_sales(history_data)
        if total_sales_month < needed_sales:
            logger.info(get_message("main", "process_autosearch_json_to_data_less_sales", total_sales_month, needed_sales))
            return -1

        item_nameid = json_data["item_nameid"]
        full_skin_name = await get_full_skin_name_nameid(item_nameid)
        encoded_full_skin_name = urllib.parse.quote(full_skin_name)

        skin_name = split_item_name(full_skin_name)[0]
        skin_exterior = split_item_name(full_skin_name)[1]

        return {
            "skin_name": skin_name,
            "exterior": skin_exterior,
            "price": selling_price,
            "autobuy_price": autobuy_price,
            "profit": profit,
            "profit_percent": profit_percent,
            "link": f"https://steamcommunity.com/market/listings/730/{encoded_full_skin_name}",
            "total_sales_month": total_sales_month,
            "item_nameid": item_nameid,
        }

    except (KeyError, TypeError, AttributeError) as e:
        logger.warning(get_message("main", "process_autosearch_json_to_data_key_error", e))
        return []

async def process_main_json_to_data(json_data, needed_amount: int, currency: int, fee: float):
    if not json_data:
        global current_client
        current_client =  None
        logger.warning(get_message("main", "process_main_json_to_data_json_unsuccessful"))
        return []
    try:
        autobuy_price = await process_autobuy_json_to_data(json_data.get("autobuy_data"))
        item_nameid = json_data.get("item_nameid", "Не найдено")

        if autobuy_price is None:
            logger.info(get_message("main", "process_main_json_to_data_no_buyers"))
            return []

        processed_data = []
        listing_info = json_data.get("market_data").get("listinginfo", {})

        assets_check = json_data.get("market_data")
        if "assets" not in assets_check or not isinstance(assets_check["assets"], dict):
            logger.info(get_message("main", "process_main_json_to_data_item_not_listed", item_nameid))
            return []
        assets = assets_check.get("assets", {}).get("730", {}).get("2", {})

        currency = int(currency) # Transforms to string for some reason
        if json_data.get("has_exterior"):
            for listing_id, info in islice(listing_info.items(), needed_amount):
                asset_id = info.get("asset", {}).get("id", "")
                asset_info = assets.get(asset_id, {})
                stickers = extract_stickers_info(asset_info.get("descriptions", [{}]))
                keychains = extract_keychain_info(asset_info.get("descriptions", [{}]))

                price = (info.get("converted_price", 0) + info.get("converted_fee", 0)) / 100
                profit = price * (1 - fee / 100) - autobuy_price
                profit_percent = (price * (1 - fee / 100) / autobuy_price - 1) * 100

                skin_name = asset_info.get("market_hash_name", "Имя не найдено")
                skin_exterior = asset_info.get("descriptions", [{}])[0].get("value", "Не найдено")
                encoded_skin = urllib.parse.quote(skin_name)

                row = {
                    "skin_name": skin_name,
                    "exterior": skin_exterior,
                    "price": price,
                    "autobuy_price": autobuy_price,
                    "profit": profit,
                    "profit_percent": profit_percent,
                    "currency": get_currency_symbol(currency),
                    "link": f"https://steamcommunity.com/market/listings/730/{encoded_skin}",
                    "inspect_link": asset_info.get("market_actions", [{}])[0].get("link", "Ссылка не найдена"),
                    "sticker_image_urls": stickers.get("images_url"),
                    "sticker_titles": stickers.get("sticker_titles"),
                    "sticker_urls": stickers.get("sticker_urls"),
                    "keychain_image_url": keychains.get("image_url"),
                    "keychain_title": keychains.get("keychain_title"),
                    "keychain_url": keychains.get("keychain_url"),
                    "item_nameid": item_nameid
                }
                processed_data.append(row)
        else:
            for listing_id, info in islice(listing_info.items(), needed_amount):
                asset_id = info.get("asset", {}).get("id", "")
                asset_info = assets.get(asset_id, {})
                stickers = extract_stickers_info(asset_info.get("descriptions", [{}])) # Patches are same as Stickers

                price = (info.get("converted_price", 0) + info.get("converted_fee", 0)) / 100
                profit = price * (1 - fee / 100) - autobuy_price
                profit_percent = (price * (1 - fee / 100) / autobuy_price - 1) * 100

                skin_name = asset_info.get("market_hash_name", "Имя не найдено")
                encoded_skin = urllib.parse.quote(skin_name)

                row = {
                    "skin_name": skin_name,
                    "price": price,
                    "autobuy_price": autobuy_price,
                    "profit": profit,
                    "profit_percent": profit_percent,
                    "currency": get_currency_symbol(currency),
                    "link": f"https://steamcommunity.com/market/listings/730/{encoded_skin}",
                    "inspect_link": asset_info.get("market_actions", [{}])[0].get("link", "Ссылка не найдена"),
                    "sticker_image_urls": stickers.get("images_url"),
                    "sticker_titles": stickers.get("sticker_titles"),
                    "sticker_urls": stickers.get("sticker_urls"),
                    "item_nameid": item_nameid
                }
                processed_data.append(row)

        return processed_data
    except (KeyError, TypeError, AttributeError) as e:
        logger.warning(get_message("main", "process_main_json_to_data_key_error", str(e)))
        return []

async def fetch_and_process(currency = None, quality = None, amount = None, skin_str = None, steam_fee = None, profit = None, sales = None, souvenir = False, stattrak = False, knife = False, skip_boosted = False, boost_percentage = None, mode="DEFAULT"):
        curr = currency or DEFAULT_CURRENCY
        quality = quality
        amount = amount or DEFAULT_AMOUNT_QUERY
        skin_str = skin_str or DEFAULT_SKIN
        fee = steam_fee or DEFAULT_STEAM_FEE
        prof = profit or DEFAULT_AMOUNT_PROFIT
        sale = sales or DEFAULT_AMOUNT_SALES
        boost = boost_percentage or DEFAULT_BOOST

        json_data = await fetch_market_json(curr, quality, amount, skin_str, souvenir, stattrak, knife, skip_boosted, boost, mode)
        if json_data.get("market_data") == -1 or json_data.get("market_data") == -2:
            return json_data.get("market_data")
        elif not json_data:
            skin_logger_name = skin_str if skin_str else json_data.get("item_nameid", "(Предмет не найден)")
            logger.warning(get_message("main", "fetch_and_process_data_not_retrieved",skin_logger_name))
            return None

        if mode == "RANDOM":
            json_formatted = await process_autosearch_json_to_data(json_data, fee, prof, sale)
        else:
            json_formatted = await process_main_json_to_data(json_data, amount, curr, fee)

        if json_formatted == -1:
            return -1

        return json_formatted

async def app_main(page: ft.Page):
    await ui_main(page, fetch_data_callback=fetch_and_process)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-level", type=str, default=None,
                        help="Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)")

    args = parser.parse_args()

    if args.log_level:
        log_level = args.log_level.upper()
        logger.setLevel(log_level)

    logger.info("Start Coroutine")
    asyncio.run((ft.app_async(target=app_main, assets_dir="assets")))
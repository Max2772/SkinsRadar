import json
from src.logger import logger, get_message

STEAM_CURRENCIES_PATH = "data/steam_currencies.json"

def load_currencies():
    try:
        with open(STEAM_CURRENCIES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info(get_message("currencies", "load_currencies_file_not_found"))
        return []
    except json.JSONDecodeError:
        logger.info(get_message("currencies", "load_currencies_decode_error"))
        return []

def get_currency_by_code(steam_code: int):
    currencies = load_currencies()
    for currency in currencies:
        if currency["steam_code"] == steam_code:
            return currency
    return None

def get_currency_symbol(steam_code: int):
    currency = get_currency_by_code(steam_code)
    return currency["symbol"] if currency else "X"

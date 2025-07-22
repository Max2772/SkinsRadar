import logging
from logging.handlers import RotatingFileHandler
from src.log_messages import MAIN_MESSAGES, UTILS_MESSAGES, SKINS_MANAGER_MESSAGES, PROXY_MANAGER_MESSAGES, CURRENCIES_MESSAGES, HANDLERS_MESSAGES

LOG_LEVEL_MAPPING = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "FATAL": logging.CRITICAL,
    "CRITICAL": logging.CRITICAL,
}

LOG_MESSAGES = {
    "main": MAIN_MESSAGES,
    "utils": UTILS_MESSAGES,
    "skins_manager": SKINS_MANAGER_MESSAGES,
    "proxies_manager": PROXY_MANAGER_MESSAGES,
    "currencies": CURRENCIES_MESSAGES,
    "handlers": HANDLERS_MESSAGES
}

LOG_LANGUAGE = None
LOG_LEVEL = None
_loger = None

def set_log_level(log_level: str):
    global LOG_LEVEL
    LOG_LEVEL = log_level if log_level in LOG_LEVEL_MAPPING else "INFO"

def set_log_language(log_language: str):
    global LOG_LANGUAGE
    LOG_LANGUAGE = log_language if log_language in ["en", "ru"] else "en"

def get_message(module: str, key: str, *args) -> str:
    return LOG_MESSAGES[module][LOG_LANGUAGE][key].format(*args)

def setup_logger():
    global _loger
    if _loger is not None:
        return _loger

    log_level = LOG_LEVEL_MAPPING.get(LOG_LEVEL, logging.INFO)

    _loger = logging.getLogger(__name__)
    _loger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    if log_level == logging.INFO:
        console_handler.setFormatter(logging.Formatter('%(asctime)s - [%(processName)-11s] %(levelname)s - %(message)s'))
    else:
        console_handler.setFormatter(
            logging.Formatter('%(asctime)s - [%(processName)-11s] %(levelname)s - '
                              '%(module)s.%(funcName)s:%(lineno)d - %(message)s'))
    _loger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        'logs.log', maxBytes=2*1024*1024, backupCount=3, encoding="utf-8", errors="replace"
    )
    file_handler.setLevel(log_level)
    if log_level == logging.INFO:
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - [%(processName)-11s] %(message)s'))
    else:
        file_handler.setFormatter(logging.Formatter('%(asctime)s - [%(processName)-11s] %(levelname)s - '
                                                    '%(module)s.%(funcName)s:%(lineno)d - %(message)s'))
    _loger.addHandler(file_handler)

    _loger.info("Loger initialized")
    return _loger

def get_logger():
    global _loger
    if _loger is None:
        temp_logger = logging.getLogger(__name__)
        return temp_logger
    return _loger
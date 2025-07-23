import json
from typing import Optional, Union
import re
from datetime import datetime, timedelta
from src.logger import get_logger, get_message

logger = get_logger()

def split_item_name(full_skin_name: str) -> tuple[str, str]:
    pattern = r"^(.*?)(?:\s*\((Battle-Scarred|Factory New|Field-Tested|Minimal Wear|Well-Worn)\))?$"
    match = re.match(pattern, full_skin_name.strip())

    if match:
        name = match.group(1)
        exterior = match.group(2) or ""
        return name, exterior
    else:
        return full_skin_name, ""

def clean_price(autobuy_price: str) -> Optional[float]:
    if autobuy_price is None:
        return None
    if not isinstance(autobuy_price, str):
        return float(autobuy_price)

    parts = autobuy_price.split()
    for part in parts:
        if re.search(r"[\d,.]", part):
            cleaned = re.sub(r"[^\d,.]", "", part).replace(",", ".")
            if cleaned.count(".") > 1:
                cleaned = cleaned[:cleaned.find(".", cleaned.find(".") + 1)]
                match = re.match(r"(\d+)[,.](\d{0,999})", cleaned)
                return float(match.group(1) + match.group(2)) if match and match.group(2) else float(match.group(1) * 1000) if match else 0.0
            else:
                match = re.match(r"(\d+)[,.](\d{0,4})", cleaned)
                return float(match.group(1) + "." + match.group(2)) if match and match.group(2) else float(match.group(1)) if match else 0.0
    return None

def check_exterior(full_skin_name: str) -> bool:
    name, exterior = split_item_name(full_skin_name)
    return not exterior == ""

def extract_stickers_info(descriptions): # Same for patches
    for item in descriptions:
        if item.get("name") == "sticker_info":
            html = item.get("value", "Нет стикеров")
            if not html or html == "Нет стикеров":
                return {"images_url": [], "sticker_titles": [], "sticker_urls": []}
            image_urls = re.findall(r'src="([^"]+)"', html)
            titles = [title.replace("Sticker:", "Sticker |").replace("Patch:", "Patch |") for title in  re.findall(r'title="([^"]+)"', html)]
            sticker_urls = ["https://steamcommunity.com/market/listings/730/" + title for title in titles]

            result = {
                "images_url": image_urls[:5],
                "sticker_titles": titles[:5],
                "sticker_urls": sticker_urls[:5]
            }
            return result
    return {"images_url": [], "sticker_titles": [], "sticker_urls": []}

def extract_keychain_info(descriptions):
    for item in descriptions:
        if item.get("name") == "keychain_info":
            html = item.get("value", "Нет брелков")
            if html == "Нет брелков":
                return {"image_url": [], "keychain_title": [], "keychain_url": []}

            image_url = re.search(r'src="([^"]+)"', html).group(1)
            title = re.search(r'title="([^"]+)"', html)

            if not (image_url and title):
                return {"image_url": [], "keychain_title": [], "keychain_url": []}

            title = title.group(1).replace("Charm:", "Charm |")
            link = "https://steamcommunity.com/market/listings/730/" + title

            result = {
                "image_url": image_url,
                "keychain_title": title,
                "keychain_url": link
            }
            return result
    return {"image_url": [], "keychain_title": [], "keychain_url": []}

def extract_history_prices(html: str) -> Optional[list]:
    pattern = r"var line1\s*=\s*(\[\[.*?\]\]);"
    match = re.search(pattern, html, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            return None
    return None

def is_skin_boosted(history_data, max_boost: float) -> bool:
    one_month_ago = datetime.now() - timedelta(days=30)

    prices = []
    sales = []

    for entry in reversed(list(history_data)):
        try:
            entry_date = datetime.strptime(entry[0], "%b %d %Y %H: +0")
            if one_month_ago > entry_date:
                break
            if one_month_ago <= entry_date:
                prices.append(float(entry[1]))
                sales.append(int(entry[2]))
        except (ValueError, TypeError) as e:
            logger.error(get_message("utils", "is_skin_boosted_entry_error", str(entry), str(e)))

    if not prices:
        logger.info(get_message("utils", "is_skin_boosted_no_sales_data"))
        return False

    # avg_price = sum(prices) / len(prices) could be used for more complicated check
    avg_sales = sum(sales) / len(sales)

    min_price = float('inf')
    max_price = 0.0
    for price, sales in zip(prices, sales):
        if sales >= avg_sales:
            min_price = min(price, min_price)
            max_price = max(price, max_price)

    if min_price == float('inf') or max_price == 0:
        logger.info(get_message("utils", "is_skin_boosted_no_valid_prices"))
        return False

    # To remove debug later
    # logger.debug(f"AVG_SALES: {avg_sales}")
    # logger.debug(f"MIN_PRICE: {min_price}, MAX_PRICE: {max_price}")

    price_diff_percent = ((max_price - min_price) / min_price) * 100
    return price_diff_percent > max_boost

def get_total_sales(data) -> int:
    one_month_ago = datetime.now() - timedelta(days=31)

    total_sales = 0
    for entry in reversed(list(data)):
        try:
            entry_date = datetime.strptime(entry[0], "%b %d %Y %H: +0")
            if one_month_ago > entry_date:
                break
            if one_month_ago <= entry_date:
                total_sales += int(entry[2])
        except ValueError as e:
            logger.error(get_message("utils", "get_total_sales_date_error", entry[0], str(e)))
    return total_sales

def has_patches(data_skins_table) -> bool:
    for skin in data_skins_table:
        if skin.get("sticker_image_urls"):
            return True
    return False

def is_skin_supported(full_skin_name: str) -> tuple:
    pattern_souvenir = r"^.{0,5}Souvenir\s+.*"
    pattern_stattrak = r"^.{0,5}StatTrak™\s+.*"
    pattern_knife = r"^★\s+.*"

    match_souvenir = re.match(pattern_souvenir, full_skin_name.strip())
    match_stattrak = re.match(pattern_stattrak, full_skin_name.strip())
    match_knife = re.match(pattern_knife, full_skin_name.strip())

    return match_souvenir, match_stattrak, match_knife



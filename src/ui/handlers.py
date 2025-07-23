from typing import Optional
import asyncio
from fuzzywuzzy import fuzz

import flet as ft
from flet import Text, ListTile, Colors

from src.proxies_manager import update_proxies, wipe_all_proxies, is_proxies_db_empty
from src.skins_manager import update_skins, get_item_results, get_max_rows, get_current_row, decrement_current_row, reset_max_rows
from src.utils import split_item_name, check_exterior
from src.ui.data_table import create_skins_table_datatable, create_auto_table_datatable
from src.logger import get_logger, get_message
from src.proxies_manager import extract_proxies

logger = get_logger()

async def reload_skins_table(page: ft.Page, fetch_data_callback=None):
    table_container = page.data["table_container"]
    current_skin = page.data["current_skin"]
    if not isinstance(table_container.content, ft.ProgressRing):
        table_container.content = ft.ProgressRing()
    page.update()
    try:
        if current_skin:
            table_container.content = await create_skins_table_datatable(page, fetch_data_callback=fetch_data_callback)
        else:
            table_container.content = Text("Please choose a skin for search")
    except Exception as e:
        table_container.content = ft.Column([Text(f"Error loading data: {str(e)}", color=Colors.RED),  ft.ProgressRing()],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        logger.warning(get_message("handlers", "reload_skins_table_error", str(e)))
        page.update()
        await asyncio.sleep(1)
        await reload_skins_table(page, fetch_data_callback=fetch_data_callback)
    finally:
        page.update()

async def update_search_results(query: str) -> Optional[int]:
    if not query:
        return None
    search_results = []
    results = await get_item_results(query)
    count = 0
    for (name,) in results:
        if count >= 5:
            break
        if fuzz.partial_ratio(query.lower(), name.lower()) > 80:
            search_results.append(name)
            count += 1
    return search_results

async def handle_search_suggestions(e) -> None:
    search_results = await update_search_results(e.control.value)
    search_bar_result = e.page.data["search_bar_result"]
    search_bar_result.content.controls = []

    if not search_results:
        search_bar_result.visible = False
    else:
        search_bar_result.visible = True
        search_bar_result.content.controls.extend([
            ft.Container(
            content=ListTile(
                title=Text(
                    full_skin_name,
                    text_align=ft.TextAlign.CENTER,
                    size=16
                ),
                on_click=lambda e, skin=full_skin_name: close_search_bar(e, skin)
            ),
            width=800,
            alignment=ft.alignment.center,
            bgcolor=e.page.theme_mode,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=16,
            ) for full_skin_name in search_results
        ])
    e.page.update()

def close_search_bar(e, full_skin_name) -> None:
    search_bar = e.page.data["search_bar"]
    search_bar_result = e.page.data["search_bar_result"]
    dropdown_exterior = e.page.data["dropdown_exterior"]
    fetch_data_callback = e.page.data["fetch_data_callback"]
    search_bar.open = False
    if full_skin_name:
        skin_name = split_item_name(full_skin_name)[0]
        e.page.data["current_skin"] = skin_name
        if check_exterior(full_skin_name):
            skin_exterior = split_item_name(full_skin_name)[1]
            e.page.data["current_exterior"] = skin_exterior
            dropdown_exterior.value = skin_exterior
        else:
            e.page.data["current_exterior"] = None
            dropdown_exterior.value = "No Exterior"
        e.page.run_task(reload_skins_table, e.page, fetch_data_callback)
    search_bar_result.content.controls = []
    search_bar_result.visible = False
    search_bar.value = ""
    e.page.update()

def validate_listings_amount(e):
    try:
        amount = int(e.control.value)
        if amount < 1 or amount > 100:
            e.control.error_text = "Should be between 1 and 100"
            e.control.value = ""
        else:
            e.control.error_text = None
            e.page.data["amount_query"] = amount
    except ValueError:
        e.control.error_text = "Incorrect character"
    finally:
        e.page.update()

def validate_profit_amount(e):
    try:
        amount = float(e.control.value)
        if amount < -100 or amount > 100:
            e.control.error_text = "Should be between -100 and 100"
            e.control.value = ""
        else:
            e.control.error_text = None
            e.page.data["amount_profit"] = amount
    except ValueError:
        e.control.error_text = "Incorrect character"
    finally:
        e.page.update()

def validate_sales_amount(e):
    try:
        amount = int(e.control.value)
        if amount < 1:
            e.control.error_text = "Should be more than 1"
            e.control.value = ""
        else:
            e.control.error_text = None
            e.page.data["amount_sales"] = amount
    except ValueError:
        e.control.error_text = "Incorrect character"
    finally:
        e.page.update()

async def on_update_skins_db_button_click(e):
    update_skins_db_button = e.page.data["update_skin_db_button"]
    update_skins_db_button.disabled = True
    update_skins_db_button.text = "Updating Skins Database..."
    e.page.update()
    try:
        await update_skins()
    except Exception as ex:
        logger.warning(get_message("handlers", "on_update_skins_db_button_click_error", str(ex)))
    finally:
        update_skins_db_button.disabled = False
        update_skins_db_button.text = "Update Skins Database"
        e.page.update()

async def on_wipe_proxies_db_button_click(e):
            if not await is_proxies_db_empty():
                wipe_proxy_button = e.page.data["wipe_proxy_button"]
                wipe_proxy_button.disabled = True
                wipe_proxy_button.text = "Delete all proxies..."
                e.page.update()
                try:
                    await wipe_all_proxies()
                except Exception as ex:
                    logger.warning(get_message("handlers", "on_wipe_proxies_db_button_click_error", str(ex)))
                finally:
                    wipe_proxy_button.disabled = False
                    wipe_proxy_button.text = "Wipe Proxies Database"
                    e.page.update()

def on_dropdown_exterior_change(e):
    if e.control.value == "No Exterior":
        e.page.data["current_exterior"] = None
    else:
        e.page.data["current_exterior"] = e.control.value
    logger.info(get_message("handlers", "on_dropdown_exterior_change_success", e.control.value))
    e.page.update()

def on_dropdown_currency_change(e):
    e.page.data["currency"] = e.control.value
    logger.info(get_message("handlers", "on_dropdown_currency_change_success", e.control.value))
    e.page.update()













def on_validate_input_field(e):
    try:
        amount = float(e.control.value)
        if amount < 0 or amount > 100:
            e.control.error_text = "Should be between 0 and 100"
            e.control.value = ""
        elif amount == 0:
            e.control.error_text = "Can't be 0"
        else:
            e.control.error_text = None
            return amount
    except ValueError:
        e.control.error_text = "Incorrect character"
    finally:
        e.page.update()

def on_save_input_field(e, status_text: ft.Text, page_parametr_str: str):
    try:
        amount = on_validate_input_field(e)

        e.page.data[page_parametr_str] = amount
        logger.info(get_message("handlers", "on_save_input_field_success", page_parametr_str, amount))
        e.control.value = ""
    except ValueError:
        e.control.error_text = "Incorrect character"
    finally:
        status_text.value = f"Current: {amount}%"
        e.page.update()

def on_toggle_theme(e):
    e.page.theme_mode = ft.ThemeMode.DARK if e.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
    logger.info(get_message("handlers", "on_toggle_theme_success", e.page.theme_mode))
    e.page.update()

#######################################  AUTO TABLE UI HANDLERS  #######################################

async def restore_button_color(control):
    await asyncio.sleep(0.2)
    setattr(control, "bgcolor", ft.Colors.BLUE_50),
    control.update()

async def start_parsing(page: ft.Page):
    if page.data["is_auto_parsing"]:
        return

    page.data["is_auto_parsing"] = True
    logger.info(get_message("handlers", "start_parsing_start"))

    auto_table_container = page.data["auto_table_container"]

    if not auto_table_container.content or not isinstance(auto_table_container.content, ft.DataTable):
        table = await create_auto_table_datatable(page, page.data["fetch_data_callback"])
        auto_table_container.content = table
    original_content = auto_table_container.content
    auto_table_container.content = ft.Column([original_content, ft.ProgressRing()],
                                             horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    page.update()
    while page.data["is_auto_parsing"]:
        try:
            current_row = await get_current_row()
            if current_row > await get_max_rows():
                await reset_max_rows()

            new_row = await create_auto_table_datatable(
                page,
                page.data["fetch_data_callback"],
                is_souvenir_supported(page),
                is_stattrak_supported(page),
                is_knife_supported(page),
                is_skip_boosted_supported(page),
                True
            )
            auto_table_container.content = original_content

            if new_row == -1:
                logger.info(get_message("handlers", "start_parsing_item_filtered"))
            elif new_row == -2:
                logger.info(get_message("handlers", "start_parsing_item_boosted"))
            elif new_row:
                auto_table_container.content.rows.append(new_row)
                logger.info(get_message("handlers", "start_parsing_row_added"))
                page.data["data_auto_table"].append(page.data["new_data_auto_table"])
                page.update()
            else:
                logger.warning(get_message("handlers", "start_parsing_row_failed"))
                if await get_current_row() > 1:
                    await decrement_current_row()
        except Exception as e:
            logger.warning(get_message("handlers", "start_parsing_error", str(e)))
            auto_table_container.content = ft.Column(
                controls=[original_content, ft.Text(f"Error loading data: {str(e)}", color=ft.Colors.RED)],
                alignment=ft.MainAxisAlignment.CENTER,
            )
            page.update()
            auto_table_container.content = original_content
            page.update()
            continue
        finally:
            if await get_current_row() > await get_max_rows():
                logger.info(get_message("handlers", "start_parsing_completed"))
                await pause_auto_parsing(page)
                break
        await asyncio.sleep(1)

async def pause_auto_parsing(page: ft.Page):
    page.data["is_auto_parsing"] = False
    logger.info(get_message("handlers", "pause_auto_parsing_success"))
    page.update()

async def clean_auto_table(page: ft.Page):
    auto_table_container = page.data["auto_table_container"]
    if auto_table_container and isinstance(auto_table_container.content, ft.DataTable):
        auto_table_container.content.rows.clear()
        page.data["data_auto_table"] = []

    logger.info(get_message("handlers", "clean_auto_table_success"))
    page.update()

def is_souvenir_supported(page: ft.Page) -> bool:
    return page.data["souvenir_checkbox"].value

def is_stattrak_supported(page: ft.Page) -> bool:
    return page.data["stattrak_checkbox"].value

def is_knife_supported(page: ft.Page) -> bool:
    return page.data["knife_checkbox"].value

def is_skip_boosted_supported(page: ft.Page) -> bool:
    return page.data["skip_boosted_checkbox"].value

def on_skin_type_checkbox_change(e, text: str):
    if e.control.value:
        logger.info(get_message("handlers", "on_skin_type_checkbox_change_enabled", text))
    else:
        logger.info(get_message("handlers", "on_skin_type_checkbox_change_disabled", text))

async def on_files_picked_proxy_button(e: ft.FilePickerResultEvent):
    proxy_button = e.page.data["proxy_button"]
    status_text = proxy_button.controls[1] if isinstance(proxy_button.controls[1], ft.Text) else None
    if not status_text:
        return
    status_text.value = ""

    try:
        if e.files:
            all_working_proxies = []
            for file in e.files:
                file_path = file.path
                try:
                    all_working_proxies += await extract_proxies(file_path)
                except Exception as ex:
                    logger.error(get_message("handlers", "on_files_picked_proxy_button_file_error", file_path, str(ex)))
                    status_text.value = get_message("handlers", "on_files_picked_proxy_button_file_error")
            inserted_amount = await update_proxies(all_working_proxies)
            status_text.value = get_message("handlers", "on_files_picked_proxy_button_inserted_amount", inserted_amount)
        else:
            logger.warning(get_message("handlers", "on_files_picked_proxy_button_no_file"))
            status_text.value = get_message("handlers", "on_files_picked_proxy_button_no_file")
    except Exception as ex:
        logger.warning(get_message("handlers", "on_files_picked_proxy_button_error", str(ex)))
        status_text.value = get_message("handlers", "on_files_picked_proxy_button_error", str(ex))
    finally:
        e.page.update()

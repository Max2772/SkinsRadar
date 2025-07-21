import flet as ft
import asyncio
from flet.core.page import RouteChangeEvent, ViewPopEvent

from src.ui.ui_components import (
    create_search_bar,
    create_search_bar_result,
    create_proxy_button,
    create_wipe_proxies_db_button,
    create_update_skins_db_button,
    create_listings_amount_field,
    create_profit_amount_field,
    create_sales_amount_field,
    create_exterior_dropdown,
    create_currency_dropdown,
    create_table_container,
    create_splash_screen,
    create_app_bar,
    create_settings_input_field,
    create_toggle_theme_button,
    create_auto_table_container,
    create_skin_type_checkbox
)
from src.ui.views import create_skins_table_view, create_settings_view, create_auto_table_view
from src.currencies import load_currencies
from src.ui.handlers import on_files_picked_proxy_button

DEFAULT_SKIN = None
DEFAULT_AMOUNT_QUERY = 10
DEFAULT_AMOUNT_PROFIT = -100
DEFAULT_AMOUNT_SALES = 1
DEFAULT_CURRENCY = 1
DEFAULT_STEAM_FEE = 13.0
DEFAULT_BOOST = 30.0

async def main(page: ft.Page, fetch_data_callback=None):
    page.title = "Skins Radar"
    page.window.resizable = True
    page.theme_mode = ft.ThemeMode.SYSTEM

    page.add(create_splash_screen(page))
    file_picker = ft.FilePicker(on_result=on_files_picked_proxy_button)
    page.overlay.append(file_picker)
    page.update()

    search_bar_result = create_search_bar_result()
    search_bar = create_search_bar()
    proxy_button = create_proxy_button(file_picker)
    wipe_proxy_button = create_wipe_proxies_db_button()
    update_skins_db_button = create_update_skins_db_button()
    listings_amount_field = create_listings_amount_field(DEFAULT_AMOUNT_QUERY)
    profit_amount_field = create_profit_amount_field(DEFAULT_AMOUNT_PROFIT)
    sales_amount_field = create_sales_amount_field(DEFAULT_AMOUNT_SALES)
    dropdown_exterior = create_exterior_dropdown()
    table_container = create_table_container()
    auto_table_container = create_auto_table_container()
    app_bar = create_app_bar()
    theme_button = create_toggle_theme_button()
    souvenir_checkbox = create_skin_type_checkbox("Souvenir")
    stattrak_checkbox = create_skin_type_checkbox("StatTrak™")
    knife_checkbox = create_skin_type_checkbox("★ Knife | Gloves", True)
    skip_boosted_checkbox = create_skin_type_checkbox("🗲 Skip Boosted", True)

    await asyncio.sleep(0) # Change to 0 when developing
    page.controls.clear()

    page.data = {
        "current_skin": DEFAULT_SKIN,
        "amount_query": DEFAULT_AMOUNT_QUERY,
        "amount_profit": DEFAULT_AMOUNT_PROFIT,
        "amount_sales": DEFAULT_AMOUNT_SALES,
        "current_exterior": None,
        "currency": DEFAULT_CURRENCY,
        "currencies": load_currencies(),
        "steam_fee": DEFAULT_STEAM_FEE,
        "max_boost": DEFAULT_BOOST,
        "search_bar": search_bar,
        "search_bar_result": search_bar_result,
        "dropdown_exterior": dropdown_exterior,
        "table_container": table_container,
        "proxy_button": proxy_button,
        "wipe_proxy_button": wipe_proxy_button,
        "update_skin_db_button": update_skins_db_button,
        "fetch_data_callback": fetch_data_callback,
        "data_skins_table": [],
        "auto_table_container": auto_table_container,
        "data_auto_table": [],
        "previous_view": page.views[-1].route,
        "is_auto_parsing": False,
        "souvenir_checkbox": souvenir_checkbox,
        "stattrak_checkbox": stattrak_checkbox,
        "knife_checkbox": knife_checkbox,
        "skip_boosted_checkbox": skip_boosted_checkbox,
        "file_picker": file_picker
    }

    # Needs to be initialized after page.data
    dropdown_currency = create_currency_dropdown(page)
    commission_field = create_settings_input_field(page, "Commission Percentage (%)", "steam_fee")
    boost_field = create_settings_input_field(page, "Max Boost Percentage (%)", "max_boost")

    skins_table_view = create_skins_table_view(
        search_bar,
        search_bar_result,
        listings_amount_field,
        dropdown_exterior,
        dropdown_currency,
        table_container,
        app_bar
    )

    settings_view = create_settings_view(
        theme_button,
        commission_field,
        boost_field,
        proxy_button,
        wipe_proxy_button,
        update_skins_db_button,
        app_bar
    )

    auto_table_view = create_auto_table_view(
        profit_amount_field,
        sales_amount_field,
        souvenir_checkbox,
        stattrak_checkbox,
        knife_checkbox,
        skip_boosted_checkbox,
        auto_table_container,
        app_bar
    )

    page.views.append(skins_table_view)
    page.update()
    page.go("/skins_table")

    def route_change(e: RouteChangeEvent) -> None:
        if page.route == "/settings":
            page.data["previous_view"] = page.views[-1].route

        page.views.clear()

        if page.route == "/settings":
            page.views.append(settings_view)
        elif page.route == "/auto_table":
            page.views.append(auto_table_view)
        else:
            page.views.append(skins_table_view)
        page.update()

    def view_pop(e: ViewPopEvent) -> None:
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go("/skins_table")
        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
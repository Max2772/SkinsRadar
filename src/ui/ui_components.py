import flet as ft
from flet import SearchBar, Container, Column, ElevatedButton, TextField, Colors, Icons
from src.ui.handlers import handle_search_suggestions, on_proxy_button_click, on_update_skins_db_button_click, validate_listings_amount, validate_profit_amount, validate_sales_amount, on_dropdown_exterior_change, on_dropdown_currency_change, on_validate_input_field, on_save_input_field, on_toggle_theme, on_skin_type_checkbox_change

def create_search_bar_result() -> ft.Container:
    return Container(
        visible=False,
        content=Column(controls=[])
    )

def create_search_bar() -> ft.SearchBar:
    return SearchBar(
        view_elevation=5,
        divider_color=ft.Colors.AMBER,
        bar_hint_text="Enter skin name...",
        view_hint_text="Choose a skin from the options...",
        on_change=handle_search_suggestions
    )

def create_proxy_button() -> ft.ElevatedButton:
    return ElevatedButton(
        text="Update Proxy",
        icon=Icons.VPN_LOCK,
        style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_600, color=ft.Colors.WHITE),
        on_click=on_proxy_button_click
    )

def create_update_skins_db_button() -> ft.ElevatedButton:
    return ElevatedButton(
        text="Update Skins Database",
        icon=Icons.DATASET_OUTLINED,
        style=ft.ButtonStyle(bgcolor=ft.Colors.BLACK87, color=ft.Colors.WHITE),
        on_click=on_update_skins_db_button_click
    )

def create_listings_amount_field(default_query: int) -> ft.TextField:
    return TextField(
        label="Amount",
        value=str(default_query),
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: validate_listings_amount(e)
    )

def create_profit_amount_field(default_profit: float) -> ft.TextField:
    return TextField(
        label="Profit%",
        border_color=ft.Colors.BLUE_50,
        color=ft.Colors.BLUE_50,
        label_style=ft.TextStyle(color=ft.Colors.BLUE_50),
        value=str(default_profit),
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: validate_profit_amount(e)
    )

def create_sales_amount_field(default_sales: int) -> ft.TextField:
    return TextField(
        label="Sales",
        border_color=ft.Colors.BLUE_50,
        color=ft.Colors.BLUE_50,
        label_style=ft.TextStyle(color=ft.Colors.BLUE_50),
        value=str(default_sales),
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=lambda e: validate_sales_amount(e)
    )

def create_exterior_dropdown() -> ft.Dropdown:
    return ft.Dropdown(
        label="Exterior",
        options=[
            ft.dropdown.Option("Factory New", "Factory New"),
            ft.dropdown.Option("Minimal Wear", "Minimal Wear"),
            ft.dropdown.Option("Field-Tested", "Field-Tested"),
            ft.dropdown.Option("Well-Worn", "Well-Worn"),
            ft.dropdown.Option("Battle-Scarred", "Battle-Scarred"),
            ft.dropdown.Option("No Exterior", "No Exterior")
        ],
        value="Field-Tested",
        on_change=lambda e: on_dropdown_exterior_change(e)
    )

def create_currency_dropdown(page: ft.Page) -> ft.Dropdown:
    dropdown_options = [
        ft.dropdown.Option(
            key=currency["steam_code"],
            text=f"{currency['symbol']} ({currency['iso_code']})"
        )
        for currency in page.data["currencies"]
    ]
    return ft.Dropdown(
        label="Currency",
        options=dropdown_options,
        value="1",
        on_change=lambda e: on_dropdown_currency_change(e)
    )

def create_table_container() -> ft.Container:
    return Container(
        padding=10,
        content=ft.Text("Enter a skin's name for search"),
        alignment=ft.alignment.center
    )

def create_auto_table_container() -> ft.Container:
    return ft.Container(
        padding=10,
        content=ft.Text("Press Start to start parsing"),
        alignment=ft.alignment.center
    )

def create_app_bar() -> ft.AppBar:
    return ft.AppBar(
        leading=ft.Container(
            content=ft.Image(
                src="assets/icon_white.png",
                opacity=0.8,
                error_content=ft.Text("X"),
                width=24,
                height=24,
                fit=ft.ImageFit.CONTAIN,
            ),
            width=20,
            height=20,
            padding=8,
        ),
        title=ft.Text(
            "SkinsRadar",
            opacity=0.8,
            size=24,
            weight=ft.FontWeight.BOLD,
            font_family="Montserrat",
            color=ft.Colors.WHITE
        ),
        center_title=False,
        bgcolor=ft.Colors.BLUE_700,
        actions=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.TABLE_CHART,
                            icon_color=Colors.WHITE,
                            opacity=0.8,
                            tooltip="Skins Table",
                            on_click=lambda e: e.page.go("/skins_table")
                        ),
                        ft.IconButton(
                            icon=ft.Icons.AUTO_FIX_HIGH,
                            icon_color=Colors.WHITE,
                            opacity=0.8,
                            tooltip="Auto Parsing",
                            on_click=lambda e: e.page.go("/auto_table")
                        ),
                        ft.IconButton(
                            icon=ft.Icons.SETTINGS,
                            icon_color=Colors.WHITE,
                            opacity=0.8,
                            tooltip="Settings",
                            on_click=lambda e: e.page.go("/settings")
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.END,
                ),
                padding=ft.padding.only(right=10),
            )
        ],
    )

def create_splash_screen(page: ft.Page) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src="assets/icon_white.png",
                    error_content=ft.Text("X"),
                    width=128,
                    height=128,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text(
                    "SkinsRadar",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    font_family="Montserrat",
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                    ),
                ft.Text(
                    "Loading...",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    font_family="Montserrat",
                    color=ft.Colors.WHITE,
                    opacity=0.8,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.ProgressRing(
                    width=50,
                    height=50,
                    stroke_width=5,
                    color=ft.Colors.WHITE,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        width=page.width,
        height=page.height,
        expand=True,
    )

def create_settings_input_field(page: ft.Page, text: str, page_parametr_str: str) -> ft.Column:
            input_field = ft.TextField(
                label=text,
                width=200,
                height=60,
                keyboard_type=ft.KeyboardType.NUMBER,
                input_filter=ft.InputFilter(regex_string=r"^\d*\.?\d*$"),
            )

            status_text = ft.Text(
                value=f"Current: {page.data[page_parametr_str]}%",
                color=ft.Colors.BLUE_400,
                weight=ft.FontWeight.W_500,
            )

            input_field.on_change = on_validate_input_field
            input_field.on_submit = lambda e: on_save_input_field(e, status_text, page_parametr_str)

            return ft.Column(
                controls=[
                    input_field,
                    status_text
                ],
                spacing=5,
                alignment=ft.MainAxisAlignment.START
            )

def create_toggle_theme_button() -> ft.IconButton:
    return ft.IconButton(
        icon = ft.Icons.BRIGHTNESS_6,
        tooltip = "Toggle Theme",
        on_click = on_toggle_theme,
    )

def create_skin_type_checkbox(text: str, is_on: bool = False) -> ft.Checkbox:
    return ft.Checkbox(
        label=text,
        value=is_on,
        label_style=ft.TextStyle(
            color=ft.Colors.WHITE,
            font_family="Montserrat",
            size=16,
        ),
        on_change=lambda e:on_skin_type_checkbox_change(e, text),
        active_color=ft.Colors.BLUE_600,
        check_color=ft.Colors.WHITE
    )
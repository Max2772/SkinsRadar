import flet as ft
from flet.core.alignment import center

from src.ui.handlers import reload_skins_table, start_parsing, clean_auto_table, pause_auto_parsing, restore_button_color

def create_settings_view(
    theme_button,
    commission_field,
    boost_field,
    proxy_button,
    wipe_proxy_button,
    update_skins_db_button,
    app_bar
) -> ft.View:
    return ft.View(
        route="/settings",
        controls=[
            app_bar,
            ft.Container(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ListTile(
                                    title=ft.Text("Commission Percentage", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Set the commission percentage for market calculations (0-100%).", size=14, color=ft.Colors.GREY_600),
                                    trailing=commission_field,
                                    content_padding=ft.padding.only(left=16, right=16, top=10, bottom=10)
                                ),
                                ft.ListTile(
                                    title=ft.Text("🗲 Max Boost Percentage", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Set the maximum boost percentage to filter boosted items (0-100%).",
                                                     size=14, color=ft.Colors.GREY_600),
                                    trailing=boost_field,
                                    content_padding=ft.padding.only(left=16, right=16, top=10, bottom=10)
                                ),
                                ft.ListTile(
                                    title=ft.Text("Update Proxies", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Refresh proxy list to improve connection reliability.",
                                                     size=14, color=ft.Colors.GREY_600),
                                    trailing=proxy_button,
                                    content_padding=ft.padding.only(left=16, right=16, top=10, bottom=10)
                                ),
                                ft.ListTile(
                                    title=ft.Text("Wipe Proxy", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Wipe all proxies from database.",
                                                     size=14, color=ft.Colors.GREY_600),
                                    trailing=wipe_proxy_button,
                                    content_padding=ft.padding.only(left=16, right=16, top=10, bottom=10)
                                ),
                                ft.ListTile(
                                    title=ft.Text("Update Skins Database", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Download the latest skins data for accurate listings.", size=14, color=ft.Colors.GREY_600),
                                    trailing=update_skins_db_button
                                ),
                                ft.ListTile(
                                    title=ft.Text("Toggle Theme", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Switch between light and dark theme for better visibility.", size=14, color=ft.Colors.GREY_600),
                                    trailing=theme_button
                                ),
                                ft.ListTile(
                                    title=ft.Text("Go Back", size=16, weight=ft.FontWeight.BOLD),
                                    subtitle=ft.Text("Return to the main screen.", size=14, color=ft.Colors.GREY_600),
                                    trailing=ft.ElevatedButton(
                                        text="Go Back",
                                        on_click=lambda e: e.page.go(e.page.data["previous_view"]),
                                        style=ft.ButtonStyle(bgcolor=ft.Colors.RED_600, color=ft.Colors.WHITE)
                                    )
                                ),
                            ],
                            spacing=20,
                        ),
                        padding=ft.padding.all(20),
                    ),
                    elevation=4,
                    margin=ft.margin.symmetric(horizontal=20, vertical=10),
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=20),
                width=600,
            ),
            ft.Container(
                content=ft.Text(
                    "Developed by Max2772, UterSt",
                    size=14,
                    color=ft.Colors.GREY_500,
                    text_align=center
                ),
                alignment=ft.alignment.bottom_center,
                padding=ft.padding.only(bottom=20)
            )
        ],
        scroll=ft.ScrollMode.AUTO,
        vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def create_skins_table_view(
        search_bar,
        search_bar_result,
        listings_amount_field,
        dropdown_exterior,
        dropdown_currency,
        table_container,
        app_bar
) -> ft.View:
    return ft.View(
        route="/skins_table",
        controls=[
            app_bar,
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                        "Steam Market Listings",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE_700,
                            font_family="Montserrat",
                        text_align=ft.TextAlign.CENTER,
                    ),
                        padding=ft.padding.only(bottom=10, top=30)
                    ),
                    ft.Column(
                        controls=[
                        search_bar,
                        search_bar_result,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Reload",
                                icon=ft.Icons.REFRESH,
                                icon_color=ft.Colors.BLUE_700,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.BLUE_700,
                                    shape=ft.RoundedRectangleBorder(radius=8)
                                ),
                                on_click=lambda e: e.page.run_task(
                                    reload_skins_table,
                                    e.page,
                                    e.page.data["fetch_data_callback"]
                                ),
                            ),
                            listings_amount_field,
                            dropdown_exterior,
                            dropdown_currency
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    table_container
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        spacing=26,
    )

def create_auto_table_view(
    profit_amount_field,
    sales_amount_field,
    souvenir_checkbox,
    stattrak_checkbox,
    knife_checkbox,
    boosted_checkbox,
    auto_table_container,
    app_bar
) -> ft.View:
    return ft.View(
        route="/auto_table",
        controls=[
            app_bar,
            ft.Container(
                content=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            "Radar Mode",
                                            size=32,
                                            weight=ft.FontWeight.BOLD,
                                            font_family="Montserrat",
                                            color=ft.Colors.WHITE,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                        ft.Text(
                                            "Automatically scan and track profitable skins on the Steam Market",
                                            size=16,
                                            color=ft.Colors.GREY_200,
                                            font_family="Montserrat",
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                ),
                                ft.Row(
                                    controls=[
                                        profit_amount_field,
                                        sales_amount_field,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                ),
                                ft.Row(
                                    controls=[
                                        souvenir_checkbox,
                                        stattrak_checkbox,
                                        knife_checkbox,
                                        boosted_checkbox
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            text="Start",
                                            icon=ft.Icons.PLAY_ARROW,
                                            icon_color=ft.Colors.BLUE_700,
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.BLUE_50,
                                                color=ft.Colors.BLUE_700,
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                            ),
                                            on_hover=lambda e: (
                                                setattr(e.control, "bgcolor",
                                                        ft.Colors.GREY_400 if e.data == "true" else ft.Colors.BLUE_50),
                                                e.control.update()
                                            ),
                                            on_click=lambda e: (
                                                setattr(e.control, "bgcolor", ft.Colors.GREY_500),
                                                e.page.update(),
                                                e.page.run_task(start_parsing, e.page),
                                                e.page.run_task(restore_button_color, e.control)
                                            ),
                                        ),
                                        ft.ElevatedButton(
                                            text="Pause",
                                            icon=ft.Icons.PAUSE,
                                            icon_color=ft.Colors.BLUE_700,
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.BLUE_50,
                                                color=ft.Colors.BLUE_700,
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                            ),
                                            on_hover=lambda e: (
                                                setattr(e.control, "bgcolor", ft.Colors.GREY_400 if e.data == "true" else ft.Colors.BLUE_50),
                                                e.control.update()
                                            ),
                                            on_click=lambda e: (
                                                setattr(e.control, "bgcolor", ft.Colors.GREY_500),
                                                e.page.update(),
                                                e.page.run_task(pause_auto_parsing, e.page),
                                                e.page.run_task(restore_button_color, e.control)
                                            ),
                                        ),
                                        ft.ElevatedButton(
                                            text="Clean",
                                            icon=ft.Icons.CLEAR,
                                            icon_color=ft.Colors.BLUE_700,
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.Colors.BLUE_50,
                                                color=ft.Colors.BLUE_700,
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                            ),
                                            on_hover=lambda e: (
                                                setattr(e.control, "bgcolor",
                                                        ft.Colors.GREY_400 if e.data == "true" else ft.Colors.BLUE_50),
                                                e.control.update()
                                            ),
                                            on_click=lambda e: (
                                                setattr(e.control, "bgcolor", ft.Colors.GREY_500),
                                                e.page.update(),
                                                e.page.run_task(clean_auto_table, e.page),
                                                e.page.run_task(restore_button_color, e.control)
                                            ),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=20,
                                ),
                            ],
                            spacing=20,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.all(20),
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=[
                                ft.Colors.BLUE_900,
                                ft.Colors.BLUE_700,
                                ft.Colors.BLUE_500,
                            ],
                            stops=[0.0, 0.5, 1.0],
                        ),
                        border_radius=10,
                    ),
                    elevation=4,
                    margin=ft.margin.symmetric(horizontal=20, vertical=10),
                ),
                alignment=ft.alignment.center,
                width=1000,
            ),
            auto_table_container,
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        padding=ft.padding.only(top=20),
    )
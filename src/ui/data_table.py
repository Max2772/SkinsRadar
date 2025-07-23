import flet as ft
from flet import DataTable, DataColumn, DataCell, Text, Row, Container, Image, TextButton, Colors
from flet.core.types import TextAlign
from src.utils import has_patches

async def create_skins_table_datatable(page: ft.Page, fetch_data_callback=None):
    if fetch_data_callback:
        page.data["data_skins_table"] = await fetch_data_callback(
            page.data["currency"],
            page.data["current_exterior"],
            page.data["amount_query"],
            page.data["current_skin"],
            page.data["steam_fee"]) or []

    if not page.data["data_skins_table"]:
        return None

    if not page.data["current_exterior"]:
        is_patches_skin = has_patches(page.data["data_skins_table"])
        if is_patches_skin:
            table_skins_with_patches = DataTable(
                columns=[
                    DataColumn(Text("Item Name", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER,),
                    DataColumn(Text("AB Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Profit", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Profit %", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Patches", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Link", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Item_Name ID", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            DataCell(
                                ft.Container(
                                    content=Text(
                                            value=row["skin_name"],
                                            color=ft.Colors.BLUE_700,
                                            tooltip=row["link"],
                                            weight=ft.FontWeight.BOLD,
                                    ),
                                    on_click=lambda e, url=row["link"]: page.launch_url(url),
                                    tooltip=row["link"],
                                    ink=True,
                                    border_radius=4,
                                ),
                            ),
                            DataCell(Text(f"{row['currency']}{row['autobuy_price']:.2f}")),
                            DataCell(Text(f"{row['currency']}{row['price']:.2f}")),
                            DataCell(Text(f"{row['currency']}{row['profit']:.2f}", color=Colors.RED_900 if row['profit'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                            DataCell(Text(f"{row['profit_percent']:.2f}%", color=Colors.RED_900 if row['profit_percent'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                            DataCell(
                                Row(
                                    controls=[
                                        Container(
                                            content=Image(
                                                src=url,
                                                width=32,
                                                height=32,
                                                fit=ft.ImageFit.CONTAIN,
                                                error_content=Text("X"),
                                                tooltip=title
                                            ),
                                            bgcolor=Colors.TRANSPARENT,
                                            border_radius=4,
                                            on_hover=lambda e: (
                                                setattr(e.control, "bgcolor", Colors.with_opacity(0.5, Colors.GREY_400) if e.data == "true" else Colors.TRANSPARENT),
                                                e.control.update()
                                            ),
                                            on_click=lambda e: page.launch_url(link)
                                        ) for url, title, link in zip(
                                            row.get("sticker_image_urls", []),
                                            row.get("sticker_titles", []),
                                            row.get("sticker_urls", [])
                                        )
                                    ],
                                    spacing=4
                                ) if row.get("sticker_image_urls") else Row(controls=[])
                            ),
                            DataCell(
                                TextButton(
                                    text="Inspect",
                                    on_click=lambda e, url=row["inspect_link"]: page.launch_url(url),
                                    tooltip=row["inspect_link"],
                                )
                            ),
                            DataCell(Text(row["item_nameid"]))
                        ],
                    ) for row in page.data["data_skins_table"]  or []
                ],
                border=ft.border.all(1, Colors.GREY_400),
                heading_row_color=Colors.BLUE_600,
            )
            return table_skins_with_patches
        else:
            table_no_patches = DataTable(
                columns=[
                    DataColumn(Text("Item Name", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER,),
                    DataColumn(Text("AB Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Profit", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Profit %", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                    DataColumn(Text("Item_Name ID", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            DataCell(
                                ft.Container(
                                    content=Text(
                                            value=row["skin_name"],
                                            color=ft.Colors.BLUE_700,
                                            tooltip=row["link"],
                                            weight=ft.FontWeight.BOLD,
                                    ),
                                    on_click=lambda e, url=row["link"]: page.launch_url(url),
                                    tooltip=row["link"],
                                    ink=True,
                                    border_radius=4,
                                ),
                            ),
                            DataCell(Text(f"{row['currency']}{row['autobuy_price']:.2f}")),
                            DataCell(Text(f"{row['currency']}{row['price']:.2f}")),
                            DataCell(Text(f"{row['currency']}{row['profit']:.2f}", color=Colors.RED_900 if row['profit'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                            DataCell(Text(f"{row['profit_percent']:.2f}%", color=Colors.RED_900 if row['profit_percent'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                            DataCell(Text(row["item_nameid"]))
                        ],
                    ) for row in page.data["data_skins_table"]  or []
                ],
                border=ft.border.all(1, Colors.GREY_400),
                heading_row_color=Colors.BLUE_600,
            )
            return table_no_patches

    else:
        table_weapons = DataTable(
            columns=[
                DataColumn(Text("Skin Name", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER,),
                DataColumn(Text("Exterior", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("AB Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Profit", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Profit %", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Stickers", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Charms", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Link", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Item_Name ID", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        DataCell(
                            ft.Container(
                                content=Text(
                                        value=row["skin_name"],
                                        color=ft.Colors.BLUE_700,
                                        tooltip=row["link"],
                                        weight=ft.FontWeight.BOLD,
                                ),
                                on_click=lambda e, url=row["link"]: page.launch_url(url),
                                tooltip=row["link"],
                                ink=True,
                                border_radius=4,
                            ),
                        ),
                        DataCell(Text(row["exterior"].replace("Exterior: ", ""))),
                        DataCell(Text(f"{row['currency']}{row['autobuy_price']:.2f}")),
                        DataCell(Text(f"{row['currency']}{row['price']:.2f}")),
                        DataCell(Text(f"{row['currency']}{row['profit']:.2f}", color=Colors.RED_900 if row['profit'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                        DataCell(Text(f"{row['profit_percent']:.2f}%", color=Colors.RED_900 if row['profit_percent'] < 0 else Colors.GREEN_900, weight=ft.FontWeight.BOLD)),
                        DataCell(
                            Row(
                                controls=[
                                    Container(
                                        content=Image(
                                            src=url,
                                            width=32,
                                            height=32,
                                            fit=ft.ImageFit.CONTAIN,
                                            error_content=Text("X"),
                                            tooltip=title
                                        ),
                                        bgcolor=Colors.TRANSPARENT,
                                        border_radius=4,
                                        on_hover=lambda e: (
                                            setattr(e.control, "bgcolor", Colors.with_opacity(0.5, Colors.GREY_400) if e.data == "true" else Colors.TRANSPARENT),
                                            e.control.update()
                                        ),
                                        on_click=lambda e: page.launch_url(link)
                                    ) for url, title, link in zip(
                                        row.get("sticker_image_urls", []),
                                        row.get("sticker_titles", []),
                                        row.get("sticker_urls", [])
                                    )
                                ],
                                spacing=4
                            ) if row.get("sticker_image_urls") else Row(controls=[])
                        ),
                        DataCell(
                            Container(
                                content=Image(
                                    src=row["keychain_image_url"],
                                    width=32,
                                    height=32,
                                    fit=ft.ImageFit.CONTAIN,
                                    error_content=Text("X"),
                                    tooltip=row["keychain_title"]
                                ),
                                bgcolor=Colors.TRANSPARENT,
                                border_radius=4,
                                on_hover=lambda e: (
                                    setattr(e.control, "bgcolor", Colors.with_opacity(0.5, Colors.GREY_400) if e.data == "true" else Colors.TRANSPARENT),
                                    e.control.update()
                                ),
                                on_click=lambda e, url=row["keychain_url"]: page.launch_url(url)
                            ) if row.get("keychain_image_url") else Container()
                        ),
                        DataCell(
                            TextButton(
                                text="Inspect",
                                on_click=lambda e, url=row["inspect_link"]: page.launch_url(url),
                                tooltip=row["inspect_link"],
                            )
                        ),
                        DataCell(Text(row["item_nameid"]))
                    ],
                ) for row in page.data["data_skins_table"]  or []
            ],
            border=ft.border.all(1, Colors.GREY_400),
            heading_row_color=Colors.BLUE_600,
        )
        return table_weapons

async def create_auto_table_datatable(page: ft.Page, fetch_data_callback, souvenir = False, stattrak = False, knife = False, skip_boosted = False, return_rows_only = False):
    if fetch_data_callback and return_rows_only:
        page.data["new_data_auto_table"] = await fetch_data_callback(
            page.data["currency"],
            page.data["current_exterior"],
            page.data["amount_query"],
            page.data["current_skin"],
            page.data["steam_fee"],
            page.data["amount_profit"],
            page.data["amount_sales"], souvenir, stattrak, knife, skip_boosted, page.data["max_boost"], "RANDOM") or []

    if return_rows_only:
        if page.data["new_data_auto_table"] == -1 or page.data["new_data_auto_table"] == -2:
            return page.data["new_data_auto_table"]
        if not page.data["new_data_auto_table"]:
            return None

        row = page.data["new_data_auto_table"]
        return ft.DataRow(
                cells=[
                    DataCell(
                        ft.Container(
                            content=Text(
                                value=row["skin_name"],
                                color=ft.Colors.BLUE_700,
                                tooltip=row["link"],
                                weight=ft.FontWeight.BOLD,
                            ),
                            on_click=lambda e, url=row["link"]: page.launch_url(url),
                            tooltip=row["link"],
                            ink=True,
                                border_radius=4,
                        ),
                    ),
                    DataCell(Text(row["exterior"])),
                    DataCell(Text(f"$ {row['autobuy_price']:.2f}")),
                    DataCell(Text(f"$ {row['price']:.2f}")),
                    DataCell(
                        Text(f"$ {row['profit']:.2f}", color=Colors.RED_900 if row['profit'] < 0 else Colors.GREEN_900,
                             weight=ft.FontWeight.BOLD)),
                    DataCell(Text(f"{row['profit_percent']:.2f}%",
                                  color=Colors.RED_900 if row['profit_percent'] < 0 else Colors.GREEN_900,
                                  weight=ft.FontWeight.BOLD)),
                    DataCell(Text(row["total_sales_month"], text_align=TextAlign.CENTER)),
                    DataCell(Text(row["item_nameid"]))
                ],
            )
    else:
        table = DataTable(
            columns=[
                DataColumn(Text("Skin Name", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER,),
                DataColumn(Text("Exterior", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("AB Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Price", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Profit", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Profit %", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Sales (Month)", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
                DataColumn(Text("Item_Name ID", weight=ft.FontWeight.BOLD), heading_row_alignment=ft.MainAxisAlignment.CENTER),
            ],
            rows=[],
            border=ft.border.all(1, Colors.GREY_400),
            heading_row_color=Colors.BLUE_600,
        )
        return table
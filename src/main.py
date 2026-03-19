import flet as ft
from ui.home import home_view


def main(page: ft.Page):
    page.add(home_view())


ft.run(main)

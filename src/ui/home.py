import flet as ft
from dataclasses import dataclass, field

from converters.image import convert_image


@dataclass
class State:
    picked_files: list[ft.FilePickerFile] = field(default_factory=list)


state = State()


def home_view() -> ft.Control:
    file_list = ft.Column()

    format_dropdown = ft.Dropdown(
        editable=True,
        label="フォーマット選択",
        options=[
            ft.dropdown.Option("PNG"),
            ft.dropdown.Option("JPEG"),
            ft.dropdown.Option("WEBP"),
        ],
        value="PNG"
    )

    async def handle_pick(e):
        files = await ft.FilePicker().pick_files(
            allow_multiple=True,
            file_type=ft.FilePickerFileType.IMAGE
        )
        if files:
            state.picked_files = files
            file_list.controls.clear()
            for f in files:
                file_list.controls.append(ft.Text(f.name))
            file_list.update()

    def handle_convert(e):
        for f in state.picked_files:
            convert_image(f.path, format_dropdown.value)

    return ft.Column([
        ft.ElevatedButton("ファイルを選択", on_click=handle_pick),
        file_list,
        format_dropdown,
        ft.ElevatedButton("変換する", on_click=handle_convert)
    ])

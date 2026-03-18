import flet as ft
from dataclasses import dataclass, field


@dataclass
class State:
    picked_files: list[ft.FilePickerFile] = field(default_factory=list)


state = State()


def home_view() -> ft.Control:
    file_list = ft.Column()

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
    return ft.Column([
        ft.ElevatedButton("ファイルを選択", on_click=handle_pick),
        file_list
    ])

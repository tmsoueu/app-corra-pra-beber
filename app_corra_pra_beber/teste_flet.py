import flet as ft

def main(page: ft.Page):
    def ao_montar(e):
        page.window_width = 390
        page.window_height = 800
        page.window_resizable = False
        page.window_maximizable = False
        page.window_minimizable = True
        page.update()
    page.on_mount = ao_montar
    page.add(ft.Text("Teste de redimensionamento"))

ft.app(target=main, view=ft.AppView.FLET_APP, port=4444)
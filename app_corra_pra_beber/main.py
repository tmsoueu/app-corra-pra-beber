import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("Olá, Mundo com Flet!", size=30, color=ft.Colors.BLUE_500), # CORRIGIDO AQUI
        ft.ElevatedButton("Clique-me!", on_click=lambda e: page.add(ft.Text("Botão Clicado!")))
    )

if __name__ == "__main__":
    ft.app(target=main)
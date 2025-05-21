import flet as ft
from views.home_view import HomeView
import asyncio
import platform

async def main(page: ft.Page):
    # Ajusta o tamanho da janela para simular um dispositivo mobile (apenas em desktop)
    if platform.system() in ("Windows", "Darwin", "Linux"):
        page.window.width = 390  # largura típica de celular em px
        page.window.height = 800  # altura típica de celular em px
        page.window.resizable = False  # impede redimensionamento manual
        page.window.maximizable = False  # impede maximizar
        page.window.minimizable = True  # permite minimizar

    # Define o tema escuro para toda a aplicação
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    
    # Função para exibir a tela de splash (carregamento) com o logo centralizado
    def mostrar_splash():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/splash",
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="assets/logo.png",
                            width=180,
                            height=180,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        alignment=ft.alignment.center,
                        expand=True
                    ),
                    ft.Text(
                        "Carregando...",
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLUE_300
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        page.update()

    # Exibe a splash screen e aguarda 2 segundos antes de ir para a tela principal
    mostrar_splash()
    await asyncio.sleep(2)
    page.go("/")

    # Função de navegação entre as rotas/views do app
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            # View principal (Home)
            page.views.append(HomeView(page))
        elif page.route == "/counter":
            # View do contador, responsiva e centralizada
            page.views.append(
                ft.View(
                    route="/counter",
                    controls=[
                        ft.AppBar(title=ft.Text("Tela do Contador")),
                        ft.Container(
                            content=ft.ResponsiveRow([
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Esta é a tela do contador!",
                                            size=24,
                                            weight=ft.FontWeight.BOLD,
                                            text_align=ft.TextAlign.CENTER
                                        ),
                                        ft.ElevatedButton(
                                            "Voltar para Home",
                                            on_click=lambda e: page.go("/"),
                                            expand=True
                                        )
                                    ],
                                    col={"xs": 12, "sm": 10, "md": 8, "lg": 6},
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]),
                            padding=20,
                            alignment=ft.alignment.center,
                            expand=True
                        )
                    ]
                )
            )
        page.update()

    # Define a função de navegação para mudanças de rota
    page.on_route_change = route_change

# Ponto de entrada da aplicação Flet
if __name__ == "__main__":
    ft.app(target=main)

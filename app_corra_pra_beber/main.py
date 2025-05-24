"""
Módulo principal da aplicação Corra Pra Beber.
Este módulo configura e inicializa a aplicação Flet, definindo o layout
e a navegação entre as diferentes telas.
"""

import asyncio
import platform
from typing import Callable

import flet as ft
from views.home_view import HomeView
from views.login_view import LoginView

# Constantes da aplicação
LARGURA_MOBILE = 390
ALTURA_MOBILE = 800
TEMPO_SPLASH = 2  # segundos

def mostrar_splash(page: ft.Page) -> None:
    """
    Exibe a tela de splash (carregamento) com o logo centralizado.
    
    Args:
        page: Instância da página Flet
    """
    page.views.clear()
    page.views.append(
        ft.View(
            route='/splash',
            controls=[
                ft.Container(
                    content=ft.Image(
                        src='assets/logo.png',
                        width=180,
                        height=180,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ),
                ft.Text(
                    'Carregando...',
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

def route_change(page: ft.Page, route: str) -> None:
    """
    Gerencia a navegação entre as diferentes rotas/views do app.
    
    Args:
        page: Instância da página Flet
        route: Rota atual da aplicação
    """
    page.views.clear()
    
    if page.route == '/':
        # View principal (Home)
        page.views.append(HomeView(page))
    elif page.route == '/counter':
        # View do contador, responsiva e centralizada
        page.views.append(
            ft.View(
                route='/counter',
                controls=[
                    ft.AppBar(title=ft.Text('Tela do Contador')),
                    ft.Container(
                        content=ft.ResponsiveRow([
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        'Esta é a tela do contador!',
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    ft.ElevatedButton(
                                        'Voltar para Home',
                                        on_click=lambda e: page.go('/'),
                                        expand=True
                                    )
                                ],
                                col={'xs': 12, 'sm': 10, 'md': 8, 'lg': 6},
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
    elif page.route == '/login':
        # View de login
        page.views.append(LoginView(page))
    
    page.update()

async def main(page: ft.Page) -> None:
    """
    Função principal que configura e inicializa a aplicação.
    
    Args:
        page: Instância da página Flet
    """
    # Ajusta o tamanho da janela para simular um dispositivo mobile (apenas em desktop)
    if platform.system() in ('Windows', 'Darwin', 'Linux'):
        page.window.width = LARGURA_MOBILE
        page.window.height = ALTURA_MOBILE
        page.window.resizable = False
        page.window.maximizable = False
        page.window.minimizable = True

    # Define o tema escuro para toda a aplicação
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    
    # Exibe a splash screen e aguarda antes de ir para a tela de login
    mostrar_splash(page)
    await asyncio.sleep(TEMPO_SPLASH)
    page.go('/login')

    # Define a função de navegação para mudanças de rota
    page.on_route_change = lambda e: route_change(page, e.route)

if __name__ == '__main__':
    ft.app(target=main)

"""
Módulo que implementa a view do contador.
Esta view exibe uma tela de contador com botão para voltar à home.
"""

import flet as ft

class CounterView(ft.View):
    """
    View do contador responsiva e centralizada.
    
    Args:
        page: Instância da página Flet
    """
    
    def __init__(self, page: ft.Page):
        super().__init__(
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
import flet as ft

class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",  # Define a rota para esta view (ex: tela inicial)
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Container centralizado e responsivo para mobile
                ft.Container(
                    content=ft.ResponsiveRow([
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "Olá, Mundo com Flet!",
                                    size=30,
                                    color=ft.Colors.BLUE_500,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                ft.ElevatedButton(
                                    "Clique-me!",
                                    on_click=lambda e: page.add(ft.Text("Botão Clicado!")),
                                    expand=True
                                ),
                                ft.ElevatedButton(
                                    "Ir para o contador",
                                    on_click=lambda e: page.go("/counter"),
                                    expand=True
                                )
                            ],
                            col={"xs": 12, "sm": 8, "md": 6},  # Ocupa toda a largura no mobile, menos em telas maiores
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]),
                    padding=20,
                    alignment=ft.alignment.center,
                    expand=True,
                    width=400,  # Largura máxima para não ficar exagerado em telas grandes
                )
            ]
        )
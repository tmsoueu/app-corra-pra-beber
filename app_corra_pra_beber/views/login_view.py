import flet as ft

# Cores base da paleta (adaptadas para tema escuro)
LARANJA_VIBRANTE = ft.Colors.ORANGE_ACCENT_400  # Ajuste para melhor visibilidade em fundo escuro
DOURADO_AMBAR = ft.Colors.AMBER_ACCENT_400     # Ajuste para melhor visibilidade em fundo escuro
BRANCO_CREME = ft.Colors.WHITE
CINZA_CLARO = ft.Colors.BLUE_GREY_50
# CINZA_ESCURO_FUNDO = ft.Colors.BLUE_GREY_900 # Removido o fundo escuro da View principal
# CINZA_ESCURO_CARD = ft.Colors.BLUE_GREY_800 # Removido o fundo escuro do card
# Cor laranja original fornecida pelo usuário, não mais usada para fundo de card:
# LARANJA_FUNDO_CARD = "#eb7b13"

class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/login",  # Define a rota para esta view
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # bgcolor=CINZA_ESCURO_FUNDO, # Removido o fundo escuro da View
            # O fundo da View agora será o tema padrão (escuro ou claro)
            controls=[
                # Coluna principal centralizada vertical e horizontalmente
                ft.Column(
                    controls=[
                        # Logo (imagem) - Centralizado automaticamente pela coluna principal
                        ft.Image(
                            src="assets/logo.png",
                            width=150,
                            height=150,
                            fit=ft.ImageFit.CONTAIN,
                            # Adicionar um leve brilho ou ajuste para visibilidade em fundo escuro, se necessário
                        ),
                        # Container para textos e botão, com largura máxima para mobile
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    # Título principal
                                    ft.Text(
                                        "Corra pra Beber",
                                        size=40,
                                        weight=ft.FontWeight.BOLD,
                                        color=LARANJA_VIBRANTE,  # Usando a cor ajustada para fundo escuro
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    # Subtítulo
                                    ft.Text(
                                        "Pronto pra correr e beber?",
                                        size=18,
                                        color=DOURADO_AMBAR,  # Usando a cor ajustada para fundo escuro
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    # Botão Continuar com Google
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [ft.Image(src='https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg', width=24, height=24),
                                                 ft.Text("Continuar com Google", size=16)
                                                ],
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            on_click=lambda e: print("Botão Google Clicado!"),  # Placeholder para a lógica de login
                                            bgcolor=BRANCO_CREME,  # Mantido branco padrão para o botão Google
                                            color=ft.Colors.BLACK87,  # Cor do texto no botão branco
                                            # style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                            elevation=2,
                                            expand=True # O botão se expande dentro do Container menor
                                        ),
                                        margin=ft.margin.only(top=20),
                                        width=300 # Limita a largura máxima do container interno (e do botão)
                                    )
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=15,
                            ),
                            padding=ft.padding.all(20), # Padding interno para os elementos
                            alignment=ft.alignment.center, # Centraliza o conteúdo dentro deste container
                            # Sem largura fixa aqui para o Container externo (agora removido)
                            # O Container interno abaixo controla a largura dos textos/botão
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, # Centraliza a coluna principal
                    spacing=25, # Espaçamento entre o logo e o container de textos/botão
                )
            ]
        ) 
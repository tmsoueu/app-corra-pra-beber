"""
Módulo que implementa a view de login da aplicação.
Esta view exibe a tela inicial com logo, título e botão de login com Google.
"""

import flet as ft
import webbrowser
import os
import subprocess
from utils.auth_google import auth_manager

# Constantes de cores
LARANJA_VIBRANTE = ft.Colors.ORANGE_ACCENT_400
DOURADO_AMBAR = ft.Colors.AMBER_ACCENT_400
BRANCO_CREME = ft.Colors.WHITE
CINZA_CLARO = ft.Colors.BLUE_GREY_50

# Constantes de fonte
FONTE_TITULO = 'Roboto Condensed'

# Constantes de dimensões
LARGURA_LOGO = 150
ALTURA_LOGO = 150
LARGURA_MAXIMA_BOTAO = 300
TAMANHO_TITULO = 40
TAMANHO_SUBTITULO = 18
TAMANHO_TEXTO_BOTAO = 16

class LoginView(ft.View):
    """
    View de login responsiva e centralizada.
    
    Args:
        page: Instância da página Flet
    """
    
    def __init__(self, page: ft.Page):
        self.page = page
        
        # Carrega a fonte do Google Fonts
        page.fonts = {
            FONTE_TITULO: 'https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=swap'
        }
        
        super().__init__(
            route='/login',
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        # Logo
                        ft.Image(
                            src='assets/logo.png',
                            width=LARGURA_LOGO,
                            height=ALTURA_LOGO,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        # Container para textos e botão
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    # Título principal
                                    ft.Text(
                                        'Corra pra Beber',
                                        size=TAMANHO_TITULO,
                                        weight=ft.FontWeight.BOLD,
                                        color=LARANJA_VIBRANTE,
                                        text_align=ft.TextAlign.CENTER,
                                        font_family=FONTE_TITULO
                                    ),
                                    # Subtítulo
                                    ft.Text(
                                        'Pronto pra correr e beber?',
                                        size=TAMANHO_SUBTITULO,
                                        color=LARANJA_VIBRANTE,
                                        text_align=ft.TextAlign.CENTER
                                    ),
                                    # Botão Continuar com Google
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Image(
                                                        src='https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg',
                                                        width=24,
                                                        height=24
                                                    ),
                                                    ft.Text(
                                                        'Continuar com Google',
                                                        size=TAMANHO_TEXTO_BOTAO
                                                    )
                                                ],
                                                height=50,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                            ),
                                            on_click=self.login_google,
                                            bgcolor=BRANCO_CREME,
                                            color=ft.Colors.BLACK87,
                                            elevation=2,
                                            expand=True
                                        ),
                                        margin=ft.margin.only(top=30),
                                        width=LARGURA_MAXIMA_BOTAO,
                                        padding=ft.padding.symmetric(vertical=20)
                                    )
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=1,
                            ),
                            padding=ft.padding.all(20),
                            alignment=ft.alignment.center,
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=25,
                )
            ]
        )
    
    def login_google(self, e):
        """
        Inicia o processo de login com Google.
        
        Args:
            e: Evento do clique no botão
        """
        try:
            # Inicia o fluxo de autenticação
            auth_url = auth_manager.iniciar_login()
            print(f'URL de autenticação gerada: {auth_url}')
            
            # Tenta abrir o navegador de diferentes formas
            try:
                # Primeiro tenta usar o webbrowser padrão
                webbrowser.open(auth_url)
            except Exception as e1:
                print(f'Erro ao abrir navegador com webbrowser: {e1}')
                try:
                    # Se falhar, tenta abrir com o comando start (Windows)
                    if os.name == 'nt':
                        os.startfile(auth_url)
                    else:
                        # Para Linux/Mac
                        subprocess.call(['xdg-open', auth_url])
                except Exception as e2:
                    print(f'Erro ao abrir navegador com os.startfile/subprocess: {e2}')
                    # Se tudo falhar, mostra a URL para o usuário copiar
                    self.page.snack_bar = ft.SnackBar(
                        content=ft.Text('Não foi possível abrir o navegador automaticamente. Por favor, copie e cole esta URL no seu navegador:'),
                        bgcolor=ft.colors.ORANGE
                    )
                    self.page.snack_bar.open = True
                    self.page.update()
            
            # Exibe diálogo para colar a URL de redirecionamento
            self.page.dialog = ft.AlertDialog(
                title=ft.Text('Autenticação Google'),
                content=ft.Text('Após fazer login, cole a URL para a qual você foi redirecionado:'),
                actions=[
                    ft.TextField(
                        label='URL de Redirecionamento',
                        multiline=True,
                        min_lines=1,
                        max_lines=3,
                        on_submit=self.processar_login
                    ),
                    ft.ElevatedButton(
                        'Confirmar',
                        on_click=self.processar_login
                    )
                ],
                actions_alignment=ft.MainAxisAlignment.END
            )
            self.page.dialog.open = True
            self.page.update()
            
        except Exception as e:
            print(f'Erro ao iniciar login: {e}')
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text('Erro ao iniciar o processo de login. Tente novamente.'),
                bgcolor=ft.colors.RED
            )
            self.page.snack_bar.open = True
            self.page.update()
    
    def processar_login(self, e):
        """
        Processa a URL de redirecionamento após autenticação.
        
        Args:
            e: Evento do botão ou campo de texto
        """
        # Obtém a URL do campo de texto
        url = e.control.value if isinstance(e.control, ft.TextField) else e.control.parent.controls[0].value
        
        # Processa o redirecionamento
        user_data = auth_manager.processar_redirecionamento(url)
        
        # Fecha o diálogo
        self.page.dialog.open = False
        
        if user_data:
            # Redireciona para a página principal
            self.page.go('/')
        else:
            # Exibe mensagem de erro
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text('Erro ao fazer login. Tente novamente.'),
                bgcolor=ft.colors.RED
            )
            self.page.snack_bar.open = True
        
        self.page.update() 
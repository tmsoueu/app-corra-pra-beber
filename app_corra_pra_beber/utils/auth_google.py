"""
Módulo de autenticação com Google OAuth2.
Implementa o fluxo de autenticação e gerenciamento de sessão do usuário.
"""

import os
import webbrowser
from typing import Optional, Dict, Any
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from pathlib import Path

# Carrega variáveis do .env localizado em storage/data/.env
ENV_PATH = Path(__file__).parent.parent / 'storage' / 'data' / '.env'
load_dotenv(dotenv_path=ENV_PATH)

CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')

# Escopos necessários para obter informações básicas do usuário
SCOPE = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

# Endpoints do Google
AUTHORIZATION_BASE_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
USER_INFO_URL = 'https://www.googleapis.com/oauth2/v1/userinfo'

class GoogleAuth:
    """
    Classe para gerenciar a autenticação com Google OAuth2.
    """
    
    def __init__(self):
        self.oauth: Optional[OAuth2Session] = None
        self.user_data: Optional[Dict[str, Any]] = None
        self._state = None
    
    def iniciar_login(self) -> str:
        """
        Inicia o fluxo de autenticação e retorna a URL de autorização.
        
        Returns:
            str: URL de autorização do Google
        """
        self.oauth = OAuth2Session(
            CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )
        
        authorization_url, self._state = self.oauth.authorization_url(
            AUTHORIZATION_BASE_URL,
            access_type='offline',
            prompt='select_account'
        )
        
        return authorization_url
    
    def processar_redirecionamento(self, redirect_response: str) -> Optional[Dict[str, Any]]:
        """
        Processa a resposta do redirecionamento após autenticação.
        
        Args:
            redirect_response: URL de redirecionamento após autenticação
            
        Returns:
            Optional[Dict[str, Any]]: Dados do usuário ou None em caso de erro
        """
        if not self.oauth:
            return None
            
        try:
            token = self.oauth.fetch_token(
                TOKEN_URL,
                authorization_response=redirect_response,
                client_secret=CLIENT_SECRET
            )
            
            # Buscar dados do usuário
            resp = self.oauth.get(USER_INFO_URL)
            userinfo = resp.json()
            
            self.user_data = {
                'id': userinfo.get('id'),
                'nome': userinfo.get('name'),
                'email': userinfo.get('email'),
                'foto': userinfo.get('picture')
            }
            
            return self.user_data
            
        except HTTPError as e:
            print('Erro ao autenticar com o Google:', e)
            return None
    
    def obter_usuario_atual(self) -> Optional[Dict[str, Any]]:
        """
        Retorna os dados do usuário atualmente autenticado.
        
        Returns:
            Optional[Dict[str, Any]]: Dados do usuário ou None se não autenticado
        """
        return self.user_data
    
    def logout(self) -> None:
        """
        Realiza o logout do usuário, limpando os dados da sessão.
        """
        self.oauth = None
        self.user_data = None
        self._state = None

# Instância global do gerenciador de autenticação
auth_manager = GoogleAuth() 
import os
import webbrowser
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


def login_google():
    """
    Inicia o fluxo OAuth2 do Google, abre o navegador para o usuário autenticar,
    recebe o token e retorna os dados do usuário Google (id, nome, email, foto).
    """
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL, access_type='offline', prompt='select_account')

    print('Abrindo navegador para autenticação Google...')
    webbrowser.open(authorization_url)
    print(f'Caso não abra automaticamente, acesse: {authorization_url}')

    # Usuário deve colar a URL de redirecionamento após login
    redirect_response = input('Cole aqui a URL para a qual você foi redirecionado após login: ')

    try:
        token = oauth.fetch_token(
            TOKEN_URL,
            authorization_response=redirect_response,
            client_secret=CLIENT_SECRET
        )
        # Buscar dados do usuário
        resp = oauth.get(USER_INFO_URL)
        userinfo = resp.json()
        return {
            'id': userinfo.get('id'),
            'nome': userinfo.get('name'),
            'email': userinfo.get('email'),
            'foto': userinfo.get('picture')
        }
    except HTTPError as e:
        print('Erro ao autenticar com o Google:', e)
        return None 
import sqlite3
from pathlib import Path

# Caminho do arquivo do banco de dados local
CAMINHO_BANCO = Path(__file__).parent.parent / 'dados.db'

# Função para conectar ao banco de dados
# Sempre usar 'with conectar_banco() as conn:' para garantir fechamento correto

def conectar_banco():
    return sqlite3.connect(CAMINHO_BANCO)

# Função para criar a tabela de usuários, se não existir
# Executar no início da aplicação

def criar_tabela_usuarios():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')
        conn.commit()

# Função para inserir um novo usuário
# Retorna True se inserido com sucesso, False se email já existe

def inserir_usuario(nome, email, senha):
    try:
        with conectar_banco() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Função para buscar usuário por email e senha (login)
# Retorna o dicionário do usuário se encontrado, ou None

def buscar_usuario(email, senha):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, email FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'nome': row[1], 'email': row[2]}
        return None

# Função para buscar usuário por email (para verificar existência)

def usuario_existe(email):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM usuarios WHERE email = ?', (email,))
        return cursor.fetchone() is not None

# Função para criar a tabela de usuários Google, se não existir
# Executar no início da aplicação

def criar_tabela_usuarios_google():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios_google (
                id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                foto TEXT
            )
        ''')
        conn.commit()

# Função para inserir ou atualizar usuário Google
# Se o usuário já existe, atualiza nome, email e foto

def inserir_ou_atualizar_usuario_google(id_google, nome, email, foto):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios_google (id, nome, email, foto)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                nome=excluded.nome,
                email=excluded.email,
                foto=excluded.foto
        ''', (id_google, nome, email, foto))
        conn.commit()

# Função para buscar usuário Google por id
# Retorna dicionário do usuário ou None

def buscar_usuario_google_por_id(id_google):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, email, foto FROM usuarios_google WHERE id = ?', (id_google,))
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'nome': row[1], 'email': row[2], 'foto': row[3]}
        return None

# Função para buscar usuário Google por email
# Retorna dicionário do usuário ou None

def buscar_usuario_google_por_email(email):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, email, foto FROM usuarios_google WHERE email = ?', (email,))
        row = cursor.fetchone()
        if row:
            return {'id': row[0], 'nome': row[1], 'email': row[2], 'foto': row[3]}
        return None 
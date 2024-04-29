import os
import platform
import time
import json

lista_de_contas = []

login_gerente_var = 'Bill01'
password_gerente = 'abc123'


def limpar_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def limpar_terminal_mensagem(texto: str, tempo: int):
    limpar_terminal()
    print(texto)
    time.sleep(tempo)
    limpar_terminal()


def criar_ou_pegar_lista():
    path = './listas_de_contas.json'

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def login_gerente():
    limpar_terminal_mensagem('Aguarde...', 1)
    print('Digite seu login de gerente:')
    login = input()

    limpar_terminal_mensagem('', 1)
    print('Digite sua ssenha de gerente:')
    password = input()

    if login == login_gerente_var and password == password_gerente:
        return (True, 'Login realizado com sucesso!')
    else:
        return (False, 'Senha ou Login invalidos!')

import os
import platform
import time
import random
import json
from datetime import datetime


def pegar_lista_de_contas():
    path = './lista_de_contas.json'

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        with open(path, "w", encoding="utf-8") as f:
            return json.dump([], f, ensure_ascii=False, indent=2)


def buscar_por_conta(conta):
    lista = pegar_lista_de_contas()
    for item in lista:
        if item["numero_conta"] == conta:
            return True
    return False


def buscar_por_cpf(cpf):
    lista = pegar_lista_de_contas()
    for item in lista:
        if item["cpf"] == cpf:
            return True
    return False


def gerar_numero_da_conta():
    numero_conta = ''
    while True:
        numero_conta = ''.join(str(random.randint(0, 9)) for _ in range(5))
        exist_conta = buscar_por_conta(numero_conta)
        if exist_conta:
            continue
        else:
            break
    return numero_conta


def criar_nova_conta():
    limpar_terminal_mensagem('', 0.5)
    print('Digite o nome do novo Cliente:')
    nome = input()
    limpar_terminal_mensagem('', 0.5)
    print('Digite o cpf do novo Cliente:')
    cpf = input()

    data_atual = formatar_data()
    numero_conta = gerar_numero_da_conta()

    exist_cpf = buscar_por_cpf(cpf)

    if exist_cpf:
        return (False, 'CPF já existente!')
    else:
        return (True, {
            'name': nome,
            'cpf': cpf,
            'data': data_atual,
            'numero_conta': numero_conta
        })


def formatar_data():
    agora = datetime.now()
    data_formatada = agora.strftime("%Y-%m-%d / %H:%M:%S")
    return data_formatada


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

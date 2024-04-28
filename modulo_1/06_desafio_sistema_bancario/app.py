import uuid
import platform
import os
import time
import locale
from datetime import datetime

uuid4 = uuid.uuid4
sistema_operacional = platform.system()


menu = """
[d] Depositar;
[s] Sacar;
[e] Extrado;
[q] Sair.

Escolha a opção desejada
"""

saldo = 0.0
LIMITE_DE_VALOR_POR_SAQUE = 500
extrato = []
numero_de_saques_diarios = 0
NUMERO_MAXIMO_DE_SAQUES_DIARIOS = 3


def limpar_terminal():
    if sistema_operacional == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def formatar_data():
    agora = datetime.now()
    data_formatada = agora.strftime("%Y-%m-%d / %H:%M:%S")
    return data_formatada


def formatar_valor(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor_formatado = locale.currency(valor, grouping=True)
    return valor_formatado


def criar_transacao(operacao, valor):
    if operacao == 'd':
        return {
            'id': uuid.uuid4(),
            'data': formatar_data(),
            'operação': 'Deposito',
            'valor': formatar_valor(valor)
        }
    elif operacao == 's':
        return {
            'id': uuid(),
            'data': formatar_data(),
            'operação': 'Deposito',
            'valor': formatar_valor(valor)
        }
    else:
        print('Operação Inexistente')


def pegar_valor():
    try:
        print('Digite o valor:')
        valor = float(input())
        return valor
    except Exception as e:
        limpar_terminal()
        print('Digite apenas números')
        print(e)
        limpar_terminal()
        return e


def deposito(valor: float):
    if valor > 0:
        global saldo
        saldo += valor
        transacao = criar_transacao('d', valor)
        extrato.append(transacao)
        return True
    else:
        return False


def saque(valor):
    global saldo
    global numero_de_saques_diarios
    if saldo <= 0 or saldo < valor:
        limpar_terminal()
        print('Você não tem saldo suficiente!')
        time.sleep(3)
        limpar_terminal()
        return False
    if valor > LIMITE_DE_VALOR_POR_SAQUE:
        limpar_terminal()
        print(f'Seu Limite de saque por operação é de {
              formatar_valor(LIMITE_DE_VALOR_POR_SAQUE)}!')
        time.sleep(3)
        limpar_terminal()
        return False
    if numero_de_saques_diarios >= NUMERO_MAXIMO_DE_SAQUES_DIARIOS:
        limpar_terminal()
        print(f'Você atingiu seu limite de {
              NUMERO_MAXIMO_DE_SAQUES_DIARIOS} saques diario!')
        time.sleep(3)
        limpar_terminal()
        return False

    saldo -= valor
    transacao = criar_transacao('d', valor)
    extrato.append(transacao)
    numero_de_saques_diarios += 1
    return True


while True:
    print(menu)
    opcao = input()

    if opcao == 'd':
        limpar_terminal()
        valor = pegar_valor()
        if isinstance(valor, float):
            if deposito(valor):
                limpar_terminal()
                print('Transação realizada com sucesso!')
                time.sleep(3)
                limpar_terminal()
                continue
            else:
                limpar_terminal()
                print('Digite apenas números positivos')
                time.sleep(3)
                limpar_terminal()
                continue
        else:
            limpar_terminal()
            print('Digite apenas números!')
            time.sleep(3)
            limpar_terminal()
            continue
    elif opcao == 's':
        limpar_terminal()
        valor = pegar_valor()
        if isinstance(valor, float):
            if saque(valor):
                limpar_terminal()
                print('Transação realizada com sucesso!')
                time.sleep(3)
                limpar_terminal()
                continue
            else:
                limpar_terminal()
                continue
    elif opcao == 'e':
        limpar_terminal()
        print(extrato)
        print(f'Seu saldo total: {formatar_valor(saldo)}')
        time.sleep(3)
        limpar_terminal()
    elif opcao == 'q':
        limpar_terminal()
        print('Obrigado!')
        time.sleep(3)
        limpar_terminal()
        break
    else:
        print('Opção não encontrada')

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

saldo = 0
limite_de_de_valor_por_saque = 500
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
            'id': uuid(),
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


def criar_operacao(operacao, valor):
    if operacao == 'd':
        if valor > 0:
            saldo += valor
        else:
            limpar_terminal()
            print('deposito invalido')
            time.sleep(2)
            return
    elif operacao == 's':
        if valor > 500:
            limpar_terminal()
            print(f'limite por operação de {
                  formatar_valor(limite_de_de_valor_por_saque)}')
            time.sleep(2)
            return
        if numero_de_saques_diarios == NUMERO_MAXIMO_DE_SAQUES_DIARIOS:
            limpar_terminal()
            print(f'você tem um limite de saques diarios de {
                  NUMERO_MAXIMO_DE_SAQUES_DIARIOS}')
            time.sleep(2)
            return

        if valor < 0:
            saldo -= valor
            numero_de_saques_diarios += 1
        else:
            limpar_terminal()
            print('deposito invalido')
            time.sleep(2)
            return


def receber_valor():
    try:
        valor = float(input())
        return valor
    except Exception as e:
        limpar_terminal()
        print(e)
        print('Operação Invalida, digite apenas números')
        time.sleep(2)
        limpar_terminal()
        return


while True:
    print(menu)

    opcao = input()

    if opcao == 'd':
        limpar_terminal()
        print('Digite o valor que gostaria de depositar:')
        valor = receber_valor()
        criar_operacao('d', valor)
        transacao = criar_transacao('d', valor)
        extrato.append(transacao)
        limpar_terminal()
        print('Operação realizada com sucesso!')
        time.sleep(2)

    elif opcao == 's':
        limpar_terminal()
        print('Digite o valor que gostaria de sacar:')
        valor = receber_valor()
        criar_operacao('s', valor)
        transacao = criar_transacao('s', valor)
        extrato.append(transacao)
        limpar_terminal()
        print('Operação realizada com sucesso!')
        time.sleep(2)
    elif opcao == 'e':
        limpar_terminal()
        print(extrato)
        print(formatar_valor(saldo))
        time.sleep(5)
        limpar_terminal()
    elif opcao == 'q':
        limpar_terminal()
        print('Obrigado!')
        time.sleep(2)
        break
    else:
        limpar_terminal()
        print('Opção invalida! Por favor tente novamente')
        time.sleep(3)
        limpar_terminal()

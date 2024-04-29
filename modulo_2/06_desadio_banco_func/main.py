import contas
import transacoes
import utils

menu = """
[1] Cadastrar Nova conta;
[2] Operação Bancaria;
[q] Sair

Escolha a opção desejada
"""

while True:
    print(menu)
    op = input()

    if op == '1':
        result_login = contas.login()
        valid_login, message_login = result_login
        if valid_login:
            utils.limpar_terminal_mensagem(message_login, 2)
        else:
            utils.limpar_terminal_mensagem(message_login, 2)
            continue
    elif op == '2':
        transacoes.main()
    elif op == 'q':
        message = 'bye'
        utils.limpar_terminal_mensagem(message, 2)
        break
    else:
        message = 'Por favor digite uma das opções listadas no menu'
        utils.limpar_terminal_mensagem(message, 2)
        continue

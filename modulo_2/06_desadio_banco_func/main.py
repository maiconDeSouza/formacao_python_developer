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
        result = contas.main()
        if result is not None:
            concluido, message = result
            if concluido:
                utils.limpar_terminal_mensagem('Concluido!!', 3)
                continue
            else:
                utils.limpar_terminal_mensagem(message, 3)
                continue
    elif op == '2':
        transacoes.main()
    elif op == 'q':
        utils.limpar_terminal_mensagem('Bye', 2)
        break
    else:
        msg = 'Por favor digite uma opão correta!'
        tempo = 2
        utils.limpar_terminal_mensagem(msg, tempo)
        continue

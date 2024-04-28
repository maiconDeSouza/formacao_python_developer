import utils

login_gerente = 'Bill1'
senha_gerente = 'abc123'

menu = """
[1] criar nova conta;
[2] listar as contas;
[q] voltar para o menu anterior

Escolha a opção desejada
"""


def login():
    print('Digite o login para poder cadastrar uma nova conta:')
    login = input()

    utils.limpar_terminal_mensagem('', 0.5)

    print('Digite a senha para poder cadastrar a nova conta:')
    senha = input()

    if login == login_gerente and senha == senha_gerente:
        return True
    else:
        return False


def menu_contas():
    while True:
        print(menu)
        op = input()

        if op == '1':
            sucess, message = utils.criar_nova_conta()
            if sucess:
                msg = f'Conta criada com Sucesso!, {message}'
                utils.limpar_terminal_mensagem(msg, 5)
                break
            else:
                msg = f'algo deu errado, {message}'
                utils.limpar_terminal_mensagem(msg, 3)
                continue
        elif op == '2':
            print('Listar Contas')
        elif op == 'q':
            utils.limpar_terminal_mensagem('Voltando, aguarde...', 2)
            break
        else:
            msg = 'Por favor digite uma opão correta!'
            tempo = 2
            utils.limpar_terminal_mensagem(msg, tempo)
            continue


def main():
    utils.limpar_terminal_mensagem('Aguarde...', 2)
    login_is_valid = login()

    if login_is_valid:
        menu_contas()
    else:
        return (False, 'Login ou senha estão invalidas',)

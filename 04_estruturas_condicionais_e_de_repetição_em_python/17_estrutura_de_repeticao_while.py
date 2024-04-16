is_valid = True

while is_valid:
    print('Digite uma das opções abaixo')
    print('1 -> Sacar')
    print('2 -> Depositar')
    print('3 -> Sair')

    opcao = input()

    if opcao == '1':
        print('Saca ai muleke')
    elif opcao == '2':
        print('Deposita ai Muleke')
    elif opcao == '3':
        print('Falou Muleke!')
        is_valid = False
    else:
        print('Digite algo valido muleke')

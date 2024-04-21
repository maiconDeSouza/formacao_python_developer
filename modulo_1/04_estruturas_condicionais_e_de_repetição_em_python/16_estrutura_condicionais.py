saldo = 2000.00
saque = float(input('Digite o valor do seu saque: '))

if saldo < saque:
    print('Saque não permitido')
else:
    print('Saque liberado!!')


# tem o elif -> senão se

idade = 18

habilitacao = "Pode tirar carteira de habilitação" if idade >= 18 else "Não pode tirar carteira de habilitação"

print(habilitacao)

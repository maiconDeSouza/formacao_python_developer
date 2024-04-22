salario = 2000


def aplicar_bonus(bonus):
    global salario
    salario += bonus
    return salario


mcn = aplicar_bonus(1500)

print(mcn)


def funcao(*args, **kw):
    print(args)
    print(kw)


funcao("python", 2022, curso="dio")

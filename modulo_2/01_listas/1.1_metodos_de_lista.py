caixa_de_som = list('Tronsmart')


caixa_de_som_2 = caixa_de_som.copy()
caixa_de_som_2[0] = 't'
caixa_de_som_3 = caixa_de_som
caixa_de_som_4 = [letra.upper() for letra in caixa_de_som]

print(caixa_de_som, '->', id(caixa_de_som))
print(caixa_de_som_2, '->', id(caixa_de_som_2))
print(caixa_de_som_3, '->', id(caixa_de_som_3))
print(caixa_de_som_4, '->', id(caixa_de_som_4))
print('Quantas vez aparece a letra T ->', caixa_de_som_4.count('T'))

caixa_de_som_4.extend(caixa_de_som_4)
print(caixa_de_som_4)

d = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(d)

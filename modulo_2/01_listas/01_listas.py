teste = list('Maçã')
print(teste)

teste_2 = list(range(1, 11))
print(teste_2)


python = list('Python')
python_2 = python[::]
python_2[0] = 'p'
print(python)
print(python_2)

for ind in python:
    print(ind)

teste_2_par = [numero for numero in teste_2 if numero % 2 == 0]
print(teste_2_par)

teste_2_dobro = [numero * 2 for numero in teste_2]
print(teste_2_dobro)

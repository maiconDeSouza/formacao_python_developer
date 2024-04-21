import math

nome = 'Maicon'
idade = 36
profissao = 'Programador'
linguagem = 'Python'

frase = 'Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' % (
    nome, idade, profissao, linguagem)

print(frase)

frase2 = 'Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.'.format(
    nome, idade, profissao, linguagem)

print(frase2)

frase3 = f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {
    profissao} e estou matriculado no curso de {linguagem}.'

print(frase3)

PI = math.pi

print(f'{PI:.2f}')

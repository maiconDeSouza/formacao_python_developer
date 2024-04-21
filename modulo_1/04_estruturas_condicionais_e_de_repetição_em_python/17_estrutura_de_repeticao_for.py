texto = input('Digite um texto ou uma palavra: ')
vogais = 'AEIOU'
result = ''

for t in texto:
    t_upper = t.upper()
    if t_upper in vogais:
        result += t_upper
else:
    print(result)

for i in range(1, 24):
    print(i)

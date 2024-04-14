a = 200
b = 200
c = '200'
d = int(c)

print(f'a -> {id(a)}, b -> {id(b)}, c -> {id(c)}, d -> {id(d)}')
print(a is b)
print(a is c)

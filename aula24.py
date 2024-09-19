# Interpolação básica de strings
# s - string
# d e i - int
# f - float
# x e X - hexadecimal (ABCDEF0123456789)

nome = 'luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('o hexadecimal de %d é %04x' % (15, 15))
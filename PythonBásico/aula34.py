# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - indices e fatiamento
# Métodos uteis: append, insert, pop, del, clear, extend, +
# append - adiciona no final
# insert - adiciona no indice escolhido
# pop - remove do final ou indice escolhido
# del - apaga um indice
# clear - limpa a lista
# extend - estende a lista
# + concatena a lista

# indices positivos: +01234
# indices negativos: -54321

string = 'ABCDE' #5 caracteres (len)

lista = [123, True, 'Luiz Otávio' , 1.2, []] #lista com vários tipos de dados
print(lista)
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))

print()

lista2 = [10,20,30,40]
# lista2[2]=300
# del lista[2]
# print(lista2)
# print(lista2[2])
lista2.append(50)
lista2.pop()
lista2.append(60)
lista2.append(70)
ultimo_valor = lista2.pop(3)
print(lista2, 'removido, ', ultimo_valor)
lista2.append('luiz')
nome = lista2.pop()
lista2.append(1233)
del lista[-1]
#lista2,clear()
print(lista2)
lista.insert(0,5)
print(lista2)
print(lista[4])

print()

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)

print()

#for in com listas
lista_d = ['maria', 'luiz', 'helena']
for nome in lista_d:
    print(nome)
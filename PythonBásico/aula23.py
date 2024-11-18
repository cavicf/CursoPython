# Operadores in e not in
# String são iteráveis (pode navegar item por item)
# 0 1 2 3 4 5
# O t a v i o 
#-6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome)
print('b' in nome)
print('vio' in nome)
print('zero' in nome)
print('vio' not in nome) 

nomeDois = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nomeDois:
    print(f'{encontrar} está em {nomeDois}')
else:
    print(f'{encontrar} não está em {nomeDois}')
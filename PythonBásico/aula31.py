# While e for

senha_salva = '123456'
repeticoes = 0
senha_digitada = ''

while senha_salva != senha_digitada:
    senha_digitada = input(f'sua senha({repeticoes}x): ')
    repeticoes += 1
print(repeticoes)
print('aquele laço acima pode ter repetições infinitas')

#####################################################################

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print()
print(novo_texto)
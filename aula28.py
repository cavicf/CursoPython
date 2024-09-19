# Introdução ao try/excepet
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

print(1234)
print(456)
#float('a')
numero_str = input('vou dobrar o numero que vc digitar: ')


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('isso não é número')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é número')


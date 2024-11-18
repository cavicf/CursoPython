# Formatação básica de strings
# s - string
# d - int 
# f - float.<numer de digitos>f
# x ou X - hexadecimal
# = - força o numero a aparecer antes dos zeros
# (caractere)(<>^)(quantidade)
# > - esquerda
# < - direita
# ^ - Centro 
# sinal - + ou -
# ex.: 0>-100,.1f
# conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.478324732743294:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
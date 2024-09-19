#Operadores Lógicos
#and (e) or(ou) not(não)
#or - qualquer condição verdadeira
#se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor
#são considerados falsy (que vc ja viu)
#0 0.0 '' False
#Também existe o tipo None que é usado para representar um não valor


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E'or entrada == 'e') and (senha_digitada == senha_permitida):
    print('Entrar')
else:
    print('Sair')

#Avaliação de curto circuito
print(0.0 or False or 0 or 'abc' or True)


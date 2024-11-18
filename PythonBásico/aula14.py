a = 'A'
b = 'B'
c = 1.1
#outro tipo de formatação que segue a ordem dos argumentos da 
#função .format
#se utilizar dos indices podemos alterar as ordens
#e podemos passar parametros nomeados para a função como a nome3
string = 'a={0} b={1} c={nome3:.2f}'
formato = string.format(a, b, nome3=c)

print(formato)
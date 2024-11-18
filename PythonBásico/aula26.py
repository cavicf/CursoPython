# fatiamento de strings
# 012345678
# Olá mundo 
# -987654321
# Fatiamento [1:f:p][::] p é a quantidade de passos que vai ser percorrido
# Obs: a função len retorna a qtd de caracteres da str
# sempre pegar 1 a mais pra pegar até onde vc deseja

variavel = 'Olá mundo'
print(variavel[0:5])
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[::-1]) #vai de 0 a 9 porem com os indices negativos(invertido)


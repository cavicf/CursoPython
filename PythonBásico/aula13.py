#Camily tem 1.55 de altura e pesa 45 quilos e seu imc é?

nome = 'Camily Victal'
altura = 1.55
peso = 45
imc = peso / altura**2


#formatação de strings
#com o f na frente e as variaveis entre {}, temos uma formatação para impresão
#o :.f formata a quantidade de casas decimais que quermos imprimir
# a formatação :,.f é o limite das casas decimais com virgula pra dinheiro por exemplo
linha_1 = f'{nome} tem altura de {altura:.2f} e pesa {peso} quilos e tem imc de {imc:.2f}'
print(linha_1)

print(nome, 'tem', altura, 'de altura e pesa', peso, 'quilos e tem imc de', imc)

#as ellipsis (...) são placeholders ou seja, seguram o lugar
#da variavel para você
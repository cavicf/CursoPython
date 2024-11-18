#Coletando dados do usuário com a função input
#ela só coleta no tipo string por isso é importante o casting
#se colocar o = depois do nome da variavel no {} será exibido
#o nome da variavel mais o valor dela
nome = input('qual é seu nome? ')
print(f'O seu nome é {nome}')

#fazendo a conversão para que possa ser feita a conta
numero_1 = int(input('digite um numero: '))
numero_2 = int(input('digite outro numero: '))
print(f'a soma dos numeros é: {numero_1 + numero_2}')
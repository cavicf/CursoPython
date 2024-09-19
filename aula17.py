#Estruturas condicionais
#if/ elif    / else
#se/ se ão se/ se não
#o elif depende do if, é uma outra condição que depende do if

condicao = True
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

#só sera executado se a condição for verdadeira pois ele verifica
if condicao:
    print('este é o código do if')
#executa se for falso
else:
    print('este é o else do primeiro if')

if 10==10:
    print('outro if')

print('fora do bloco')

#pass é outro placeholder que o interpretador vai pular
#segue hierarquia de ordem, então se tiver duas consições verdadeiras
#sera executada somente a que veio primeiro

if condicao1:
    print('codigo para condicao 1')
elif condicao2:
    print('codigo pra condicao 2')
elif condicao3:
    print('codigo pra condicao 3')
elif condicao4:
    print('codigo pra condicao 4')
else:
    print('nenhuma condicao foi satisfeita')

print('fora dos ifs')

#Estruturas condicionais
#if/ elif    / else
#se/ se ão se/ se não
#o elif depende do if, é uma outra condição que depende do if

entrada = input('voce quer entrar ou sair? ')

if entrada == 'entrar':
    print('voce entrou no sistema')
elif entrada == 'sair':
    print('voce saiu do sistema')
else:
    print('voce não digitou nem entrar e nem sair')

print('se vc sai dos tabs e dos ifs,  você está fora dos blocos')
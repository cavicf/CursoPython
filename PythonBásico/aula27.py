nomeUsuario = input('Digite seu nome: ')
idadeUsuario = input('digite sua idade: ')

if nomeUsuario and idadeUsuario:
    print(f'Seu nome é {nomeUsuario}')
    print(f'Seu nome invertido é {nomeUsuario[::-1]}')
    if ' ' in nomeUsuario:
        print('Seu nome contém espaços')
    else:
        print('Não contem espaços')
    print(f'Seu nome tem {len(nomeUsuario)} letras')
    print(f'A primeira letra do seu nome é {nomeUsuario[0]}')
    print(f'A ultima letra do seu nome é {nomeUsuario[-1]}')
else:
    print('Desculpe, você deixou campos vazios')

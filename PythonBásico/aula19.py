primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor = {primeiro_valor} é maior do que o segundo_valor = {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'segundo_valor = {segundo_valor} é maior do que o primeiro_valor = {primeiro_valor}')
else:
    print('valores iguais')
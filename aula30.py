# flag (bandeira) - marcar um local
# none = não valor 
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade

# v1 = 'a'
# v2 = 'b'
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('não passou no if')
else:
    print('passou no if ')
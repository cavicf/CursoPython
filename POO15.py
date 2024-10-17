#Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação
# Mas nela, quando o objeto pai for apagado, todas as referencias dos objetos
# filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('maria')
cliente1.inserir_endereco('av brasil', 54)
cliente1.inserir_endereco('rua b', 64)
print(cliente1.enderecos[0].rua)
cliente1.listar_enderecos()

del cliente1

print('aqui termina meu código')
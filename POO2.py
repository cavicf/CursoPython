# Métodos em instâncias de classes Python
class Carro:
    def __init__ (self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelelrando')
        
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('celta')
print(celta.nome)
celta.acelerar()
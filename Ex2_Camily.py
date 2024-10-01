#Camily Victal Finamor / 2024001197
from abc import ABC, abstractmethod

#Classe base abstrata dos terrenos
class Terreno(ABC):
    def __init__(self, localizacao, preco):
        self._localizacao = localizacao
        self._preco = preco
    
    @property
    def localizacao(self):
        return self._localizacao
    
    @localizacao.setter
    def localizacao(self, nova):
        self._localizacao = nova
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        self._preco = valor
    
    @abstractmethod
    def calcula_peso(self):
        pass


##########################################################################

#Classe concreta: Terreno circular
class Circular(Terreno):
    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)
        self._raio = raio

    @property
    def raio(self):
        return self._raio
    
    def calcula_peso(self):
        area = 3.14 * (self._raio**2)
        return self.preco/area
    
##########################################################################

#Classe concreta: Terreno retangular
class Retangular(Terreno):
    def __init__(self, localizacao, preco, maior, menor):
        super().__init__(localizacao, preco)
        self._maior = maior
        self._menor = menor
    
    @property
    def maior(self):
        return self._maior
    
    @property
    def menor(self):
        return self._menor
    
    def calcula_peso(self):
        area = self._maior * self._menor
        return self._preco/area
    
###########################################################################

#Aqui vou criar a lista de terrenos e apontar qual deles terá o melhor 
#custo por metro quadrado
if __name__ == "__main__":
    #aqui inicializei instancias das classes com dados fictícios
    terreno1 = Circular('Brasília', 70000, 15)
    terreno2 = Retangular('Itajubá', 75000, 35, 20)
    terreno3 = Circular('Córrego', 110000, 20)
    
    #aqui criei a lista de terrenos
    terrenos = [terreno1, terreno2, terreno3]

    #aqui vou imprimir todos os dados antes de avaliar os preços
    for terreno in terrenos:
        print(f'Localização: {terreno.localizacao} - Preço: R${terreno.preco} - Peso:{terreno.calcula_peso()}')

    #Aqui vou fazer o teste de qual terá o melhor custo
    melhor_custo = min(terrenos, key=lambda terreno: terreno.calcula_peso())
    print(f'\nO melhor custo benefício é o terreno localizado em {melhor_custo.localizacao}, com preço de R${melhor_custo.preco} e peso de {melhor_custo.calcula_peso()}')


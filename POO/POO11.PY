# @property + @setter - getter e setter
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
#atributos que começam com _ não devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

#toda property tem um return
    @property
    def cor(self):
        print('property')
        return self._cor

    @cor.setter
    def cor(self,valor):
        if valor == 'Rosa':
            raise ValueError ('nao aceito essa cor')
        print('estou no seter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

##################################################

caneta = Caneta('Azul')
caneta.cor = 'pink'
#getter -> obter valor
caneta.cor_tampa = 'verde'
print(caneta.cor)
print(caneta.cor_tampa)
# @property - um getter no modo Pythonico
# getter - um método para obter um atributo
#cor -> get_cor()
# @property - é uma propriedade do objeto, ela é um método que se comporta como atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
#Código cliente - código que usa seu código


#Jeito Pythonico
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('property')
        return self.cor_tinta

    @property
    def cor_tampa(self):
      return 12345          
##################################################

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)





#Jeito tradicional
# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta
    
# ##################################################

# caneta = Caneta('Azul')
# print(caneta.get_color())
# print(caneta.get_color())
# print(caneta.get_color())
# print(caneta.get_color())
# print(caneta.get_color())
# print(caneta.get_color())
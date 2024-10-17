# Encapsulamento (modificadores de acesso: public, protected, private)
# python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
# (sem underline) = public
#     pode ser usado em qualquer lugar
# (um underline) = protected 
#     não deve ser usado fora da classe ou suas subclasses
# (dois underlines) = private 
#     só deve ser usado na classe em que foi declarado

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é protegido'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'


f = Foo()
print(f.public)
print(f.metodo_publico())

print(f._protected) #python permite mas é errado
print(f._metodo_protected()) #python permite mas é errado

print(f.__private) #python já nem permite
print(f.__metodo_private()) #python ja nem permite

#O correto seria utilizar os _ e __ só dentro de escopo de classes, o property permite o uso deles
#como se fossem publicos utilizando o .

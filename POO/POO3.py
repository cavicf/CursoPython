#Escopo da classe e de métodos da classe
#no construtor da classe, não precisamos declarar os métodos, apenas os atributos. Os métodos são definidos com o def.
#O __init__ é um inicializador de ATRIBUTOS
#tanto os atributos quanto os métodos precisam do self para que os objetos façam uso da classe
#Os métodos tem retornos então não esquecer dos return
class Animal:
    def __init__(self,nome):
        #na declaração dos atributos, não esquecer de inicializar eles com o self.(nome do atributo) e o atributo para qual aquela "função" está se referindo
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'


leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('maçã'))
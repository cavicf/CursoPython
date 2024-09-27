 #Métodos de classe + factories(fábricas)
#São métodos onde o self será "cls", ou seja, ao inves de receber a instancia no primeiro parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2023 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#quando se usa dos classmethods pra gerar novas instancias chamamos de fabricas 


#LEMBRAR: posso utilzar dos atributos da classe dentro dos métodos porque ai quando criarmos o objeto ele vai se encaixar no self e será passdo como atributo para os métodos trabalharem com esses valores
    @classmethod 
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod 
    def criar_sem_nome(cls, idade):
        return cls('anonima', idade)
    
    @classmethod #esse decorator permite que utilizemos métodos da classe sem precisar de objetos, pode usar a própria classe como naquele atributo global. O cls substitui o self para as classes
    def metodo_de_classe(cls):
        print('hey que legal')

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
print(Pessoa.ano)
print(p2.nome, p2.idade)
p4 = Pessoa.criar_sem_nome(23)
print(p4.nome, p4.idade)
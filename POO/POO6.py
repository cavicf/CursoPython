#Atributos de Classe
#quando utiliza o self a ordem de precedencia o python vai procurar na instancia(atributos) e depois na classe
#podemos criar uma variavel ou atributo "global" que será utilizado para todas as instancias e métodos da classe, mas é melhor fazer uso dele com o nome da classe para evitar erros

class Pessoa:
    ano_atual = 2022 #atributo global
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #utilizando o atributo global com o nome da classe


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

Pessoa.ano_atual = 1 

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(Pessoa.ano_atual)
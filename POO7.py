#__dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022 #atributo global


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #utilizando o atributo global com o nome da classe




#Com o dict e vars vc consegue consultar os atributos da sua classe e seus valores
#pode criar um dicionário pra guardar os dados e utilizá-los posteriormente com os objetos
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
print(p1.nome, p1.idade)
print(vars(p1))
# p2 = Pessoa('Helena', 12)

# Pessoa.ano_atual = 1 

# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())
# print(Pessoa.ano_atual)
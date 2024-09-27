#Camily Victal Finamor - 2024001197
from abc import ABC, abstractmethod

#Classe base das empregadas, é abstrata
class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome
    
    @property
    def telefone(self):
        return self._telefone
    
    @abstractmethod
    def getSalario(self):
        pass

#########################################################################

#Classe concreta: Empregada Horista
class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self._horasTrabalhadas = horasTrabalhadas
        self._valorPorHora = valorPorHora

    @property
    def horasTrabalhadas(self):
        return self._horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self._valorPorHora
    
    #Utilizando o método abstrato para calcular o salário das horistas
    def getSalario(self):
        return self.valorPorHora * self.horasTrabalhadas
    
#########################################################################

#Classe concreta: Diarista
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self._diasTrabalhados = diasTrabalhados
        self._valorPorDia = valorPorDia

    @property
    def diasTrabalhados(self):
        return self._diasTrabalhados
    
    @property
    def valorPorDia(self):
        return self._valorPorDia
    
    #Utilizando o método abstrato para calcular o salário das diaristas
    def getSalario(self):
        return self.diasTrabalhados * self.valorPorDia
    
#########################################################################

#Classe concreta: Mensalista
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self._valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self._valorMensal
    
    #Utilizando o método abstrato para calcular o salário das mensalistas
    def getSalario(self):
        return self.valorMensal
    
#########################################################################

#Aqui vou criar a lista de empregadas e apontar qual delas será mais
#econômica para a república
if __name__ == "__main__":
    #aqui inicializei instancias das classes com dados fictícios
    empregada1 = Horista('Mariana', '12312-1231', 160, 12)
    empregada2 = Diarista('Joana', '45645-4564', 20, 65)
    empregada3 = Mensalista('Ana', '78978-7897', 1200)
    
    #aqui criei a lista de empregadas
    empregadas = [empregada1, empregada2, empregada3]

    #aqui vou imprimir o valor mensal do salário de cada uma delas
    for empregada in empregadas:
        print(f'Nome: {empregada.nome} - Salário: R${empregada.getSalario()}')

    #Aqui vou fazer o teste de qual será mais barata para a república
    menor_valor = min(empregadas, key=lambda empregada: empregada.getSalario())
    print(f'A opção mais barata é a {menor_valor.nome}, seu telefone é {menor_valor.telefone}')
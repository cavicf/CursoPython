# Camily Victal Finamor - 2024001197

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome, cargo):
        self._codigo = codigo
        self._nome = nome
        self._cargo = cargo
        self._pontos = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def cargo(self):
        return self._cargo

    @property
    def pontos(self):
        return self._pontos

    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self._pontos.append(PontoFunc(mes, ano, faltas, atrasos))

    def lancaFaltas(self, mes, ano, nroFaltas):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.faltas = nroFaltas

    def lancaAtrasos(self, mes, ano, nroAtrasos):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.atrasos = nroAtrasos

    def getPonto(self, mes, ano):
        for ponto in self._pontos:
            if ponto.mes == mes and ponto.ano == ano:
                return ponto
        return PontoFunc(mes, ano, 0, 0)

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

    def imprimeFolha(self, mes, ano):
        salarioLiquido = self.calculaSalario(mes, ano)
        bonus = self.calculaBonus(mes, ano)
        print(f"Código: {self.codigo}\nNome: {self.nome}\nSalário Líquido: R${salarioLiquido:.2f}\nBônus: R${bonus:.2f}")

##########################################################################################

class Professor(Funcionario):
    def __init__(self, codigo, nome, cargo, salarioHora, nroAulas):
        super().__init__(codigo, nome, cargo)
        self._salarioHora = salarioHora
        self._nroAulas = nroAulas

    @property
    def salarioHora(self):
        return self._salarioHora

    @property
    def nroAulas(self):
        return self._nroAulas

    def calculaSalario(self, mes, ano):
        ponto = self.getPonto(mes, ano)
        salarioBruto = self.salarioHora * self.nroAulas
        descontoFaltas = self.salarioHora * ponto.faltas
        salarioLiquido = salarioBruto - descontoFaltas
        return salarioLiquido

    def calculaBonus(self, mes, ano):
        ponto = self.getPonto(mes, ano)
        salarioLiquido = self.calculaSalario(mes, ano)
        bonus = 0.1 * salarioLiquido
        bonus -= 0.01 * salarioLiquido * ponto.atrasos
        if bonus < 0:
            bonus = 0
        return bonus

##########################################################################################

class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, cargo, salarioMensal):
        super().__init__(codigo, nome, cargo)
        self._salarioMensal = salarioMensal

    @property
    def salarioMensal(self):
        return self._salarioMensal

    def calculaSalario(self, mes, ano):
        ponto = self.getPonto(mes, ano)
        descontoFaltas = (self.salarioMensal / 30) * ponto.faltas
        salarioLiquido = self.salarioMensal - descontoFaltas
        return salarioLiquido

    def calculaBonus(self, mes, ano):
        ponto = self.getPonto(mes, ano)
        salarioLiquido = self.calculaSalario(mes, ano)
        bonus = 0.08 * salarioLiquido
        bonus -= 0.01 * salarioLiquido * ponto.atrasos
        if bonus < 0:
            bonus = 0
        return bonus

##########################################################################################

class PontoFunc:
    def __init__(self, mes, ano, faltas, atrasos):
        self._mes = mes
        self._ano = ano
        self._faltas = faltas
        self._atrasos = atrasos

    @property
    def mes(self):
        return self._mes

    @property
    def ano(self):
        return self._ano

    @property
    def faltas(self):
        return self._faltas

    @faltas.setter
    def faltas(self, value):
        self._faltas = value

    @property
    def atrasos(self):
        return self._atrasos

    @atrasos.setter
    def atrasos(self, value):
        self._atrasos = value

##########################################################################################

if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()

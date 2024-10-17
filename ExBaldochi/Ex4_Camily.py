#Camily Victal Finamor - 2024001197
from datetime import date

#Classe Conta:
class Conta():
    def __init__(self, nroConta, nome, limite, senha):
        self._nroConta = nroConta
        self._nome = nome
        self._limite = limite
        self._senha = senha
        self._transacoes = []

    @property
    def nroConta(self):
        return self._nroConta
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def limite(self):
        return self._limite
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def transacoes(self):
        return self._transacoes
    
    @property
    def saldoFinal(self):
        return self._saldoFinal
    
    def adicionaDeposito(self, valor, data, nomeDepositante):
        deposito = Deposito(valor, data, nomeDepositante)
        return self._transacoes.append(deposito)
    
    def adicionaSaque(self, valor, data, senha):
        if senha != self._senha or self.calculaSaldo() < valor:
            return False
        saque = Saque(valor, data, senha)
        self._transacoes.append(saque)
    
    def adicionaTransf(self, valor, data, senha, contaFavorecido):
        if senha != self._senha or self.calculaSaldo() < valor:
            return False
        transf = Transferencia(valor, data, senha, "D")
        transf2 = Transferencia(valor, data, senha, "C")
        contaFavorecido._transacoes.append(transf2)
        self._transacoes.append(transf)
    
    def calculaSaldo(self):
        saldoFinal = 0
        for i in self._transacoes:
            if isinstance(i, Deposito) or (isinstance(i, Transferencia) and i.tipoTransf == "C"):
                saldoFinal += i.valor
            elif isinstance(i, Saque) or (isinstance(i, Transferencia) and i.tipoTransf == "D"):
                saldoFinal -= i.valor
        return saldoFinal + self._limite
    
###################################################################################################
#Classe Mãe Transacao:
class Transacao:
    def __init__(self, valor, data):
        self._valor = valor
        self._data = data

    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        return self._data

#####################################################################################################
#Classe filha Saque:
class Saque(Transacao):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self._senha = senha

    @property
    def senha(self):
        return self._senha

#####################################################################################################
#Classe filha Deposito:
class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self._nomeDepositante = nomeDepositante

    @property
    def nomeDepositante(self):
        return self._nomeDepositante

####################################################################################################
#Classe filha Transferencia:
class Transferencia(Transacao):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self._senha = senha
        self._tipoTransf = tipoTransf

    @property
    def senha(self):
        return self._senha
    
    @property
    def tipoTransf(self):
        return self._tipoTransf
    
####################################################################################################
# Aqui vou fazer o teste com o main
if __name__ == "__main__":
  c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
  c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
  if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
      print('Não foi possível realizar o saque no valor de 2000')
  if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
      print('Não foi possível realizar o saque no valor de 1000')

  c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
  c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
  if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
      print('Não foi possível realizar o saque no valor de 1500')
  if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
      print('Não foi possível realizar a transf no valor de 5000')
  if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
      print('Não foi possível realizar a transf no valor de 800')

  print('--------')
  print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
  print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700
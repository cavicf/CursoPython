from abc import ABC, abstractmethod

#classe das transações
class Transacao():
    def __init__(self, valor, desc):
        self._valor = valor
        self._desc = desc
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def desc(self):
        return self._desc

#########################################################################

#classe mãe abstrata
class Conta(ABC):
    def __init__(self, nmr_conta, nome, saldo):
        self._nmr_conta = nmr_conta
        self._nome = nome
        self._saldo = saldo
        self._listaTrans = []

    @property
    def nmr_conta(self):
        return self._nmr_conta
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def listaTrans(self):
        return self._listaTrans
    
    def deposito(self, valor, desc):
        self._listaTrans.append(Transacao(valor, desc))
        self._saldo += valor

    def saque(self, valor, desc):
        if valor>0:
            return False
        if self._saldo + valor < 0:
            return False
        self._listaTrans.append(Transacao(valor, desc))
        self._saldo += valor
        return True

    @abstractmethod
    def imprimirExtrato(self):
        pass 



#######################################################################

#classe da conta corrente
class Corrente(Conta):
    def __init__(self, nmr_conta, nome, saldo, mensalidade):
        super().__init__(nmr_conta, nome, saldo)
        self._mensalidade = mensalidade
    
    @property
    def mensalidade(self):
        return self._mensalidade
    
    def imprimirExtrato(self):
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Valor da mensalidade descontado: {self._mensalidade}')
        print(f'saldo com desconto: {self.saldo - self._mensalidade}')

########################################################################

#classe Conta Limite
class ContaLimite(Conta):
    def __init__(self, nmr_conta, nome, saldo, limite):
        super().__init__(nmr_conta, nome, saldo)
        self._limite = limite
    
    @property
    def limite(self):
        return self._limite
    
    def saque(self, valor, desc):
        if valor>0:
            return False
        if self.saldo + self._limite + valor < 0:
            return False
        self.listaTrans.append(Transacao(valor, desc))
        self._saldo += valor
        return True
    
    def imprimirExtrato(self):
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Saldo + limite: {self.limite + self.saldo}')

###########################################################################

#classe poupança
class Poupanca(Conta):
    def __init__(self, nmr_conta, nome, saldo, diaAnv):
        super().__init__(nmr_conta, nome, saldo)
        self._diaAnv = diaAnv
    
    @property
    def diaAnv(self):
        return self._diaAnv
    
    def imprimirExtrato(self):
        print(f'Nro Conta: {self.nmr_conta}')
        print(f'Nome: {self.nome}')
        print(f'Saldo: {self.saldo}')
        print(f'Dia do aniversário: {self._diaAnv}')

###########################################################################
if __name__ == "__main__":
    contas = []
    cl = ContaLimite(1111, 'Ana Souza', 0, 1000)
    cl.deposito(1500, 'crédito salário')
    if cl.saque(-1200, 'pagamento boleto'):
        print(f'saque de R$1200,00 na conta {cl.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$1200,00 na conta {cl.nmr_conta}')

    if cl.saque(-500, 'PIX'):
        print(f'saque de R$500,00 na conta {cl.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$500,00 na conta {cl.nmr_conta}')


    cc = Corrente(22222, 'Pedro José', 9000, 200)
    cc.deposito(10000, 'salário')
    if cc.saque(-100, 'pagamento boleto'):
        print(f'saque de R$100,00 na conta {cc.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$1200,00 na conta {cl.nmr_conta}')

    if cc.saque(-500, 'PIX'):
        print(f'saque de R$500,00 na conta {cc.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$500,00 na conta {cl.nmr_conta}')

    cp = Poupanca(3333, 'Klaber da Silva', 400, '04/09')
    cp.deposito(1500, 'crédito salário')
    if cp.saque(-100, 'pagamento boleto'):
        print(f'saque de R$100,00 na conta {cp.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$100,00 na conta {cp.nmr_conta}')

    if cp.saque(-300, 'PIX'):
        print(f'saque de R$300,00 na conta {cp.nmr_conta}')
    else:
        print(f'falha ao realizar saque de R$300,00 na conta {cp.nmr_conta}')



    contas.append(cl)
    contas.append(cc)
    contas.append(cp)

    print()

    for conta in contas:
        conta.imprimirExtrato()
        print()
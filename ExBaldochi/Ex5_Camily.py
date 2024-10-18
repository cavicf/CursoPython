#Camily Victal Finamor - 2024001197

from abc import ABC, abstractmethod
from datetime import date

#Classe abstrata Venda
class Venda(ABC):
    def _init_(self, nroNF, dtEmissao):
        self._nroNF = nroNF
        self._dtEmissao = dtEmissao
        self._itens = []

    @property
    def nroNF(self):
        return self._nroNF
    
    @property
    def dtEmissao(self):
        return self._dtEmissao
    
    @property
    def itens(self):
        return self._itens
    
    def adicionaItem(self, codProd, quant, precoUnit):
        item = Item_Venda(codProd, quant, precoUnit)
        self._itens.append(item)

    def calculaTotalVendido(self):
        return sum([p.precoUnit * p.quant for p in self._itens])
    

    @abstractmethod
    def geraNF(self):
        pass

    @abstractmethod
    def calculaImposto(self):
        pass

#########################################################################
#Classe concreta da venda a pessoa fisica
class VendaPF(Venda):
    def _init_(self, nroNF, dtEmissao, cpf, nome):
        super()._init_(nroNF, dtEmissao)
        self._cpf = cpf
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    def geraNF(self):
        pass

    def calculaImposto(self):
        total = venda.calculaTotalVendido()
        return (9/100) * total
    
######################################################################
#Classe concreta de venda a pessoa juridica
class VendaPJ(Venda):
    def _init_(self, nroNF, dtEmissao, cnpj, nomeFantasia):
        super()._init_(nroNF, dtEmissao)
        self._cnpj = cnpj
        self._nomeFantasia = nomeFantasia

    @property
    def cnpj(self):
        return self._cnpj
    
    @property
    def nomeFantasia(self):
        return self._nomeFantasia
    
    def geraNF(self):
        pass

    def calculaImposto(self):
        total = venda.calculaTotalVendido()
        return (6/100) * total
    
#######################################################################
#Classe dos itens que é agregada a venda
class Item_Venda:
    def _init_(self, codProd, quant, precoUnit):
        self._codProd = codProd
        self._quant = quant
        self._precoUnit = precoUnit

    @property
    def codProd(self):
        return self._codProd
    
    @property
    def quant(self):
        return self._quant
    
    @property
    def precoUnit(self):
        return self._precoUnit
######################################################################
#Testando tudo com o main fornecido 

if _name_ == "_main_": 
    totalFaturado = 0 
    totalImposto = 0 
    vendas = [] 
    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao') 
    vendapf.adicionaItem(100, 10, 10) 
    vendapf.adicionaItem(100, 10, 20) 
    vendapf.adicionaItem(100, 10, 30) 
    vendas.append(vendapf) 
    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda') 
    vendapj.adicionaItem(200, 100, 10) 
    vendapj.adicionaItem(201, 100, 20) 
    vendas.append(vendapj) 
    for venda in vendas: 
        totalFaturado += venda.calculaTotalVendido() 
        totalImposto += venda.calculaImposto() 
    print('Total faturado: {}'.format(totalFaturado)) 
    print('Total pago em impostos: {}'.format(totalImposto))
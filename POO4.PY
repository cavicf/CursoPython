class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.marca = marca
        self.cor = cor
        self.motorLigado = motorLigado

    def ligarMotor(self):
        if self.motorLigado == True:
            print('motor ja está ligado')
        else:
            self.motorLigado = True
            print('motor acaba de ser ligado')

class Moto(Veiculo):
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.estilo = estilo
        
    def mostrarAtributos(self):
        print(f'Esta é uma moto da {self.marca} de cor {self.cor} e estilo {self.estilo}')
        if (self.motorLigado):
            print('seu motor esta ligado') 
        else: print('seu motor está desligado')

class Carro(Veiculo):
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self.portaMalasCheio = portaMalasCheio

    def encherPortaMalas(self):
        if self.portaMalasCheio == True:
            print('porta malas ja cheio')
        else:
            self.portaMalasCheio = True
            print('porta malas acaba de ser cheio')

    def mostrarAtributos(self):
        print(f'Este é um carro da {self.marca} de cor {self.cor}')
        if (self.portaMalasCheio):
            print('seu porta malas esta cheio') 
        else: print('seu porta malas está vazio')


moto1 = Moto('Honda', 'Azul', False, 'trail' )
moto1.ligarMotor()
moto1.mostrarAtributos()

carro1 = Carro('fiat', 'prata', False, False)
carro1.encherPortaMalas()
carro1.mostrarAtributos()
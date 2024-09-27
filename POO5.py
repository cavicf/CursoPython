#Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome 
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja está filmando')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
         
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

c1 = Camera('canon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
#print(c1.filmando)
#print(c2.filmando)

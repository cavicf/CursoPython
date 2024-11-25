#Camily Victal Finamor - 2024001197
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
#MODEL----------------------------------------------------------------------------
class Aluno:
    def __init__(self, cpf, nome, email, tipoAula, professor, nmrAulas):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__tipoAula = tipoAula
        self.__professor = professor
        self.__nmrAulas = nmrAulas

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def tipoAula(self):
        return self.__tipoAula
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def nmrAulas(self):
        return self.__nmrAulas

#VIEWCADASTRAR-------------------------------------------------------------------
class ViewCadastrar(tk.Toplevel):
    def __init__(self, controlador, listaProfessor):
        tk.Toplevel.__init__(self)
        self.controlador = controlador
        self.geometry('300x250')
        self.title('Cadastrar Aluno')

        self.framecpf = tk.Frame(self)
        self.framenome = tk.Frame(self)
        self.frameemail = tk.Frame(self)
        self.frametpaula = tk.Frame(self)
        self.frameprof = tk.Frame(self)
        self.framenmraula = tk.Frame(self)
        self.framebotao = tk.Frame(self)
        self.framecpf.pack()
        self.framenome.pack()
        self.frameemail.pack()
        self.frametpaula.pack()
        self.frameprof.pack()
        self.framenmraula.pack()
        self.framebotao.pack()

        self.labelcpf = tk.Label(self.framecpf, text='CPF:')
        self.labelcpf.pack(side='left')
        self.inputcpf = tk.Entry(self.framecpf, width=20)
        self.inputcpf.pack(side='left', padx=5)

        self.labelnome = tk.Label(self.framenome, text='Nome:')
        self.labelnome.pack(side='left')
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side='left',padx=5)

        self.labelemail = tk.Label(self.frameemail, text='Email:')
        self.labelemail.pack(side='left')
        self.inputemail = tk.Entry(self.frameemail, width=20)
        self.inputemail.pack(side='left',padx=5)

        self.labeltipo = tk.Label(self.frametpaula, text='Selecione o tipo:')
        self.labeltipo.pack(side='left')
        self.escolhatipo = tk.StringVar()
        self.combotipo = Combobox(self.frametpaula, width=15, textvariable=self.escolhatipo)
        self.combotipo.config(values=('--Selecione--','Pilates', 'Funcional'))
        self.combotipo.current(0)
        self.combotipo.pack(side='left')

        self.labelprof = tk.Label(self.frameprof, text='Selecione o prof:')
        self.labelprof.pack(side='left')
        self.escolhaprof = tk.StringVar()
        self.comboprof = Combobox(self.frameprof, width=15, textvariable=self.escolhaprof)
        self.comboprof.config(values=('--Selecione--', listaProfessor))
        self.combotipo.current(0)
        self.comboprof.pack(side='left')

        self.labelnmr = tk.Label(self.framenmraula, text='Número de aulas:')
        self.labelnmr.pack(side='left')
        self.escolhanmr = tk.StringVar()
        self.combonmr = Combobox(self.framenmraula, width=15, textvariable=self.escolhaprof)
        self.combonmr.config(values=('--Selecione--','2 aulas', '3 aulas', '4 aulas'))
        self.combonmr.current(0)
        self.combonmr.pack(side='left')

        self.botaoCadastrar = tk.Button(self.framebotao, text='Cadastrar', command=self.controlador.salvarAluno)
        self.botaoCadastrar.pack(side='left',pady=5, padx=5)
        self.botaoClear = tk.Button(self.framebotao, text='Limpar', command=self.controlador.limparCampos)
        self.botaoClear.pack(side='left', pady=5)

#VIEWCCONSULTAR----------------------------------------------------------------------
class ViewConsultar(tk.Toplevel):
    def __init__(self):
        pass

#VIEWMOSTAR---------------------------------------------------------------------


#CONTROLADORPROFISSIONAL--------------------------------------------------------
class ControladorAluno:
    def __init__(self, controladorPrincipal):
        self.controladorPrincipal = controladorPrincipal

    def cadastrarAluno(self):
        listaprofessor = self.controladorPrincipal.ControladorProfissional.getlistaprof()
        self.ViewCadastrar = ViewCadastrar(self, listaprofessor)
    
    def consultarAluno(self):
        self.ViewConsultar = ViewConsultar(self)

    def salvarAluno(self):
        pass

    def limparCampos(self):
        pass

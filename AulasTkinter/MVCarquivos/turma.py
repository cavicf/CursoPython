import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Turma:
    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def disciplina(self):
        return self.__disciplina

    @property
    def estudantes(self):
        return self.__estudantes


class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Turma")
        self.controle = controle

        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()        

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        #feito por combobox
        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar() #o que foi selecionado vai ficar armazenado na variavel
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip #popula o combobox com a lista de desciplinas
          
        #feito por listabox
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric: #necessário fazer um for na listabox para popular a lista de alunos
            self.listbox.insert(tk.END, nro)


        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno) #função "insereAluno" de callback no controladorPrincipal


        self.buttonCria = tk.Button(self.frameButton ,text="Cria Turma")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma) #função "criaAluno" de callback no controladorPrincipal

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal #fornece acesso aos demais controladores
        self.listaTurmas = []

    def insereTurmas(self):        
        self.listaAlunosTurma = [] #lista para conter os alunos das turmas -> cada turma vai ter uma lista destes alunos
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas() #pelo controlador principal, executa uma função do controlador da disciplina
        listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric() #pelo controlador principal, executa uma função do controlador do estudante
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, listaNroMatric) #tela (interface) que será feita a inserção | self fará a função de callback

    def criaTurma(self, event):
        codTurma = self.limiteIns.inputCodTurma.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        turma = Turma(codTurma, disc, self.listaAlunosTurma) #criação do objeto turma
        self.listaTurmas.append(turma) #appenda o objeto turma na lista de turmas
        self.limiteIns.mostraJanela('Sucesso', 'Turma criada com sucesso')
        self.limiteIns.destroy()

    def insereAluno(self, event):
        #tk.ACTIVE -> retorna o ativo atual que está armazenado
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE) #alunoSel -> pega o aluno selecionado
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel) #puxa os dados do estudante e armazena na variavel aluno
        self.listaAlunosTurma.append(aluno) #insere na lista de aluno da turma
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE) #removo o aluno que já foi selecionado da lista

    def mostraTurmas(self):
        str = ''
        for turma in self.listaTurmas:
            str += 'Código: ' +  turma.codigo + '\n'
            str += 'Disciplina: ' + turma.disciplina.codigo + '\n'
            str += 'Estudantes:\n'
            for estudante in turma.estudantes:
                str += estudante.nome + ' - ' + estudante.nroMatric + '\n'
            str += '---------------\n'
        self.limiteLista = LimiteMostraTurmas(str)
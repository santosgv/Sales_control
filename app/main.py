from tkinter import *
from .telas import SubTelas

main=Tk()

class Aplicacao(SubTelas):
    def __init__(self):
        # configuracao das funçoes do sistema
        self.main=main
        self.mainbox()
        self.windows()
        self.buttons()
        main.mainloop()

    def mainbox(self):
        # configuracao do layout da tela principal da aplicacao
        self.main.title('Controle financeiro')
        self.main.configure(background='black')
        self.main.geometry('500x400')
        self.main.resizable(False, False)

    def windows(self):
        # Janela principal do aplicacao
        self.mainframe =Frame(self.main, bg='white')
        self.mainframe.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def buttons(self):
        # Botoes da aplicacao
        self.btprod=Button(self.mainframe,text='Registrar',bg='#7B68EE',fg='white',command=self.Icadastro)
        self.btprod.place(relwidth=0.25, relheight=0.10,relx=0.02,rely=0.45)

        self.btvender=Button(self.mainframe,text='Movimentacao',bg='#7B68EE',fg='white',command=self.Ivender)
        self.btvender.place(relwidth=0.25, relheight=0.10,relx=0.38,rely=0.45)

        self.btfluxo=Button(self.mainframe,text='Balanço' ,bg='#7B68EE',fg='white',command=self.Ibalanco)
        self.btfluxo.place(relwidth=0.25, relheight=0.10,relx=0.72,rely=0.45)



from tkinter import *


main=Tk()


class SubTelas():
    # Subtelas do sistema
    def Icadastro(self):
        Icadastro = Toplevel(self.mainframe, bg='red')
        Icadastro.geometry('500x400')
        Icadastro.title('Produtos')
        Icadastro.resizable(False, False)
        Button(Icadastro, text='Teste').place(relx=0.1, rely=0.1)


    def Ivender(self):
        # Tela de vendas
        Icadastro = Toplevel(self.mainframe, bg='green')
        Icadastro.geometry('500x400')
        Icadastro.title('Venda')
        Icadastro.resizable(False, False)
        #
        a=Button(Icadastro, text='Exibir veiculos').place(relx=0.30, rely=0.60)
    def Ibalanco(self):
        # tela de balanço
        Icadastro = Toplevel(self.mainframe, bg='green')
        Icadastro.geometry('500x400')
        Icadastro.title('Balanco')
        Icadastro.resizable(False, False)

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
        self.main.title('Sales Control')
        self.main.configure(background='black')
        self.main.geometry('500x400')
        self.main.resizable(False, False)

    def windows(self):
        # Janela principal do aplicacao
        self.mainframe =Frame(self.main, bg='white')
        self.mainframe.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def buttons(self):
        # Botoes da aplicacao
        self.btprod=Button(self.mainframe,text='Cadastrar Produto',bg='#7B68EE',fg='white',command=self.Icadastro)
        self.btprod.place(relwidth=0.25, relheight=0.10,relx=0.02,rely=0.45)

        self.btvender=Button(self.mainframe,text='Vender',bg='#7B68EE',fg='white',command=self.Ivender)
        self.btvender.place(relwidth=0.25, relheight=0.10,relx=0.38,rely=0.45)

        self.btfluxo=Button(self.mainframe,text='Balanço' ,bg='#7B68EE',fg='white',command=self.Ibalanco)
        self.btfluxo.place(relwidth=0.25, relheight=0.10,relx=0.72,rely=0.45)


Aplicacao()
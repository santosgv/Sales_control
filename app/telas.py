from tkinter import *

class SubTelas():
    # Subtelas do sistema
    def Icadastro(self):
        Icadastro = Toplevel(self.mainframe, bg='red')
        Icadastro.geometry('500x400')
        Icadastro.title('Despesa X ganhos')
        Icadastro.resizable(False, False)
        Button(Icadastro, text='Despesa').place(relx=0.1, rely=0.1)


    def Ivender(self):
        # Tela de vendas
        Ivender = Toplevel(self.mainframe, bg='green')
        Ivender.geometry('500x400')
        Ivender.title('movimentaçoes')
        Ivender.resizable(False, False)
        Button(Ivender, text='Exibir').place(relx=0.30, rely=0.60)

    def Ibalanco(self):
        # tela de balanço
        Ibalanco = Toplevel(self.mainframe, bg='yellow')
        Ibalanco.geometry('500x400')
        Ibalanco.title('Balanco')
        Ibalanco.resizable(False, False)
        Button(Ibalanco, text='Balanco').place(relx=0.30, rely=0.60)
import tkinter as tk
from tkinter import Frame, Label, StringVar, ttk
from ttkthemes import ThemedStyle
import pyodbc 
import pandas as pd

class Win(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.widgets()
        
    def conection(self):
        print("Connecting...")

        self.conection_database = (
            "Driver={SQL Server};"
            "Server=DESKTOP\MSSQLSERVER01;"
            "Database=accounts;"
        )

        self.conect = pyodbc.connect(self.conection_database)
        print("Sucess")

        self.cursor =  self.conect.cursor()

        self.account_id = f"""
        SELECT id_account FROM usuarios
        ;"""
    
    def show_account(self):
        #metodo para acessar os valores do banco 
        self.columns = ('ACCOUNT', 'FIRST NAME', 'LAST NAME','TYPE','BALANCE', 'STATUS')

        self.tree = ttk.Treeview(self.second_frame, columns= self.columns, show='headings', height= 3)

        # ajustando o tamanho das colunas da treeview
        self.tree.column('ACCOUNT', width= 90)
        self.tree.column('FIRST NAME', width= 100)
        self.tree.column('LAST NAME', width= 100)
        self.tree.column('TYPE', width= 70)
        self.tree.column('BALANCE', width= 100)
        self.tree.column('STATUS', width= 70)

        self.tree.heading('ACCOUNT', text='ACCOUNT')
        self.tree.heading('FIRST NAME', text='FIRST NAME')
        self.tree.heading('LAST NAME', text='LAST NAME')
        self.tree.heading('TYPE', text='TYPE')
        self.tree.heading('BALANCE', text='BALANCE')
        self.tree.heading('STATUS', text='STATUS')

        self.tree.grid(row= 0, column= 0,)
    
    def show_account_update(self):
        self.show_account()
        #o self.id é o DADO BASE TOTAL para as manipulacoes no banco
        self.id = str(self.lb.get(self.lb.curselection())[1:2])

        self.consult = f"""
        SELECT * FROM usuarios
        WHERE id_account = {self.id};"""

        self.select_consult = self.cursor.execute(self.consult)

        for rows in self.select_consult:
            self.tree.insert("", tk.END, values=rows)
        
        self.tree.grid(row= 0, column= 0,)

    def widgets(self):
        self.conection()
        # criando frames para organizacao dos programas
        #--------------------------------------------------
        #frame central onde sera posto todas as janelas de conteudos
        self.central_frame = ttk.LabelFrame(self)
        self.central_frame.pack()
        
        #frame principal para manipulacao dos demais itens
        self.first_frame = ttk.LabelFrame(self.central_frame, text= " ")
        self.first_frame.grid(row= 0 , column= 0)

        #frame para os conteudos dos botoes
        self.framebuttonsTop = ttk.Frame(self.first_frame) 
        self.framebuttonsTop.grid(row = 1 , column= 0, pady=5) 

        #frame para a parte de baixo  do nosso programa 
        self.second_frame = ttk.Frame(self.central_frame)
        self.second_frame.grid(row= 1, column= 0)

        #frame dos botoes de edicao do segundo frame
        self.framebuttonsDown = ttk.Frame(self.central_frame)
        self.framebuttonsDown.grid(row = 2, column= 0,)
        #--------------------------------------------------
    
        #criando a listbox das contas
        self.lb = tk.Listbox(self.first_frame)
        self.lb.grid(row= 0,  column=0)

        self.consult = self.cursor.execute(self.account_id)
        
        for self.clients in self.consult:
            self.lb.insert(tk.END ,f"{self.clients}.CONTA")

        #criando botao select
        self.bs = ttk.Button(self.framebuttonsTop,
                             text="SELECT",
                             command= self.selectAccount)
        self.bs.grid(row=1, column=0)
        #metodo que cria em branco a tree em branco no começo
        self.show_account()
        
    def selectAccount(self):
        #ajuste do botao de select para melhor aparencia do projeto
        self.bs.grid(row=1, column=1, padx=90)

        self.bn = ttk.Button(self.framebuttonsTop,
                                text="NEW ACCOUNT")
        self.bn.grid(row=1, column=0)

        self.be = ttk.Button(self.framebuttonsTop,
                                text="EDIT ACCOUNT",
                                command= self.edit
                                )
        self.be.grid(row = 1, column = 2)
        # metodo de mostrar os dados 
        self.show_account_update()

        
    def edit(self):
        #escondendo os botoes para melhor aparencia estetica
        
        #ajustando a janela de informacoes 
        self.second_frame.grid(row= 1, column= 0, sticky="W", pady= 5, padx= 10)

        self.b1 = ttk.Button(self.framebuttonsDown,
                        command= self.balanceMovement, 
                        text="DEPOSIT / WITHDRAW",
                        width=25)
        self.b1.grid(row= 0, column=0) 

        self.b2 = ttk.Button(self.framebuttonsDown,
                        text="CHANGE ACCOUNT TYPE",
                        width=25)
        self.b2.grid(row= 1, column= 0) 

        self.b3= ttk.Button(self.framebuttonsDown,
                        text="CHANGE ACCOUNT STATUS",
                        width=25)
        self.b3.grid(row= 2, column= 0)

        self.b4 = ttk.Button(self.framebuttonsDown,
                        text="DELETE ACCOUNT",
                        width=25)
        self.b4.grid(row= 3, column= 0)

        self.b5 = ttk.Button(self.framebuttonsDown,
                        text="FINISH EDITION",
                        width=25)
        self.b5.grid(row= 4, column= 0)

    def balanceMovement(self):
        #config nova janela 
        self.new_root = tk.Toplevel()
        self.new_root.title("OPERAÇÃO")
        self.new_root.geometry("253x200")
        #criando todos os componentes da segunda janela 

        #mesmo esquema para essa janela para melhor manuseio do sistema
        
        #frame que vai englobar toda a ganela 
        self.central_new_root = ttk.LabelFrame(self.new_root)
        self.central_new_root.pack()

        #frame onde sera posto os conteudos
        self.frame_new_root = ttk.LabelFrame(self.central_new_root)
        self.frame_new_root.grid(row= 0, column=0)

        self.text = ttk.Label(self.frame_new_root,
                              text="Insira a seguir o valor e escolha a operação"
                                )
        self.text.grid(row= 0, column= 0)

        self.lb2 = ttk.Label(self.frame_new_root,
                        text="R$")
        self.lb2.grid(row = 1, column= 0, sticky='W')

        self.entry = ttk.Entry(self.frame_new_root,)
        self.entry.grid(row= 1, column= 0, sticky="E", padx = 0)

        


if __name__ == "__main__":
    root = tk.Tk()
    root.title('BANCO IO 1.0')
    root.geometry("720x700")
    root.iconphoto
    # Simply set the theme
    style = ThemedStyle(root)
    style.set_theme('breeze')
    app = Win(root)
    app.pack(fill="both", expand=True)


    root.mainloop()
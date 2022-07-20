import tkinter as tk
from tkinter import Frame, Label, StringVar, ttk
from ttkthemes import ThemedStyle
import pyodbc 
import pandas as pd

class Win(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.widgets()

        self.box_settings = ttk.LabelFrame(self.central_frame)
        self.box_settings.grid(row= 2, column= 0, sticky= 'NE')

        self.frame_balance_buttons = ttk.LabelFrame(self.box_settings)
        self.frame_balance_buttons.grid(row = 2, column=0, sticky= 'W')
        
    def conection(self): # Aqui criamos a conecão com o banco de dados 
        print("Connecting...")

        self.conection_database = (
            "Driver={SQL Server};"
            "Server=DESKTOP\MSSQLSERVER01;"
            "Database=accounts;"
        )

        self.conect = pyodbc.connect(self.conection_database)
        print("Sucess")

        self.cursor =  self.conect.cursor()

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

        self.msg_conecion = ttk.Label(self.central_frame, text="Connecting...")
        self.msg_conecion.grid(row = 0, column = 0)
        self.conection()
        self.msg_conecion.config(text= "Success!")
        self.msg_conecion.destroy()

        #criando a listbox das contas
        self.lb = tk.Listbox(self.first_frame)
        self.lb.grid(row= 0,  column=0)

        # Aqui criamos o comando que seleciona os ID das contas no banco 
        self.account_id = f"""
        SELECT id_account FROM usuarios
        ;"""
        self.consult = self.cursor.execute(self.account_id)
        # E aqui colocamos numa lista de consulta para acessalos para a edição 
        for self.clients in self.consult:
            self.lb.insert(tk.END ,f"{self.clients}.CONTA")

        #criando botao select
        self.bs = ttk.Button(self.framebuttonsTop,
                             text="SELECT",
                             command= self.selectAccount)
        self.bs.grid(row=1, column=0)
        #metodo que cria em branco a tree no começo
        self.show_account()

    #Aqui começamos a criar o que cada botão da parte superior faz
    #------------------------------------------------------------------------------------------------------    
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
                        command= self.changeAccount,
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
                        # command= self.finishEdit,
                        text="FINISH EDITION",
                        width=25)
        self.b5.grid(row= 4, column= 0)

    def new_account(self):
        pass
    #------------------------------------------------------------------------------------------------------
    #Aqui criamos os metodos dos botoes de baixo
    #------------------------------------------------------------------------------------------------------
    def balanceMovement(self):
        self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NW')

        self.text_balance = ttk.Label(self.box_settings,
                              text="Insira a seguir o valor e escolha a operação"
                                )
        self.text_balance.grid(row= 0, column= 0)

        self.lb2 = ttk.Label(self.box_settings,
                        text="R$")
        self.lb2.grid(row = 1, column= 0, sticky='W',)

        self.entry_balance = ttk.Entry(self.box_settings)
        self.entry_balance.grid(row= 1, column= 0)

        self.bt_deposito = ttk.Button(self.frame_balance_buttons, 
                                      command= self.depositAccount,
                                      text= "DEPOSITAR")
        self.bt_deposito.grid(row = 0, column= 0, padx= 30)

        self.bt_saque = ttk.Button(self.frame_balance_buttons,
                                   command= self.draftAccount,
                                   text= "SAQUE")
        self.bt_saque.grid(row = 0, column= 1, padx= 10)
        
    def changeAccount(self):
        self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NW')

        self.text_account = ttk.Label(self.box_settings,
                              text="Para qual tipo de conta desejaria mudar?"
                                )
        self.text_account.grid(row= 0, column= 0)

        self.entry_account = ttk.Entry(self.box_settings)
        self.entry_account.grid(row= 1, column= 0)

        self.frame_balance_buttons2 = ttk.LabelFrame(self.box_settings)
        self.frame_balance_buttons2.grid(row = 2, column=0)

        self.bt_changue_account = ttk.Button(self.frame_balance_buttons2, 
                                            command= self.changeTypeAccount,
                                            text= "CONFIRM")
        self.bt_changue_account.grid(row = 0, column= 0)

    # metodo de deposito no banco
    def depositAccount(self):
        self.desposit_balance = self.entry_balance.get()
        # print(self.id)
        self.deposit = f""" UPDATE usuarios
                            SET balance = balance + {self.desposit_balance}
                            WHERE id_account = {self.id}"""

        self.cursor.execute(self.deposit)
        self.cursor.commit()
        self.show_account_update()
    #metodo de saque do banco
    def draftAccount(self):
        self.draft_balance = self.entry_balance.get()
        # print(self.id)
        self.deposit = f"""DECLARE @VAL INT
                            SELECT 
                            @VAL =  balance 
                            FROM usuarios
                            WHERE id_account = {self.id};
                            
                            IF @VAL < {self.draft_balance}
                                SELECT 'ERROR';
                            ELSE 
                                UPDATE usuarios
                                SET balance = balance - {self.draft_balance}
                                WHERE id_account = {self.id};"""

        self.cursor.execute(self.deposit)
        self.cursor.commit()
        self.show_account_update()

    def changeTypeAccount(self):
        self.new_type =  self.entry_account.get().upper()
        if self.new_type == "CORRENTE":
            self.cursor.execute(f"""UPDATE usuarios
                                SET type_account = 'C'
                                WHERE id_account = {self.id}""")
            self.cursor.commit()
            self.show_account_update()

        elif self.new_type == "POUPANCA":
            self.cursor.execute(f"""UPDATE usuarios
                                SET type_account = 'P'
                                WHERE id_account = {self.id}""")
            self.cursor.commit()
            self.show_account_update()
        else:
            print("Tipo de conta inexistente!")

        
    #------------------------------------------------------------------------------------------------------

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
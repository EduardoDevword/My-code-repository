from ast import main
import tkinter as tk
from tkinter import Frame, Label, StringVar, ttk
from tkinter.font import NORMAL
from ttkthemes import ThemedStyle
import sv_ttk
import pyodbc 
import pandas as pd
from tkinter import messagebox

class Win(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.login()
        # self.widgets()

    def conection(self): # Aqui criamos a conecão com o banco de dados 
        try:
            self.conection_database = (
                "Driver={SQL Server};"
                "Server=DESKTOP-8NMB5UJ;" # DESKTOP servidor de casa / DESKTOP-8NMB5UJ servidor curso
                "Database=accounts;"
            )

            self.conect = pyodbc.connect(self.conection_database)
            print("Sucess")

            self.cursor =  self.conect.cursor()
        except:
            messagebox.showerror("ERROR CONECTION", "Erro na tentativa de conexão ao banco, reinicie o app")

    
    def login(self):
        self.conection()
        # criando frames para organizacao dos programas
        #--------------------------------------------------
        #frame central onde sera posto todas as janelas de conteudos
        self.account_id = f"""
        SELECT id_account FROM usuarios
        ;"""

        self.consult = pd.read_sql_query(self.account_id, self.conect)
        # E aqui colocamos numa lista de consulta para acessalos para a edição 
        
        self.valores = ['']
        for index ,self.clients in self.consult.iterrows():
            self.valores.append(self.clients.id_account)
        
        self.img = tk.PhotoImage(file= "logo_banco.png")

        self.main_frame = ttk.LabelFrame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.img_logo = ttk.Label(self.main_frame, image= self.img, background="#414141" )
        self.img_logo.pack(pady= 30)

        self.user_label = ttk.Label(self.main_frame, text="User Name")
        self.user_label.pack()

        self.entry_username = ttk.Entry(self.main_frame, width= 50)
        self.entry_username.pack()

        self.accounts_label = ttk.Label(self.main_frame, text="Nº da conta")
        self.accounts_label.pack(pady=20)

        self.combo_conta = ttk.Combobox(self.main_frame, values= self.valores)
        self.combo_conta.pack(pady=20)

        self.password_label = ttk.Label(self.main_frame, text="Password")
        self.password_label.pack()

        self.entry_password = ttk.Entry(self.main_frame, width= 50, show="*")
        self.entry_password.pack()

        self.login_button = ttk.Button(self.main_frame, text="Login", command=self.check_login)
        self.login_button.pack(pady=30)

    #metodo que ira fazer a verificacao do gerente para tentar acessar as contas
    def check_login(self):
        self.login_username = self.entry_username.get()
        self.login_password = int(self.entry_password.get())
        self.id = int(self.combo_conta.get())

        self.manager_consult = f""" SELECT 
                                    name_manager,
                                    manager_user,
                                    manager_password 
                                    FROM managesrs"""

        self.manager_result = pd.read_sql_query(self.manager_consult, self.conect)

        for index ,self.manager_dados in self.manager_result.iterrows():
            if int(self.manager_dados.manager_password) == self.login_password and self.manager_dados.manager_user  == self.login_username:
                self.main_frame.destroy()
                self.widgets()
            else:
               tk.messagebox.showerror("[ERROR] Login error", "Incorrect username or password! Try again later.")


    def show_account(self):
        #metodo para acessar os valores do banco 
        self.columns = ('ACCOUNT', 'NAME','TYPE','BALANCE', 'STATUS')

        self.tree = ttk.Treeview(self.second_frame, columns= self.columns, show='headings', height= 3)

        # ajustando o tamanho das colunas da treeview
        self.tree.column('ACCOUNT', width= 90)
        self.tree.column('NAME', width= 110 )
        self.tree.column('TYPE', width= 70)
        self.tree.column('BALANCE', width= 100)
        self.tree.column('STATUS', width= 70)

        self.tree.heading('ACCOUNT', text='ACCOUNT')
        self.tree.heading('NAME', text='NAME')
        self.tree.heading('TYPE', text='TYPE')
        self.tree.heading('BALANCE', text='BALANCE')
        self.tree.heading('STATUS', text='STATUS')

        consult = f"""
                SELECT * FROM usuarios
                WHERE id_account = {self.id};"""

        usuario = pd.read_sql_query(consult, self.conect)

        for index, columns in usuario.iterrows():
            account = columns.id_account
            name = columns["name"]
            type_account = columns.type_account
            balance = columns.balance
            status_accounts = columns.status_account
            dados = [account, name, type_account, balance, status_accounts]
            self.tree.insert("", tk.END, values= dados)

        self.tree.grid(row= 0, column= 0,)
    

    def widgets(self):
        self.central_frame = ttk.Frame(self)
        self.central_frame.pack()
        
        #frame principal para manipulacao dos demais itens
        self.first_frame = ttk.Frame(self.central_frame)
        self.first_frame.grid(row= 0 , column= 0)

        #frame para os conteudos dos botoes

        #frame para a parte de baixo  do nosso programa 
        self.second_frame = ttk.Frame(self.central_frame)
        self.second_frame.grid(row= 1, column= 0)
        #--------------------------------------------------

        self.framebuttonsDown = ttk.Frame(self.central_frame)
        self.framebuttonsDown.grid(row = 2, column= 0,)
        #ajustando a janela de informacoes 
        self.second_frame.grid(row= 1, column= 0, sticky="W", pady= 5, padx= 10)

        self.b1 = ttk.Button(self.framebuttonsDown,
                        command= self.balanceMovement, 
                        text="DEPOSIT / WITHDRAW",
                        width=25,
                        state= tk.NORMAL)
        self.b1.grid(row= 0, column=0) 

        self.b2 = ttk.Button(self.framebuttonsDown,
                        command= self.changeAccount,
                        text="CHANGE ACCOUNT TYPE",
                        width=25,
                        state= tk.NORMAL)
        self.b2.grid(row= 1, column= 0) 

        self.b3= ttk.Button(self.framebuttonsDown,
                        command = self.changeStatusAccount,
                        text="CHANGE ACCOUNT STATUS",
                        width=25,
                        state= tk.NORMAL)
        self.b3.grid(row= 2, column= 0)

        self.b4 = ttk.Button(self.framebuttonsDown,
                        command= self.deleteAccount,
                        text="DELETE ACCOUNT",
                        width=25,
                        state= tk.NORMAL)
        self.b4.grid(row= 3, column= 0)

        self.b5 = ttk.Button(self.framebuttonsDown,
                                command= self.newAccount,
                                text="NEW ACCOUNT",
                                width=25,
                                state= tk.NORMAL)
        self.b5.grid(row=4, column=0)

        self.b6 = ttk.Button(self.framebuttonsDown,
                        command= self.finishEdit,
                        text="FINISH EDITION",
                        width=25,
                        state= tk.NORMAL)
        self.b6.grid(row= 5, column= 0)

        self.show_account()

    #Aqui fica o metodo de criacao de uma nova conta 
    #------------------------------------------------------------------------------------------------------    
    def newAccount(self):

        self.type_create = tk.StringVar()

        self.frame_create_account_name = ttk.LabelFrame(self.central_frame)
        self.frame_create_account_name.grid(row = 3, column= 0, sticky="NW")

        self.frame_create_account_buttons = ttk.LabelFrame(self.central_frame)
        self.frame_create_account_buttons.grid(row = 3, column= 0, sticky= "NE")

        self.confirm_create = ttk.LabelFrame(self.central_frame)
        self.confirm_create.grid(row = 4, column= 0)

        self.nome = ttk.Label(self.frame_create_account_name, text= "Nome completo*")
        self.nome.grid(row= 0, column=0, sticky="NW")

        self.entry_create_name = ttk.Entry(self.frame_create_account_name, width= 50)
        self.entry_create_name.grid(row = 1, column = 0)

        self.tipo_conta = ttk.Label(self.frame_create_account_buttons, text= "Tipos de conta*")
        self.tipo_conta.grid(row= 0, column=0, sticky= "NW")

        self.corrente_button = ttk.Radiobutton(self.frame_create_account_buttons, 
                                                text=" Corrente", 
                                                variable=self.type_create, 
                                                value= "C")
        self.corrente_button.grid(row = 1, column= 0)

        self.poupanca_button = ttk.Radiobutton(self.frame_create_account_buttons, 
                                                text="Poupança", 
                                                variable=self.type_create, 
                                                value= "P")
        self.poupanca_button.grid(row = 1, column= 1)

        self.confirm_create_button = ttk.Button(self.confirm_create, text= "CREATE", command=self.insertNewAccount)
        self.confirm_create_button.grid(row = 0, column = 0)

    def insertNewAccount(self):
        self.name_insert = self.entry_create_name.get()
        self.type_account_create = self.type_create.get()
        self.createte_cpf

        self.insert_new_account =f"""INSERT INTO usuarios (name, type_account, balance, status_account) VALUES ( '{self.name_insert}','{self.type_account_create}', 0.00, 'On', {self.create_cpf}); """

        self.cursor.execute(self.insert_new_account)
        self.cursor.commit()

        self.frame_create_account_name.destroy()
        self.frame_create_account_buttons.destroy()
        self.confirm_create.destroy()

        self.lb.delete(0,tk.END)

        self.account_id = f"""
        SELECT id_account FROM usuarios
        ;"""
        self.consult = self.cursor.execute(self.account_id)
        # E aqui colocamos numa lista de consulta para acessalos para a edição 
        for index ,self.clients in self.consult.iterrows():
            self.lb.insert(tk.END ,f"{self.clients.id_account}.CONTA")
            
        self.show_account()
    #------------------------------------------------------------------------------------------------------
    #Aqui criamos os metodos dos botoes de baixo
    #------------------------------------------------------------------------------------------------------
    def balanceMovement(self):
        self.b2.config(state= tk.DISABLED)
        self.b3.config(state= tk.DISABLED)
        self.b4.config(state= tk.DISABLED)
        self.b5.config(state= tk.DISABLED)
        self.b6.config(state= tk.DISABLED)


        self.box_settings = ttk.Frame(self.central_frame)
        self.box_settings.grid(row = 3, column= 0, pady= 45)

        self.frame_balance_buttons = ttk.Frame(self.box_settings)
        self.frame_balance_buttons.grid(row = 2, column=0, sticky= 'W')

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

        self.box_settings = ttk.LabelFrame(self.central_frame)
        self.box_settings.grid(row= 2, column= 0, sticky= 'NE')

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
        self.deposit = f""" UPDATE usuarios
                            SET balance = balance + {self.desposit_balance}
                            WHERE id_account = {self.id}"""

        self.cursor.execute(self.deposit)
        self.cursor.commit()
        self.show_account()
        self.box_settings.destroy()
        self.b2.config(state= tk.NORMAL)
        self.b3.config(state= tk.NORMAL)
        self.b4.config(state= tk.NORMAL)
        self.b5.config(state= tk.NORMAL)
        self.b6.config(state= tk.NORMAL)
        self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NS')
        
    
    #metodo de saque do banco
    def draftAccount(self):
      
        self.draft_balance = self.entry_balance.get()

        self.consult_balance = f""" SELECT 
                                balance 
                                FROM usuarios
                                WHERE id_account = {self.id};"""

        self.result_consult_balance = pd.read_sql_query(self.consult_balance, self.conect)
        
        for index ,balance_client in self.result_consult_balance.iterrows():
            if int(balance_client.balance) < int(self.draft_balance):
               tk.messagebox.showerror("Bank transaction error", "The amount requested for the withdrawal is higher than what is in the account. Check the amount you want or contact your manager")

            else:
                self.draft = f"""
                                UPDATE usuarios
                                SET balance = balance - {self.draft_balance}
                                WHERE id_account = {self.id};"""
                self.cursor.execute(self.draft)
                self.cursor.commit()
                
        self.show_account()
        self.box_settings.destroy()
        self.b2.config(state= tk.NORMAL)
        self.b3.config(state= tk.NORMAL)
        self.b4.config(state= tk.NORMAL)
        self.b5.config(state= tk.NORMAL)
        self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NS')
    
    def changeTypeAccount(self):


        self.new_type =  self.entry_account.get().upper()
        if self.new_type == "CORRENTE":
            self.cursor.execute(f"""UPDATE usuarios
                                SET type_account = 'C'
                                WHERE id_account = {self.id}""")
            self.cursor.commit()
            self.show_account()
            self.box_settings.destroy()
            self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NS')
            

        elif self.new_type == "POUPANCA":
            self.cursor.execute(f"""UPDATE usuarios
                                SET type_account = 'P'
                                WHERE id_account = {self.id}""")
            self.cursor.commit()
            self.show_account()
            self.box_settings.destroy()
            self.framebuttonsDown.grid(row = 2, column= 0, sticky= 'NS')
        else:
            tk.messagebox.showerror("Error type account", "Non-existent account type")

    def changeStatusAccount(self):
        self.new_status = f"""DECLARE @STATUS VARCHAR(3)
                                SELECT 
                                    @STATUS = status_account
                                FROM usuarios
                                WHERE id_account = {self.id}
                                IF @STATUS = 'On'
                                    UPDATE usuarios
                                    SET status_account = 'Off'
                                    WHERE id_account = {self.id};
                                ELSE 
                                    UPDATE usuarios
                                    SET status_account = 'On'
                                    WHERE id_account = {self.id};"""
        self.cursor.execute(self.new_status)
        self.cursor.commit()
        self.show_account()

    def deleteAccount(self):
        self.delete =f"""DECLARE @CON_DELETE VARCHAR(3)
                        SELECT 
                            @CON_DELETE = status_account
                        FROM usuarios
                        WHERE id_account = {self.id}
                        IF @CON_DELETE = 'Off'
                            DELETE FROM usuarios
                            WHERE id_account = {self.id}
                        """
        self.cursor.execute(self.delete)
        self.cursor.commit()

        self.lb.delete(0,tk.END)

        self.account_id = f"""
        SELECT id_account FROM usuarios
        ;"""
        self.consult = self.cursor.execute(self.account_id)
        # E aqui colocamos numa lista de consulta para acessalos para a edição 
        for self.clients in self.consult:
            self.lb.insert(tk.END ,f"{self.clients}.CONTA")
        self.show_account()

    def finishEdit(self):
        self.bs.config(state= tk.NORMAL)
        self.framebuttonsDown.destroy()
        self.box_settings.destroy()
        self.show_account()

    #------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    # root2 =tk.Tk()
    root.title('BANCO IO 1.0')
    root.geometry("400x600")
    root.iconphoto  
    # Simply set the theme
    style = ThemedStyle(root)
    style.set_theme('equilux')
    app = Win(root)
    app.pack(fill="both", expand=True)
    # root2.mainloop()
    root.mainloop()
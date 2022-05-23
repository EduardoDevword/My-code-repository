from tkinter import *
from tkinter import messagebox
class Root:
    def _init_(self):
        self.account = {
            "1":
                {
                    "numConta" : "1",
                    "tipo" : "C",
                    "dono" : "LUCAS DUARTE",
                    "saldo" : 70000,
                    "status" : "On"
                },
            "2":
                {
                    "numConta" : "2",
                    "tipo" : "P",
                    "dono" : "ARTHUR RIBEIRO",
                    "saldo" : 400,
                    "status" : "On"
                },
            "3":
                {
                    "numConta" : "3",
                    "tipo" : "C",
                    "dono" : "EDUARDO MARMENTINI",
                    "saldo" : 450,
                    "status" : "On"
                },
        }

        self.root = Tk()
        self.root.title("BANCO IO")
        self.root.geometry("500x500")
        self.root.config(bg= "#A5A692")

        self.show = StringVar()

        self.lb = Listbox(self.root, relief = SUNKEN)

        for a in self.account:
            self.lb.insert(END,f"{a}.CONTA")

        self.lb.pack()
        
        self.bt = Button(self.root,
                        command=self.select,
                        text="SELECT")
        self.bt.place(x = 220, y = 200)

        self.root.mainloop()

    def select(self):   # Esse metodo apenas pega a conta selecionada e imprime na tela do usuario
        i =str(self.lb.get(self.lb.curselection())[:1])
        self.nConta = self.account[i]["numConta"]
        self.type = self.account[i]["tipo"]
        self.name = self.account[i]["dono"]
        self.val = self.account[i]["saldo"]
        self.status = self.account[i]["status"]

        self.msg = f"""
        Nº DA CONTA : {self.nConta} \n
        DONATARIO : {self.name} \n
        TIPO DA CONTA : {self.type} \n
        SALDO ATUAL : R$ {self.val}.00 \n
        STATUS DA CONTA : {self.status}"""

        self.show.set(self.msg)

        self.lab = Label(self.root,
                        textvariable = self.show,
                        background= "white",
                        relief = SUNKEN )
        self.lab.place(x = 129, y = 280)

        self.creat = Button(self.root,
                        text="NEW ACCOUNT")
        self.creat.place(x = 5,y = 200)

        self.ed = Button(self.root,
                         command = self.edit,
                         text = "EDIT ACCOUNT" 
                         )
        self.ed.place(x = 400 , y = 200 )
        

    def deleteAccount(self):
        if self.val > 0:
            msg = messagebox.askquestion("AVISO!","Você esta tentando deletar uma conta que contem um saldo em sua conta. Deseja mesmo realizar essa operação?", icon = 'warning')
            if msg == 'yes':
                d = self.lb.curselection()
                self.lb.delete(d)
                #aqui por questoesesteticas os botoes seram excluidos mas surgiram depois de ser chamada a função edit ou select
                self.lab.destroy()
                self.b1.destroy()
                self.b2.destroy()
                self.b3.destroy()
                self.b4.destroy()
                self.b5.destroy()
                self.ed.destroy()
                
    
    def edit(self):
        self.lab.place(x = 10 , y = 280) # Apenas ajusta a janela da conta para o lado 
        self.creat.destroy()
        #Criando os botoes de edicao do usuario 
        self.b1 = Button(self.root,
                        command= self.balanceMovement,
                        text="DEPOSITAR / SACAR",
                        width=22)
        self.b1.place(x = 280, y = 280 )

        self.b2 = Button(self.root,
                        command= self.changeAccount,
                        text="MUDAR TIPO DE CONTA",
                        width=22)
        self.b2.place(x = 280, y = 305 )

        self.b3= Button(self.root,
                        command=self.changeStatus,
                        text="MUDAR STATUS DA CONTA",
                        width=22)
        self.b3.place(x = 280, y = 330)

        self.b4 = Button(self.root,
                        command= self.deleteAccount,
                        text="DELETE ACCOUNT",
                        width=22)
        self.b4.place(x = 280, y = 355)

        self.b5 = Button(self.root,
                        command= self.finish,
                        text="FINISH EDITION",
                        width=22)
        self.b5.place(x = 280, y = 380)

    def balanceMovement(self):
        #config nova janela 
        self.new_root = Toplevel()
        self.new_root.title("OPERAÇÃO")
        self.new_root.geometry("240x200")
        #criando todos os componentes da segunda janela 

        self.text = Label(self.new_root,
                         text="Insira a seguir o valor e escolha a operação")
        self.text.pack()

        self.lb2 = Label(self.new_root,
                        text="R$")
        self.lb2.place(x = 33, y = 20)

        self.entry = Entry(self.new_root,)
        self.entry.place(x = 50, y = 20)

        self.dp = Button(self.new_root,
                        command= self.deposit,
                        text="DEPOSITAR",
                        width= 10)
        self.dp.place(x = 30, y = 70)

        self.sq= Button(self.new_root,
                        command=self.draft,
                        text="SAQUE",
                        width= 10)
        self.sq.place(x = 115, y = 70)

    def deposit(self):
        balcance = int(self.entry.get())

        self.val += balcance
        self.updateAccount()
        self.new_root.destroy() #destroy ira fechar a janela apos terminar o processo

    def draft(self):
        balcance = int(self.entry.get())
        if balcance > self.val:
            messagebox.showerror("Aviso de valor excedido", "Valor de saque superior ao que se tem disponível em sua conta.")
        else:
            self.val -= balcance
            self.updateAccount()
            self.new_root.destroy()
            

    def changeStatus(self):
        if self.status == "Off":
            self.status = "On"
            self.updateAccount()
        else:
            self.status = "Off"
            self.updateAccount()

    def changeAccount(self):
        #criando janela para a troca de tipo de conta
        self.change = Toplevel()
        self.change.title("MUDANÇA DE CONTA")
        self.change.geometry("400x70")

        self.text2 = Label(self.change,
                          text="Para qual conta o usuario deseja mudar? [Corrente/Poupança]")
        self.text2.pack()

        self.entry2 = Entry(self.change)
        self.entry2.pack()

        self.conf = Button(self.change,
                           command=self.confir,
                           text="CONFIRMAR")
        self.conf.pack()
            
    def confir(self):
        choice = self.entry2.get().upper()

        if choice == "CORRENTE":
            self.type = "C"
            self.updateAccount()
            self.change.destroy()
        else:
            self.type = "P"
            self.updateAccount()
            self.change.destroy()


    def finish(self):
        fim = messagebox.askquestion("FINISH EDITION","Você esta pronto para finalizara modificação daconta?", icon = 'question')
        if fim == "yes":
            self.lab.destroy()
            self.b1.destroy()
            self.b2.destroy()
            self.b3.destroy()
            self.b4.destroy()
            self.b5.destroy()
            self.ed.destroy()
            self.creat.destroy()
                
    def updateAccount(self):

        self.msg = f"""
        Nº DA CONTA : {self.nConta} \n
        DONATARIO : {self.name} \n
        TIPO DA CONTA : {self.type} \n
        SALDO ATUAL : R$ {self.val}.00 \n
        STATUS DA CONTA : {self.status}"""

        self.show.set(self.msg)       
Root()
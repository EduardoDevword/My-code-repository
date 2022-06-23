from tkinter import *
from random import randint

class Game:
    def __init__(self):
        self.enemy_x = randint(0, 250)
        self.enemy_y = randint(0, 250)
        self.placar =  0
        self.balas = 5
        self.minutos = "01"
        self.segundos = "00"
        
        #aqui chama amea tela inicial do g
        self.home_screen()

    #cria a tela de inicio do game
    def home_screen(self):
        self.root1 = Tk()
        self.root1.geometry("800x503")
        self.root1.title("DUCK-GAME.BETA")

        self.back = PhotoImage(file = "fundo2.png") 
        self.enemy_image = PhotoImage(file = "enemy.png")
        self.logo = PhotoImage(file = "logo_game_duck.png")
        
        self.fundo = Canvas(self.root1, width = 800, height = 500)

        self.fundo.place(x = 0, y = 0)
        self.fundo.create_image(0, 0, anchor = NW, image = self.back)

        #criando a logo do jogo
        self.logo_image = self.fundo.create_image(300, 100, anchor = NW, image = self.logo)

        #criano o bottao que vai dar inicio ao jogo
        self.play = Button(self.root1, 
                            text= "PLAY", 
                            background= "#6C63A6", 
                            width= 20, 
                            command= self.star)
        self.play.place(x = 320, y = 350)
        
        self.root1.mainloop()

    def star(self):
        self.root1.destroy()
        #aqui se da inicio ao game
        self.start_game()
        
    def sort_enemy_position(self):
        self.enemy_x = randint(0, 250)
        self.enemy_y = randint(0, 250)
        self.enemy = self.fundo.create_image(self.enemy_x, self.enemy_y, anchor = NW, image = self.enemy_image)

    #e aqui se muda a imagem do pato ao acertar
    #-----------------------------------------------------
    def changue_image1(self):
        self.fundo.delete(self.enemy)
        self.enemy_dead = self.fundo.create_image(self.enemy_x, self.enemy_y, anchor = NW, image = self.enemy_die_image)
        self.root.after(100, self.changue_image2)

    def changue_image2(self):
        self.fundo.delete(self.enemy_dead)
    #-----------------------------------------------------

    #esses tres def servem para fazer a mudanca no label quando a municao acaba
    #-----------------------------------------------------
    def changue_text1(self):
        self.municao.config( text= "RELOADING...")
        self.municao.after(3000, self.changue_text2)
        
    def changue_text2(self):
        self.municao.config( text= "FULL RECHARGE!")
        self.municao.after(1000, self.changue_text3)

    def changue_text3(self):
        self.balas = 5
        self.municao.config(text = f"BULLETS: {self.balas}/5")
    #-----------------------------------------------------

     #defs para fazer a reducao do tempo do game
    #-----------------------------------------------------
    def times_update1(self):
        self.stopwatch.config(text = f"TIME: {self.minutos}:{self.segundos}")
        self.root.after(1000, self.times_update2)
        
    def times_update2(self):
        self.minutos = "00"
        self.segundos = 59
        self.stopwatch.config(text = f"TIME: {self.minutos}:{self.segundos}")
        self.root.after(1000, self.times_update3)

    def times_update3(self):
        self.segundos -= 1
        if self.segundos <= 10:
            self.stopwatch.config(text = f"TIME: {self.minutos}:0{self.segundos}")
        else:
            self.stopwatch.config(text = f"TIME: {self.minutos}:{self.segundos}")
        self.root.after(1000, self.times_update3)
    #-----------------------------------------------------

    def start_game(self):
        self.root = Tk()
        self.root.geometry("800x503")
        self.root.title("DUCK-GAME.BETA")
        self.root.config(cursor="cross")
    
        # aqui é setado a todas as imagens dos personagens e no fundo 
        self.back = PhotoImage(file ="fundo2.png") 
        self.enemy_image = PhotoImage(file = "enemy.png")
        self.enemy_die_image = PhotoImage(file = "enemy_die.png")
        self.icon = PhotoImage(file = "logo_game_duck.png")
        self.root.iconphoto(False, self.icon)

        #Fundo do programa 
        self.fundo = Canvas(self.root, width = 800, height = 500,)
        self.fundo.place(x = 0, y = 0)
        self.fundo.create_image(0, 0, anchor = NW, image = self.back)

        # #Criando o alvo
        self.enemy = self.fundo.create_image(self.enemy_x, self.enemy_y, anchor = NW, image = self.enemy_image)

        #painel de croonometro 
        self.stopwatch = Label(self.fundo, 
                                text = f"TIME: {self.minutos}:{self.segundos}", 
                                font= ("Courier",20), 
                                background= "#03B0D8")
        self.stopwatch.place(x = 618, y = 2)

        #criando o placar
        self.score = Label(self.fundo, text= "SCORE:0", background= "#03B0D8", font= "20")
        self.score.place(x = 2, y = 2)

        #Painel de contagem de balas # cor terra #6F3C1F #cor grama #06BE10
        self.municao = Label(self.fundo, text = f"BULLETS:{self.balas}/5", background= "#6F3C1F", font= "20")
        self.municao.place(x = 0, y = 470)


        #dando acesso ao botao de atirar no game 
        self.root.bind("<Button-1>", self.shot)
        #metodo para mudança do cronometro duranre o jogo
        self.times_update1()
        
        self.root.mainloop()

    # verifica o acerto ao pato
    def enemy_hit(self):
        if self.shot_x > self.enemy_x and self.shot_x < self.enemy_x + 70:
            self.changue_image1()
            if self.balas > 0:
                self.placar += 1
            else:
                self.placar += 0
            self.score.config(text = f"SCORE: {self.placar}")
            self.balas -= 1
            if self.balas <= 0:
                self.changue_text1()
            else:
                self.municao.config(text = f"BULLETS: {self.balas}/5")
            self.sort_enemy_position()
        else:
            self.balas -= 1
            self.fundo.delete(self.enemy)
            self.sort_enemy_position()
            if self.balas <= 0:
                self.changue_text1()
            else:
                self.municao.config(text = f"BULLETS: {self.balas}/5")

    def shot(self, event):
        self.shot_x = event.x
        self.shot_y = event.y
        self.enemy_hit()

Game()
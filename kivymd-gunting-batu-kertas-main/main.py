from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang.builder import Builder
import random



class Pilih(MDScreen):

    score_computer = 0
    score_player = 0
    keterangan = "none"

    def generate(self):
        pilihan = ("gunting", "batu", "kertas")
        pilihan_com = random.choice(pilihan)
        return pilihan_com

    def score(self,com,player):
        self.keterangan = ""

        if com == player:
            self.keterangan = "Seri"
        elif com == "gunting":
            if player == "batu":
                self.score_player = self.score_player + 1
                self.keterangan = "Anda menang"
            elif player == "kertas":
                self.score_computer = self.score_computer + 1
                self.keterangan = "Anda kalah"
        elif com == "batu":
            if player == "kertas":
                self.score_player = self.score_player + 1
                self.keterangan = "Anda menang"
            elif player == "gunting":
                self.score_computer = self.score_computer + 1
                self.keterangan = "Anda kalah"
        elif com == "kertas":
            if player == "gunting":
                self.score_player = self.score_player + 1
                self.keterangan="Anda menang"
            elif player == "batu":
                self.score_computer = self.score_computer + 1 
                self.keterangan="Anda kalah"

    def click(self,pilihan_player):
        data = {"gunting":"data/scissors.png","batu":"data/fist.png","kertas":"data/hand-paper.png"}

        pilihan_com = self.generate()
        self.score(pilihan_com,pilihan_player)
        img_player = data[pilihan_player]
        img_com = data[pilihan_com]

        hasil = self.manager.get_screen("hasil")

        hasil.ids.ket.text = self.keterangan
        hasil.ids.com_score.text = str(self.score_computer)
        hasil.ids.player_score.text = str(self.score_player)
        hasil.ids.img_com.source = img_com
        hasil.ids.img_player.source = img_player

        self.manager.current = "hasil"


class Hasil(MDScreen):
    pass

    

class Home(MDScreen):
    pass

class MyApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")
        

if __name__=="__main__":
    MyApp().run()
from teste1.atributos_personagem import *


class Inimigo(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 1
        self.constituicao = 1
        self.destreza = 1
        self.agilidade = 1
        self.inteligencia = 1
        self.forca_de_vontade = 1
        self.percepcao = 1
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 6)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 3)

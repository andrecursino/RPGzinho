from teste1.atributos_personagem import *


class Cacador(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 1
        self.constituicao = 1
        self.destreza = 2
        self.agilidade = 1
        self.inteligencia = 1
        self.forca_de_vontade = 1
        self.percepcao = 2
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 10)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 5)


class Campeao(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 2
        self.constituicao = 2
        self.destreza = 1
        self.agilidade = 1
        self.inteligencia = 1
        self.forca_de_vontade = 1
        self.percepcao = 1
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 12)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 5)


class Guerreiro(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 2
        self.constituicao = 1
        self.destreza = 1
        self.agilidade = 1
        self.inteligencia = 1
        self.forca_de_vontade = 2
        self.percepcao = 1
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 12)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 5)


class Ladino(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 1
        self.constituicao = 1
        self.destreza = 2
        self.agilidade = 2
        self.inteligencia = 1
        self.forca_de_vontade = 1
        self.percepcao = 1
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 8)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 5)


class Mago(AtributosPersonagem):
    def __init__(self):
        super().__init__(self, self, self, self, self, self, self, self)
        self.forca = 1
        self.constituicao = 1
        self.destreza = 1
        self.agilidade = 1
        self.inteligencia = 2
        self.forca_de_vontade = 2
        self.percepcao = 1
        self.carisma = 1
        self.hp = AtributosPersonagem.pontos_de_vida(self, 8)
        self.mp = AtributosPersonagem.pontos_de_magia(self, 10)

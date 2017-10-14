class AtributosPersonagem:
    def __init__(self, forca, constituicao, destreza, agilidade, inteligencia, forca_de_vontade,
                 percepcao, carisma):
        self.__forca = forca
        self.__constituicao = constituicao
        self.__destreza = destreza
        self.__agilidade = agilidade
        self.__inteligencia = inteligencia
        self.__forca_de_vontade = forca_de_vontade
        self.__percepcao = percepcao
        self.__carisma = carisma

    def pontos_de_vida(self, pontos_de_vida):
        pontos_de_vida = (self.constituicao * 2) + pontos_de_vida
        return pontos_de_vida

    def pontos_de_magia(self, pontos_de_magia):
        pontos_de_magia = self.inteligencia + pontos_de_magia
        return pontos_de_magia

    def ataque(self):
        atk = self.forca + self.destreza
        return atk

    def defesa(self):
        df = self.agilidade + self.carisma
        return df

    @property
    def forca(self):
        return self.__forca

    @forca.setter
    def forca(self, forca):
        self.__forca = forca

    @property
    def constituicao(self):
        return self.__constituicao

    @constituicao.setter
    def constituicao(self, constituicao):
        self.__constituicao = constituicao

    @property
    def destreza(self):
        return self.__destreza

    @destreza.setter
    def destreza(self, destreza):
        self.__destreza = destreza

    @property
    def agilidade(self):
        return self.__agilidade

    @agilidade.setter
    def agilidade(self, agilidade):
        self.__agilidade = agilidade

    @property
    def inteligencia(self):
        return self.__inteligencia

    @inteligencia.setter
    def inteligencia(self, inteligencia):
        self.__inteligencia = inteligencia

    @property
    def forca_de_vontade(self):
        return self.__forca_de_vontade

    @forca_de_vontade.setter
    def forca_de_vontade(self, forca_de_vontade):
        self.__forca_de_vontade = forca_de_vontade

    @property
    def percepcao(self):
        return self.__percepcao

    @percepcao.setter
    def percepcao(self, percepcao):
        self.__percepcao = percepcao

    @property
    def carisma(self):
        return self.__carisma

    @carisma.setter
    def carisma(self, carisma):
        self.__carisma = carisma
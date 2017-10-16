from teste1.classe_personagem import *
from teste1.inimigo import *
from teste1.escolhe_classe import *
from teste1.combate import *

heroi = escolhe_classe()
inimigo = Inimigo()

while heroi.hp > 0 or inimigo.hp > 0:

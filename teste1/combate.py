from teste1.classe_personagem import *
from teste1.inimigo import *
from teste1.main import *
def vez():
    vez = int(input('1-Atacar e 2-Defender: '))
    if vez == 1:
        dano = hero_pwr
        enemy_hp = enemy_hp - dano
        print('Você causou {} e o inimigo ainda tem {} HP.'.format(dano, enemy_hp))
    if vez == 2:
        guard = True
        print('Em defesa.')
def ataque():

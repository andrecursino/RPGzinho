from random import randint
hero_hp = int(15)
enemy_hp = int(15)
hero_pwr = int(4)
enemy_pwr = int(4)
defeat = False
guard = False

while hero_hp >= 0 and enemy_hp >= 0:
    guard = False
    vez = int(input('1-Atacar e 2-Defender: '))
    if vez == 1:
        dano = hero_pwr
        enemy_hp = enemy_hp - dano
        print('Você causou {} e o inimigo ainda tem {} HP.'.format(dano, enemy_hp))
    if vez == 2:
        guard = True
        print('Em defesa.')

    # vez do npc
    if guard == True:
        dano_inimigo = randint(1, enemy_pwr/2)
        hero_hp = hero_hp - dano_inimigo
        print('Defesa.\nO inimigo causou {} dano e vc tem {} HP.'.format(dano_inimigo, hero_hp))
    if guard == False:
        dano_inimigo = randint(1, enemy_pwr)
        hero_hp = hero_hp - dano_inimigo
        print('O inimigo causou {} dano e vc tem {} HP.'.format(dano_inimigo, hero_hp))

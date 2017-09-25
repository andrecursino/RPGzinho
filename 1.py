# utf-8

from random import randint

tentativa = 1
hero_hp = int(15) # vida
enemy_hp = int(15) # vida do inimigo
hero_pwr = int(4) # sua força
enemy_pwr = int(4) # força do inimigo

while tentativa <= 3:
    print('#' * 10)
    print('Essa é sua tentativa {}.'.format(tentativa))
    print('*' * 10)
    while hero_hp > 0 or enemy_hp > 0:
        print('Você tem {} de vida.'.format(hero_hp))
        print('O inimigo tem {} vida.'.format(enemy_hp))
        print('-' * 10)
        print('Sua vez:')
        hero_turn = int(input('Coloque "1" para atacar ou coloque "2" para defender: '))
        print('')
        if hero_turn == 1:
            hero_atk = randint(1, hero_pwr) # dano causado por você
            print('Você atacou o inimigo e causou {} de dano.'.format(hero_atk))
            print('')
            enemy_hp = enemy_hp - hero_atk
        if hero_turn == 2:
            print('Em posição de defesa')
            print('')
        print('-' * 10)
        print('Vez do inimigo.')
        print('')
        if hero_turn == 2:
            enemy_atk = int(enemy_pwr / 2)
            hero_hp = hero_hp - enemy_atk
            print('Devido a defesa o inimigo causou apenas {} do dano.'.format(enemy_atk))
            print('')
        else:
            enemy_atk = randint(1, enemy_pwr)
            hero_hp = hero_hp - enemy_atk
            print('O inimigo lhe causou {} de dano.'.format(enemy_atk))
            print('')
    if hero_hp < 0:
        tentativa = tentativa + 1
        hero_hp = int(15)
        enemy_hp = int(15)
        print('Você perdeu a luta, mas não a guerra.\n'
              'Você pode tentar de novo')
        print('')
    if enemy_hp < 0:
        hero_hp = int(15)
        enemy_hp = int(15)
        print('Você venceu essa luta.')
        try_again = int(input('Deseja ir mais uma luta?\n'
                              'Coloque "1" para sim e "2" para não: '))
        if try_again == 1:
            tentativa = tentativa
        if try_again == 2:
            break

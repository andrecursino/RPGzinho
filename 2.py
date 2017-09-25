# utf-8

import time
from random import randint

# variaveis

hero_pwr = 4
enemy_pwr = 4


def fight():
    hero_hp = 15
    enemy_hp = 15
    while hero_hp > 0 or enemy_hp > 0:
        damage_hero = hero_turn()
        if damage_hero == 1:
            print('Defesa')
        else:
            print('Você atacou e causou {} de dano ao inimigo.'.format(damage_hero))
            enemy_hp = enemy_hp - damage_hero
        if enemy_hp > 0:
            print('Ainda lhe resta {} HP'.format(enemy_hp))
            print('*' * 20)
            print('Vez do inimigo.')
            damage_enemy = enemy_turn(damage_hero)
            hero_hp = hero_hp - damage_enemy
            print('O inimigo lhe causou {} de dano.'.format(damage_enemy))
            print('Você ainda tem {} HP'.format(hero_hp))
            print('#' * 20)
        elif hero_hp <= 0:
            print('Voce perdeu.')
            break
        elif enemy_hp <= 0:
            print('Você ganhou.')
            break


def hero_turn():
    print('Sua vez, você deseja...')
    hero_choice = int(input('Atacar (digite 1) ou Defender (digite 2):'))
    print('-' * 20)
    if hero_choice == 1:
        hero_atk = randint(2, hero_pwr)
        return hero_atk
    if hero_choice == 2:
        time.sleep(1)
        print('Em posição de defesa')
        guard = 1
        return guard


def enemy_turn(damage_hero):
    if damage_hero == 1:
        enemy_atk = randint(1, enemy_pwr/2)
        return enemy_atk
    else:
        enemy_atk = randint(1, enemy_pwr)
        return enemy_atk


print(fight())
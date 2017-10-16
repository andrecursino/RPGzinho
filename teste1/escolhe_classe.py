from teste1.classe_personagem import *


def escolhe_classe():
    print('Escolha sua Classe de Heroi:')
    print('-' * 30)
    print('1 - Caçador/n2 - Campeão/n3 - Guerreiro/n4 - ladino/n5 - Mago')
    try:
        heroi = int(input('Qual: '))
        if heroi == 1:
            return Cacador()
        elif heroi == 2:
            return Campeao()
        elif heroi == 3:
            return Guerreiro()
        elif heroi == 4:
            return Ladino()
        elif heroi == 5:
            return Mago()
    except Exception:
        print('Escolha um número válido')
        print('#' * 30)
        print()
        escolhe_classe()


heroi = escolhe_classe()

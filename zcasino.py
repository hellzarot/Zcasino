#!/usr/local/bin/python3.10
import random

misededepart = int(input("combien comptes tu jouer ce soir ? "))
bourse = misededepart
while bourse > 0:
    mise= float(input("combien tu mises ?"))
    if mise <= bourse and mise >= 1:
        numero = 1
        if 1 <= numero <= 50:
            numero = int(input("tu mises quel numero ?"))
        else:
            print("tu dois miser entre 1 et 50")
        numroulette = random.randrange(50)
        print("le numero de la boule est le",numroulette)
        if (numroulette % 2) == 0:
            couleurroulette = "pair"
        else:
            couleurroulette = "impair"
        print("la boule est ",couleurroulette)

        if (numero % 2) == 0:
            couleurnumero = "pair"
        else:
            couleurnumero = "impair"


        if (numroulette == numero):
            bourse = bourse + 3*mise
        elif (couleurroulette ==couleurnumero):
            bourse = bourse - 0.5*mise
        else:
            bourse = bourse - mise
        print("ton numero est", couleurnumero)
        print("il te reste", bourse)
    else:
        print("tu as pas assez pour miser ça")

print("dehors tu as plus de fric")
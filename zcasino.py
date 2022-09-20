#!/usr/local/bin/python3.10
import random

misededepart = int(input("combien comptes tu jouer ce soir ? "))
bourse = misededepart
while misededepart > 0:
    mise= int(input("combien tu mises ?"))
    numero = int(input("tu mises quel numero ?"))
    numroulette = random.randrange(50)
    if (numroulette % 2) == 0:
        couleurroulette = "pair"
    else:
        couleurroulette = "impair"

    if (numero % 2) == 0:
        couleurnumero = "pair"
    else:
        couleurnumero = "impair"


    if (numroulette == numero):
        bourse = bourse + 3*mise
    elif (couleurroulette ==couleurnumero):
        bourse = bourse + 0.5*mise
    else:
        bourse = bourse - mise

print("dehors tu as plus de fric")
#!/usr/local/bin/python3.10

pht = float(input("prix HT : "))
while pht != 0:
    pht =float(pht)
    pttc = pht *1.20
    print(pttc)
    pht = float(input("prix HT : "))
print("fin du programme")

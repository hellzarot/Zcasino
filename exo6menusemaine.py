#!/usr/local/bin/python3.10
joursemaine= input("quel jour sommes nous ?: ")
if joursemaine == "lundi" or joursemaine =="mercredi" or joursemaine =="vendredi":
    print(joursemaine," ? tu vas manger des patates")
elif joursemaine == "mardi" or joursemaine =="jeudi":
    print(joursemaine, " ? tu vas manger de la purée")
elif joursemaine == "samedi" or joursemaine =="dimanche":
    print("aujourdhui c'est frites")
else:
    print("rentre chez toi roger pas de patates aujourdhui !")
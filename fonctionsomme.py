#!/usr/local/bin/python3.10

def somme(a,b):
    c=a+b
    print ("la somme de ", a, " + ", b, " = ",c)

a=float(input("veuillez rentrer le premier nombre "))
b=float(input("veuillez rentrer le second nombre "))

print(somme(a,b))
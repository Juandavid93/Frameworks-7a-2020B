#Script: Number race
'''
    Description:
    randint: Let me generate integer numbers
    uniform: Let me generate float numbers
'''
import os
from random import randint
#Functions:::::::::::::::::::::::::::::
def dices () :
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot = d1 + d2
    return [d1, d2, tot]

#Main::::::::::::::::::::::::::::::::::
os.system("cls")
i = 1

while i <= 10 :
    print("Tiro Nro: ", i)
    dd = dices()
    print("d1: ", dd[0])
    print("d2: ", dd[1])
    print("Total: ",dd[2])
    i = i + 1
    key = input("::: Lanzar nuevamente :::")
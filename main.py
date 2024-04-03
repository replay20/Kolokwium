import math
import random

def zad1():
    wynik = 0
    for x in range(30,61):
        dzialanie = (math.e ** (math.sin(x)) + math.log(32,3))**(1/4)
        wynik += dzialanie
    return round(wynik,2)

print(zad1())

def zad2(min,max,ile):
    lista = []
    if(max>min) & ile>0:
        for x in range(ile):
            lista.append(random.randint(min,max))
        print(lista)
    else:
        print("Podano nieprawidlowe wartosci")

    lista2=[]
    for y in range(len(lista)):
        for z in range(y+1,len(lista)):
            if lista[y] != lista[z]:
                lista2.append(abs(lista[y] - lista[z]))
    return(lista2)

print(zad2(1,10,5))

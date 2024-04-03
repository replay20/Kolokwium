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

def zad3(nazwa_pliku):
    plik = open(nazwa_pliku, "r")
    linie = plik.readlines()
#print(linie)
    pierwszaLinia = linie[0].split()
#print(pierwszaLinia)
    liczbaKolumn = len(pierwszaLinia)
#print(liczbaKolumn)
    suma=[0]*liczbaKolumn
#print(suma)
    for i in linie:
        liczby = i.split()
        for j in range(liczbaKolumn):
            suma[j]+= int(liczby[j])
    return suma

print(zad3("liczby.txt"))

def zad4(a,h):

    if(a>0) & (h>0):
        pole = (a*a*2) + (4*a*h)
        return pole
    else:
        return "Podano nieprawidlowe wartosci"

print(zad4(4,5))


def zad1a():
    wynik=0
    for x in range(14,33):
        dzialanie = ((x ** math.e) + math.cos(x)) ** (1/5)
        wynik += dzialanie
    return round(wynik,2)

print(zad1a())

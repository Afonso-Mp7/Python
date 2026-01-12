import random
lista = []

def sortear ():
    for x in range (10) :
        lista.append(random.randint(1, 20))
    print (lista)
    return lista

def soma (lista):
    somatorio = 0
    for a in lista:
        if a % 2 == 0:
            somatorio += a
    print (f'A soma dos números pares contidos na lista {lista} é {somatorio}.')

sortear()
soma (lista)
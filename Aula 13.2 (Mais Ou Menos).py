import random
b = random.randint (1, 100)
a = int(input("Escolhe um número de 1 a 100."))
c = 0
while a != b :
    if a < b :
        print("É maior.")
    elif a > b :
        print ("É menor.")
    c += 1
    a = int(input("Escolhe outro número."))
if a == b :
    print ("Acertaste!")
    print (f'Precisaste de {c} tentativas.')
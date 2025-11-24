x = int(input("Insere um número."))
par = impar = 0
while x!=0 :
    if x%2==0 :
        par += 1
        x = int(input("Insere outro número."))
    if x%2!=0 :
        impar += 1
        x = int(input("Insere outro número."))
print (f'Colocaste {par} números pares e {impar} números ímpares.')
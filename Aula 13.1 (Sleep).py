from time import sleep
c = int(input ("Escolhe um número para contagem regressiva do foguete."))
while c >= 1 :
    print (c)
    c -= 1
    sleep (1)
print ("DESCOLOU!")
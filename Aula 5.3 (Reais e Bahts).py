a = float(input("Quantos euros queres converter?"))
reais = 5.32*a
bahts = 31.10*a
x = input("Queres converter para reais ou bahts?")
if  x == "reais" :
    print(f'Tens "{reais}".')
else  :
    print (f'Tens" {bahts}".')


a = int(input("Qual é o salário mensal?"))
b = int(input("Qual é o preço da casa?"))
c = int(input("Quantos anos pretendes pagar a casa?"))
s = (a*0.3)
p = (b/(c*12))
if p<s:
    print("A prestação é inferior.")
else:
    print("A prestação é superior.")
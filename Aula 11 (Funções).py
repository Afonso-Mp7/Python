a = int(input("Insere um número."))
b = int(input("Insere outro número."))
c = int(input("Que operação farás? Adição=0, Subtração=1, Multiplicação=2, Divisão=3"))
def adicao ():
    calc = a + b
    print (calc)
def subtracao ():
    calc = a - b
    print (calc)
def multiplicacao ():
    calc = a * b
    print (calc)
def divisao ():
    calc = a / b
    print (calc)
list_numeros = [adicao,subtracao,multiplicacao,divisao]
if 0 <= c <= 3:
    funcao = list_numeros[c]
    funcao()
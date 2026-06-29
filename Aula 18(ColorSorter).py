a = input ("Verifica se uma palavra se encontra no ficheiro.")
with open('ColorSorter.txt', 'r', encoding = 'utf-8') as ficheiro :
    for linha in ficheiro :
        if a in linha :
            print(linha.rstrip())
        else :
            print("Não se encontra no ficheiro.")

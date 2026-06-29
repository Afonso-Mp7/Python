a = int(input("Digita 0 para sair, 1 para cadastrar e 2 para buscar."))
with open('dados.txt', 'a', encoding = 'utf-8') as ficheiro:
    if a == 0 :
        print ("Obrigado!")
    elif a == 1 :
        b = input("Qual é o teu nome?")
        c = int(input("Qual é a tua idade?"))
        ficheiro.write(b)
        ficheiro.write(str(c))
    elif a == 2 :
        d = input("Escreve o que pretendes buscar.")
        for linha in ficheiro:
            if d in linha:
                print (linha.rstrip())
    else :
        print ("Não está na base de dados.")
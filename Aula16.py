

def manipular_documentos():
    b = input("Se pretendes inserir uma frase, coloca 1, se pretendes criar um documento, coloca 2: ")
    a = input("Escreve o nome do ficheiro que pretendes manipular: ")

    if b == "1":
       
        c = input("O que pretendes escrever? ")

        with open(f'{a}.txt', 'a') as arquivo:
            arquivo.write(f'{c}\n')

    elif b == "2":
        o = input("Qual é o nome do documento? ")

        with open(f'{o}.txt', 'w') as arquivo:
            print("Ficheiro criado.")

    else:
        print("Opção inválida.")

manipular_documentos()
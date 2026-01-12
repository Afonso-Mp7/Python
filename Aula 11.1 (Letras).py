a = input("Entra com uma frase.")
b = input("Qual letra desejas verificar?")

def letra ():
    soma = 0
    for x in a:
        if x == b:
            soma += 1
    print(f'A frase repete a letra {b} {soma} vezes.')

letra ()
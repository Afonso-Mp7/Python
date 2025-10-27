m = input("Qual é a marca do teu carro?")
if m in "Ford, Chevrolet, Dodge.":
    print(f'"{m}"A marca é americana.')
elif m in "Honda, Toyota, Suzuki." :
    print(f'"{m}" é asiática.')
elif m in "BMW, Peugeot, Citroen." :
    print(f'"{m}"A marca é europeia.')
else :
    print("Peço desculpa, essa marca não está presente na nossa base de dados.")
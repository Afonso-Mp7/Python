v = int(input("Qual é a velocidade em que o veículo estava?"))
if v > 80 :
    print(f'Estás acima do limite permitido. A multa foi gerada no valor de"{v - 80 * 2}"euros.')
else:
    print("Dentro do limite. Boa viagem.")


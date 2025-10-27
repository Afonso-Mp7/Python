ordenado = float(input("Qual é o teu ordenado atual?"))
if ordenado<500 :
   reajuste = 0.15
   a = ordenado * reajuste
elif ordenado >= 500 and ordenado <= 1000:
    reajuste =0.1
    a = ordenado * reajuste
else :
    reajuste = 0.05
    a = ordenado * reajuste
b = a + ordenado
print(f'A reajuste será de"{reajuste}"e o ordenado atual é"{b}".')
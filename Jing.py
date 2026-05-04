import requests

a = int(input("Qual é a moeda que deseja converter? 0 para Euro, 1 para Dolar Americano e 2 para Real Brasileiro."))
b = float(input("Qual valor deseja converter?"))
c = int(input("Para qual moeda deseja converter? 0 para Euro, 1 para Dolar Americano e 2 para Real Brasileiro."))

if c == 0 :
    if a == 1 :
        url = requests.get('https://economia.awesomeapi.com.br/last/EUR-USD')
        cotacao = url.json()
        convertido = float(cotacao['EURUSD']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    elif a == 2 :
        url = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
        cotacao = url.json()
        convertido = float(cotacao['EURBRL']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    else :
        print('Não estás a converter nada -_-')
elif c == 1 :
    if a == 0 :
        url = requests.get('https://economia.awesomeapi.com.br/last/USD-EUR')
        cotacao = url.json()
        convertido = float(cotacao['USDEUR']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    elif a == 2 :
        url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        convertido = float(cotacao['USDBRL']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    else :
        print('Não estás a converter nada -_-')
elif c == 2 :
    if a == 1 :
        url = requests.get('https://economia.awesomeapi.com.br/last/BRL-USD')
        cotacao = url.json()
        convertido = float(cotacao['BRLUSD']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    elif a == 0 :
        url = requests.get('https://economia.awesomeapi.com.br/last/BRL-EUR')
        cotacao = url.json()
        convertido = float(cotacao['BRLEUR']['bid'])
        r = b/convertido
        print('O valor convertido é', (r))
    else :
        print('Não estás a converter nada -_-')
else :
    print('Não estás a converter nada -_-')
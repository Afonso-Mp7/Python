import requests
from tkinter import *
from tkinter import ttk

a = int(input("Qual é a moeda que deseja converter? 0 para Euro, 1 para Dolar Americano e 2 para Real Brasileiro."))
b = float(input("Qual valor deseja converter?"))
c = int(input("Para qual moeda deseja converter? 0 para Euro, 1 para Dolar Americano e 2 para Real Brasileiro."))
lista = ['EUR', 'USD', 'BRL']

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
        cotacao = url.json()
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

janela = Tk()
janela.geometry ('500x500+50+50')
var1 = ttk.Combobox(janela, font = 'Arial', justify = 'right')
var1.place(width = 100, height = 30, x=100, y=100)
var1['values'] = (lista)
var1.current(0)
print(var1.get())
var2 = ttk.Combobox(janela, font = 'Arial', justify = 'left')
var2.place(width = 100, height = 30, x=500, y=100)
var2['values'] = (lista)
var2.current(0)
print(var2.get())

label = tk.Label(janela, text = 'converter')
label.place(x=200, y=200)

janela.mainloop ()
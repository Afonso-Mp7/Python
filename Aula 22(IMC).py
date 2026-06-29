from tkinter import *
import tkinter as tk

root = Tk()
root.title('Har har har har har')
root.geometry('500x500+50+50')
root.wm_resizable(width=True, height=True)

label1 = tk.Label(root, text = "Calculadora de IMC")
label1.place(x=200, y=50)

label2 = tk.Label(root, text = "Peso(kg)")
label2.place(x=100, y=100)
senha1 = Entry(root, font = 'Time 10')
senha1.place(width=200, height=15, x=175, y=105)

label3 = tk.Label(root, text = "Altura")
label3.place(x=100, y=150)
senha2 = Entry(root, font = 'Time 10')
senha2.place(width=200, height=15, x=175, y=155)

def calcular_IMC():
    peso = float(senha1.get())
    altura = float(senha2.get())
    imc = peso/(altura*altura)
    label4 = tk.Label(root, text= f'IMC = {imc}')
    label4.place(x=200, y=250)
    if imc <= 18.5 :
        a = 'Estás abaixo do peso.'
        Documentos = "imc_magro.png"
    elif imc <= 24.9 :
        a = 'Estás com peso normal.'
        Documentos = "imc_normal.png"
    elif imc <= 29.9 :
        a = 'Estás acima do peso.'
        Documentos = "imc_obeso.png"
    elif imc <= 39.9 :
        a = 'Estás com obesidade grau 1.'
        Documentos = "imc_obeso_2.png"
    elif imc >= 40.0 :
        a = 'Estás com obesidade grau 2.'
        Documentos = "imc_sobrepeso.png"
    imagem = tk.PhotoImage(file= Documentos)
    label_imagem.config(image=imagem)
    label_imagem.image = imagem
    label5 = tk.Label(root, text= f'{a}')
    label5.place(x=200, y=300)
    senha1.delete('0','end')
    senha2.delete('0', 'end')

button = tk.Button(root, text='Calcular IMC', command=calcular_IMC)
button.place(x=200, y=200)
label6 = tk.Label(root)
label6.grid(row=5, column=0, columnspan=2)

root.mainloop()
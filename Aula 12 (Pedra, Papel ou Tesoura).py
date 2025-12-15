import random
a = int(input("Escolhe Pedra,Papel ou Tesoura. Pedra-1, Papel-2, Tesoura-3."))
jogo = ["Pedra","Papel","Tesoura"]
computador= random.choice (jogo)
def vitoria (computador, a):
    if computador=="Tesoura" and a==1:
        print ("Tesoura. Venceste!")
    elif computador=="Papel" and a==3:
        print("Papel. Venceste!")
    elif computador=="Pedra" and a==2:
        print("Pedra. Venceste!")
    elif computador=="Tesoura" and a==2:
        print("Tesoura. Perdeste!")
    elif computador=="Papel" and a==1:
        print("Papel.Perdeste!")
    elif computador=="Pedra" and a==3:
        print("Pedra. Perdeste!")
    elif computador=="Tesoura" and a==3:
        print("Tesoura.Empate!")
    elif computador=="Papel" and a==2:
        print("Papel.Empate!")
    elif computador=="Pedra" and a==1:
        print("Pedra.Empate!")
    else:
        print("Não está nas regras.")

vitoria (computador, a)
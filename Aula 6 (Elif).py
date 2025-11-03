i = int(input("Qual é o teu ano de nascimento?"))
from datetime import date
hoje = date.today().year
e = hoje-i
if e<=9 :
    print("O teu escalão é Mirin.")
elif e<=14 :
    print("O teu escalão é Infantil.")
elif e<=19 :
    print("O teu escalão é Junior.")
elif e<=25 :
    print("O teu escalão é Senior.")
else :
    print("O teu escalão é Master.")

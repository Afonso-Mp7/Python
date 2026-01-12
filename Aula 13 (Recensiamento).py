from datetime import date
hoje = date.today().year
r = int(input("Qual é o teu ano de nascimento?"))
x = hoje - r
print (f'Tu estás com {x} anos.')
if x < 18 :
    print ("Ainda não tens idade para o recensiamento.")
elif x > 21 :
    print ("Já passou o prazo para o recensiamento.")
else :
    print ("Está no momento para o recensiamento.")
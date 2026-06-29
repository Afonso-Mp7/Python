from time import sleep
joker = 2
dinheiro = 0
nome = input("Insere o teu nome para começar a competição.")
sleep (2)
print (f'Bem vindo/a, {nome}, à mini competição de Joker!')
sleep (3)
print (f'Mas antes de tudo, passo a explicar as regras.')
sleep (3)
print (f'Terás de responder a 10 questões, e, sempre que acertares, será acrescentado 100$!')
sleep (4)
print (f'Porém, cada falha resultará na perda de 100$ ao teu total. ')
sleep (4)
print (f'Mas não te preocupes! Terás 2 ajudas no caso de precisares.')
sleep (4)
print (f'2 Jokers, que irão dar-te a resposta certa.')
sleep (4)
print (f'Usa-as com sabedoria e boa sorte! O quiz vai começar!')
sleep (5)
print ("Primeira pergunta: Qual é o animal que aparece no logotipo da Ferrari?")
sleep (4)
a = input("A- Leão , B- Cavalo , C- Tigre , D- Leopardo ")
if a == "B,b":
        print("Acertaste!")
        dinheiro += 100
elif a in "A,a, C,c, D,d":
        print("Erraste!")
        dinheiro -= 100
elif a in "Joker, joker, JOKER":
        print("A resposta era a B!")
        joker -= 1
        dinheiro += 100
sleep (3)
print (f'Segunda pergunta: Quem escreveu "Dom Casmurro"?')
sleep (4)
b = input("A- Machado de Assis , B- Camilo Castelo Branco, C- William Shakespeare , D- Barbara Cartland ")
if b == "A" or "a":
         print("Acertaste!")
         dinheiro += 100
elif b in "B,b, C,c D,d":
        print("Erraste!")
        dinheiro -= 100
elif b in "Joker, joker, JOKER":
        print("A resposta era a A!")
        joker -= 1
        dinheiro += 100
sleep (3)
print ("Terceira pergunta: Qual foi a primeira pessoa a viajar no espaço?")
sleep (4)
c = input("A- Neil Armstrong , B- Buzz Aldrin , C- Alan Shepard , D- Yuri Gagarin ")
if c == "D" or "d":
        print("Acertaste!")
        dinheiro += 100
elif c in "A,a B,b C,c":
        print("Erraste!")
        dinheiro -= 100
elif c in "Joker, joker, JOKER":
        print("A resposta era a D!")
        joker -= 1
        dinheiro += 100
sleep (3)
print ("Quarta pergunta: Em que ano o homem pisou na Lua pela primeira vez?")
sleep (4)
d = 0
while d != ["A,a B,b C,c D,d"] :
    d = input("A- 1968 , B- 1969 , C- 1970 , D- 1971 ")
    if d == "B" or "b":
        print("Acertaste!")
        dinheiro += 100
        break
    elif d in "A,a C,c D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif d in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a B!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
e = 0
print (f'Quinta pergunta: Qual é o sobrenome mais comum em Portugal?')
while e != ["A,a B,b C,c D,d"] :
    e = input("A- Ferreira , B- Santos , C- Pereira , D- Silva ")
    if e == "D" or "d":
        print("Acertaste!")
        dinheiro += 100
        break
    elif e in "A,a B,b C,c":
        print("Erraste!")
        dinheiro -= 100
        break
    elif e in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a D!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
print ("Sexta pergunta: Quem pintou a Mona Lisa?")
sleep (4)
f = 0
while f != ["A,a B,b C,c D,d"] :
    f = input("A- Claude Monet , B- Pablo Picasso , C- Leonardo da Vinci , D- Vincent Van Gogh ")
    if f == "C" or "c":
        print("Acertaste!")
        dinheiro += 100
        break
    elif f in "A,a B,b D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif f in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a C!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
g = 0
print ("Sétima pergunta: Qual é a moeda oficial do Japão?")
while g != ["A,a B,b C,c D,d"] :
    g = input("A- Lek , B- Iene , C- Baht , D- Dólar ")
    if g == "B" or "b":
        print("Acertaste!")
        dinheiro += 100
        break
    elif g in "A,a, C,c, D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif g in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a B!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
h = 0
print ("Oitava pergunta: Qual foi a única pessoa a receber vários prémios Nobel em diferentes áreas científicas?")
while h != ["A,a B,b C,c D,d"] :
    h = input("A- Marie Curie , B- Albert Einstein , C- Stephen Hawking , D- Mahatma Ghandi ")
    if h == "A" or "a":
        print("Acertaste!")
        dinheiro += 100
        break
    elif h in "B,b C,c D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif h in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a A!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
print ("Nona pergunta: Qual foi o primeiro presidente de Portugal?")
sleep (4)
i = 0
while i != ["A,a B,b C,c D,d"] :
    i = input("A- Bernardino Machado , B- Teófilo Braga , C- Manuel de Arriaga , D- Marcelo Rebelo de Sousa ")
    if i == "C" or "c":
        print("Acertaste!")
        dinheiro += 100
        break
    elif i in "A,a B,b D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif i in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a C!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (3)
j = 0
print ("Décima e última pergunta: Qual é o país mais novo do mundo?")
while j != ["A,a B,b C,c D,d"] :
    j = input("A- Sudão do Sul , B- Kosovo , C- Palau , D- Timor Leste ")
    if j == "A" or "a":
        print("Acertaste!")
        dinheiro += 100
        break
    elif j in "B,b C,c D,d":
        print("Erraste!")
        dinheiro -= 100
        break
    elif j in "Joker, joker, JOKER":
        if joker > 0:
            print("A resposta era a A!")
            joker -= 1
            dinheiro += 100
            break
        elif joker <= 0:
            print("Já não tens Jokers! Estás por tua conta.")
            sleep(2)
sleep (5)
print ("E com isto, chegámos ao fim da competição!")
sleep (3)
if dinheiro < 0 :
    print (f'E acabaste de perder...{dinheiro} euros.')
    sleep (3)
    print ("Mais sorte para a próxima!")
elif dinheiro == 0 :
    print ("A boa notícia é que não perdeste dinheiro! A má notícia é que não ganhaste também.")
    sleep (4)
    print ("Espero que pelo menos tenhas aprendido alguma coisa!")
elif dinheiro <= 400 :
    print ("Conseguiste no total...")
    sleep (3)
    print (f'{dinheiro} euros! Podia estar melhor!')
elif dinheiro <= 900 :
    print ("Conseguiste no total...")
    sleep (3)
    print (f'{dinheiro} euros! Nada mal!')
elif dinheiro == 1000 :
    print ("Conseguiste no total...")
    sleep (3)
    print (f'{dinheiro} euros, o prémio mais alto! Os meus parabéns!')
sleep (5)
print (f'A competição de Joker terminou. Obrigado por jogar, {nome}.')
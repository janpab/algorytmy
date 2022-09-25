from math import fabs,ceil

def to_dec(num,podstawa): #int,int > int
    is_minus = False
    if num<0:
        is_minus = True
    num = str(num).replace('-','')
    wynik = 0
    mnoznik = 1
    for i in range (len(num)-1,-1,-1):
        wynik+=int(num[i])*mnoznik
        mnoznik*=podstawa
    if is_minus:
        return wynik * -1
    else:
        return wynik
        
def konwertuj(num,podstawa,docelowy): #int,int,int > int
    dec = to_dec(num,podstawa)
    
    is_minus = False
    if dec<0:
        is_minus = True
        dec*=-1
    
    wynik = ""

    while dec!=0:
        wynik = str(dec%docelowy) + wynik
        dec = dec//docelowy
    
    if is_minus:
            return int(wynik) * -1
    else:
        return int(wynik)


def zadanie1():
    dane_s1 = []
    min_s1 = 9999999
    dane_s2 = []
    min_s2 = 9999999
    dane_s3 = []
    min_s3 = 9999999
    with open("dane_systemy1.txt") as file:
        dane_s1 = file.readlines()
    with open("dane_systemy2.txt") as file:
        dane_s2 = file.readlines()
    with open("dane_systemy3.txt") as file:
        dane_s3 = file.readlines()

    for line in dane_s1: #zczytuje wszystkie liczby z dane s1
        temperatura = int(line.split(' ')[1].strip()) #usuwa znaki białe z tablicy dane s1
        temperatura_dec = to_dec(temperatura,2) #zamienia na system dziesiętny 
        if temperatura_dec<min_s1:
            min_s1 = temperatura_dec # wybiera najniższy pomiar
    
    for line in dane_s2: 
        temperatura = int(line.split(' ')[1].strip()) #usuwa znaki białe z tablicy dane s2
        temperatura_dec = to_dec(temperatura,4) # zamienia na system dziesiętny czwórkowy na dziesiętny
        if temperatura_dec<min_s2: 
            min_s2 = temperatura_dec # najniższy pomiar 

    for line in dane_s3:
        temperatura = int(line.split(' ')[1].strip()) #usuwa znaki białe z tablicy dane s3
        temperatura_dec = to_dec(temperatura,8) # zamienia na system dziesiętny
        if temperatura_dec<min_s3:
            min_s3 = temperatura_dec # wybiera najniższy pomiar

    #konwertuje każdy wynik na system binarny 
    print(konwertuj(min_s1,10,2)) 
    print(konwertuj(min_s2,10,2))
    print(konwertuj(min_s3,10,2))
     

def zadanie2():
    dane_s1 = [] 
    dane_s2 = []
    dane_s3 = []

    licznik = 0
    zegar = 12

    with open("dane_systemy1.txt") as file:
        dane_s1 = file.readlines()
    with open("dane_systemy2.txt") as file:
        dane_s2 = file.readlines()
    with open("dane_systemy3.txt") as file:
        dane_s3 = file.readlines()
    
    for i in range(1095): #dla każdego pomiaru 
        zegar_s1 = to_dec(int(dane_s1[i].split(' ')[0].strip()),2) # zamienia wszystkie na system dziesiętny
        zegar_s2 = to_dec(int(dane_s2[i].split(' ')[0].strip()),4)
        zegar_s3 = to_dec(int(dane_s3[i].split(' ')[0].strip()),8)
        if zegar_s1 != zegar and zegar_s2 != zegar and zegar_s3 != zegar: #jeżeli któryś sie nie zgadza to licznik błędów się zwiększa
            licznik+=1
        zegar+=24 #zegar po każdej operacji sprawwdzenia zwiększa sie o 24 bo pomiary powinny byc co 24 godziny
    
    print(licznik)# ilosc błędów 

def zadanie3():
    dane_s1 = [] 
    dane_s2 = []
    dane_s3 = []

    max_s1 = -999999
    max_s2 = -999999
    max_s3 = -999999

    licznik_dni_rekordowych = 0 
    zegar = 12


    with open("dane_systemy1.txt") as file:
        dane_s1 = file.readlines()
    with open("dane_systemy2.txt") as file:
        dane_s2 = file.readlines()
    with open("dane_systemy3.txt") as file:
        dane_s3 = file.readlines()

    for i in range(1095):
        
        zegar_s1 = to_dec(int(dane_s1[i].split(' ')[1].strip()),2) # zamienia wszystkie na system dziesiętny
        zegar_s2 = to_dec(int(dane_s2[i].split(' ')[1].strip()),4)
        zegar_s3 = to_dec(int(dane_s3[i].split(' ')[1].strip()),8)

        flaga = False

        if zegar_s1>max_s1:
            flaga = True
            max_s1 = zegar_s1
        
        if zegar_s2>max_s2:
            flaga = True
            max_s2 = zegar_s2
        
        if zegar_s3>max_s3:
            flaga = True
            max_s3 = zegar_s3

        if flaga:
            licznik_dni_rekordowych +=1

    print(licznik_dni_rekordowych)
    
def zadanie4():
    skok = 0
    temp_dane_s1 = []
    pomiar_dane_s1 = []
    with open("dane_systemy1.txt") as file:
        temp_dane_s1 = file.readlines()
    
    for i in range(1095):
        temp_dane_s1[i] = to_dec(int(temp_dane_s1[i].split(' ')[1].strip()),2)

    max_skok = 0
    
    for i in range(0, 1095):
        for j in range(i+1,1095):
            rij = temp_dane_s1[i] - temp_dane_s1[j] 
            x = fabs((i+1) - (j+1))

            skoktest =  ceil((rij * rij)/ x)

            if skoktest>max_skok and i!=j:
                max_skok = skoktest
    print(max_skok)

zadanie3()


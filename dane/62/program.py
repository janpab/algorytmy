def from_oct_to_dec(num):
    wynik = 0
    mnoznik = 1
    num = str(num)
    for i in range (len(num)-1,-1,-1):
        wynik+=int(num[i])*mnoznik
        mnoznik*=8

    return wynik
def form_dec_to_oct(num):
    wynik = 0
    
    wynik = ""

    while num!=0:
        wynik = str(num%8) + wynik
        num = num//8
    return int(wynik)



def zadanie1():
    najwieksza = -999999
    najmniejsza = 999999
    liczby = []
    with open("liczby1.txt") as f: 
        liczby = f.readlines()
    for i in range(-1,999):
        liczba = liczby[i].strip()
        
        
        
        if int(liczba) > najwieksza:
            najwieksza = int(liczba)
        if int(liczba) < najmniejsza:
            najmniejsza = int(liczba)
    print(najmniejsza, najwieksza)
def zadanie2():
    liczby = []
    dlugosc_ciagu=0
    najdluzszy_ciag=0
    poczatek_najdluz_ciag=0
    
    with open("liczby2.txt") as f: 
        liczby = f.readlines()
    
    for i in range(0,999):
        for j in range(i,999):
            if int(liczby[j])-int(liczby[j+1])<0:
                dlugosc_ciagu+=1
            else:
                break
        if dlugosc_ciagu>najdluzszy_ciag:#sprawdza czy jest to dłuży ciąg od poprzednich, jeśli tak to aktualizuje zmienne tych największych.
            najdluzszy_ciag=dlugosc_ciagu
            poczatek_najdluz_ciag = int(liczby[i])
        i=j+1
        dlugosc_ciagu=0
            
    print(poczatek_najdluz_ciag,najdluzszy_ciag)
def zadanie3():


    liczby1 = []
    liczby2 = [] 
    ilosc_z_1 = 0
    ilosc_z_2 = 0   
    with open("liczby1.txt") as f: 
        liczby1 = f.readlines()

    
    with open("liczby2.txt") as f: 
        liczby2 = f.readlines()

    for i in range(0,1000):
        liczbaz1 = from_oct_to_dec(int(liczby1[i].strip()))
        liczbaz2 = int(liczby2[i].strip())
        if liczbaz1==liczbaz2:
            ilosc_z_1+=1
        if liczbaz2 < liczbaz1:
            ilosc_z_2+=1
    print(ilosc_z_1,ilosc_z_2)
def zadanie4():
    liczby=[]
    licznik_w_dec=0
    licznik_w_oct=0
    with open("liczby2.txt") as f: 
        liczby = f.readlines()
    for i in range(0,1000):
        liczba=str(liczby[i].strip())
        for j in range(len(liczba)-1):
            if liczba[j]=="6":
                licznik_w_dec+=1
    for k in range(0,1000):
        liczba=str(form_dec_to_oct(int(liczby[k].strip())))
        for l in range(len(str(liczba))-1):
            if liczba[l]=="6":
                licznik_w_oct+=1
    print(licznik_w_dec,licznik_w_oct)

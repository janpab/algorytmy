from re import I


def is_dwucykliczny(num):
    dwucykliczny=False
    num = str(num)
    if num[:int(len(num)/2)]==num[int(len(num)/2):]:
        dwucykliczny=True
    return dwucykliczny
def has_not_two_single(num):
    no_two_single = True
    num = str(num)
    for i in range(len(num)-1):
        if num[i]+num[i+1] =="11":
            no_two_single=False
            break
    return no_two_single
def from_bin_to_dec(num):
    wynik = 0
    mnoznik = 1
    num = str(num)
    for i in range (len(num)-1,-1,-1):
        wynik+=int(num[i])*mnoznik
        mnoznik*=2

    return wynik

def czy_polpierwsza(liczba):# funkcja sprawdzajaca czy liczba jest polpierwsza 
    if liczba == 1:
        return False
        
    if liczba % 2 == 0 and czy_pierwsza(int(liczba/2)):

        return True
        
    for i in range(3,int(liczba/2)+1):#i * jakas_liczba == liczba    liczba//i - pierwsza
        if czy_pierwsza(i) and czy_pierwsza(liczba//i) and  liczba//i*i==liczba:

            return True            
            
    return False




def czy_pierwsza(liczba):# funkcja sprawdzajaca czy liczba jest pierwsza
    if liczba == 1: # 1 nie jest liczbą pierwszą
        return False
    if liczba == 2:#2 jest liczbą pierwsza
        
        return True 
    if liczba % 2 == 0:# wszystkie liczby podzielne przez 2 nie są liczbami pierwszymi 
        return False
    for i in range(3, int(liczba/2)+1):  
        if liczba % i == 0:
            return False
    return True



def zadanie1():
    liczby=[]
    with open("ciagi.txt") as f: 
        liczby = f.readlines()
    ciagi_dwucykliczne = []
    ilosc_ciagow = 0
    for i in range(0,1000):
        liczba = liczby[i].strip()
        if is_dwucykliczny(liczba):
            ciagi_dwucykliczne.append(liczba)
            ilosc_ciagow+=1
    for j in range(len(ciagi_dwucykliczne)-1):
        print(ciagi_dwucykliczne[j])
    print("ilosc ciagów dwucyklicznych",ilosc_ciagow)
def zadanie2():
    liczby=[]
    licznik=0
    with open("ciagi.txt") as f: 
        liczby = f.readlines()
    for i in range(0,1000):
        liczba = liczby[i].strip()
        if has_not_two_single(liczba):
            licznik+=1
    print(licznik)
def zadanie3():
    liczby=[]
    licznik =0
    najwieksza = -9999999
    najmniejsza = 9999999

    with open("ciagi.txt") as f: 
        liczby = f.readlines()
    for i in range(0,1000):
        liczba = liczby[i].strip()
        liczba_in_dec= from_bin_to_dec(liczba)
        print("Sprawdzam", i, liczba_in_dec, licznik)
        if czy_polpierwsza(liczba_in_dec):
            if liczba_in_dec>najwieksza:
                najwieksza = liczba_in_dec
            if liczba_in_dec<najmniejsza:
                najmniejsza = liczba_in_dec
            licznik +=1
        
    print("Ilosc liczb polpierwszych",licznik)
    print("Najwieksza polpierwsza:", najwieksza)
    print("Najmniejsza liczba polpierwsza", najmniejsza)

zadanie3()
        


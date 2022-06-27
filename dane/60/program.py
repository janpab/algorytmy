


def dzielniki(number):
    dz = []
    for i in range(1, number+1):
        if number%i==0:
            dz.append(i)
    return dz




def zadanie1():
    liczby = []
    licznik_1000 = 0
    mniejsze_od_1000 = []
    with open ("liczby.txt") as file:
        liczby = file.readlines()

    for i in range(200):
        liczba = int(liczby[i].strip())
        if liczba<1000:
            licznik_1000+=1
            mniejsze_od_1000.append(liczba)
    print("ilosc liczb mniejszych od 1000: ", licznik_1000)
    print("dwie ostatnie to ", mniejsze_od_1000[len(mniejsze_od_1000)-2], mniejsze_od_1000[len(mniejsze_od_1000)-1])
        
def zadanie2():
    liczby = []
    
    with open ("liczby.txt") as file:
        liczby = file.readlines()
    for i in range(200):
        liczba = int(liczby[i].strip())
        dz_liczby = dzielniki(liczba)
        if len(dz_liczby)==18:
            print(liczba)
            for j in range(0,18):
                print(dz_liczby[j],end=" ")
            print()

def zadanie3():
    tablica = 1000001*[0]
    liczby = []

    max_pierwsza = -99999999
    
    with open ("liczby.txt") as file:
        liczby = file.readlines()
    for i in range(200):
        liczba = int(liczby[i].strip())
        dz_liczby = dzielniki(liczba)#dzielniki 
        for dzielnik in dz_liczby:#listy 
            tablica[dzielnik]+=1 #

    for i in range(200):
        liczba = int(liczby[i].strip())
        dz_liczby = dzielniki(liczba)#dzielniki 
        uniq = True
        for j in range(len(dz_liczby)):#listy 
            if dz_liczby[j] != 1 and tablica[dz_liczby[j]] > 1:
                uniq  = False
                break
        if uniq and liczba>max_pierwsza:
            max_pierwsza = liczba
    print(max_pierwsza)

zadanie3()
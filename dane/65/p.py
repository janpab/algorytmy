def zadanie1():
    ulamki = []
    with open("dane_ulamki.txt") as f:
        ulamki = f.readlines()
    najmnieszy_ulamek_w = 9999999
    najmniejszy_licznik = 9999999
    najmnijeszy_mianownik = 9999999

    for i in range(1000):
        ulamek = ulamki[i].strip()
        u1 = ulamek.split()
        mianownik = int(u1[1])
        licznik = int(u1[0])
        wynik = licznik/mianownik
        if wynik<najmnieszy_ulamek_w:
            najmnieszy_ulamek_w=wynik
            najmniejszy_licznik = licznik
            najmnijeszy_mianownik = mianownik
        if wynik == najmnieszy_ulamek_w and najmnijeszy_mianownik>mianownik:
            najmniejszy_licznik = licznik
            najmnijeszy_mianownik = mianownik
    print("ulamek to ", najmniejszy_licznik,najmnijeszy_mianownik, najmnieszy_ulamek_w)
def zadanie2():
    ulamki = []
    licznik1 = 0
    with open("dane_ulamki.txt") as f:
        ulamki = f.readlines()
    for i in range(1000):
        ulamek = ulamki[i].strip()
        u1 = ulamek.split()
        mianownik = int(u1[1])
        licznik = int(u1[0])
        nieskacalna = True

        if licznik>mianownik:
            for k in range(2, mianownik+1):# dzielimy od 2 do mnijszej liczby w ułamku
                if mianownik%k==0 and licznik%k==0:# jezeli to i to sie dzieli to j
                    nieskacalna = False
                    break
            
        if mianownik>=licznik:
            for j in range(2, licznik+1):
                if mianownik%j==0 and licznik%j==0:
                    nieskacalna = False
                    break
        if nieskacalna:
            licznik1 +=1
    print(licznik1)
def zadanie3():
    ulamki = []
    licznik1 = 0
    with open("dane_ulamki.txt") as f:
        ulamki = f.readlines()
    for i in range(1000):
        ulamek = ulamki[i].strip()
        u1 = ulamek.split()
        mianownik = int(u1[1])
        licznik = int(u1[0])
      
            

        if licznik>mianownik:
            for k in range(mianownik,1,-1):# dzielimy od 2 do mnijszej liczby w ułamku
                if mianownik%k==0 and licznik%k==0:# jezeli to i to sie dzieli to j
                    licznik=int(licznik/k)
                    mianownik=int(mianownik/k)
                    break
        elif mianownik>licznik:
            for j in range(licznik,1,-1):
                if mianownik%j==0 and licznik%j==0:
                    licznik=int(licznik/j)
                    mianownik=int(mianownik/k)
                    break
        else:
            licznik = 1
            mianownik= 1
            
        
        licznik1 += licznik
    print(licznik1)
def zadanie4():
    ulamki = []

    with open("dane_ulamki.txt") as f:
        ulamki = f.readlines()
    for i in range(1000):
        ulamek = ulamki[i].strip()
        u1 = ulamek.split()
        mianownik = int(u1[1])
        licznik = int(u1[0])



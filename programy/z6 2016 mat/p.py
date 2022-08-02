'''
Matura czerwiec 2016, zadanie 6. Systemy liczbowe
'''
with open(r'C:\Users\Jan\Desktop\J\KOREPETYCJE\algorytmy\programy\z6 2016 mat\liczby.txt') as f:
    kody = f.readlines()

kody = [el.strip() for el in kody]


def zad_61():
    licz = 0
    for el in kody:
        if el[-1] == "8":
            licz +=1
    print(licz)
zad_61()

def zad_62():
    licznik = 0
    for el in kody:
        if el[-1] == "4":
            zero = False
            for liczb in el:
                if liczb == "0":
                    zero = True
            if not zero:
                licznik += 1    
    print(licznik)
zad_62()
def zad_63():
    licznik = 0
    for el in kody:
        if el[-1] == "2" and el[-2]== "0":
            licznik+=1
    print(licznik)
zad_63()

def to_int(a, p):# 2-9
    potega=0
    suma = 0 
    for c in reversed(a):
        if c.isdigit():
            suma += int(c) * p**potega
            potega+=1
        else:
            for k in range(0,33):
                if chr(97 + k) == c:
                    liczba_z_litery = 10+k

            suma += int(liczba_z_litery) * p**potega
            potega+=1

    return suma

def zad_64():
    suma = 0
    for el in kody:
        if el[-1]=="8":
            suma+= to_int(el[:-1],8)
    print(suma)
print("6_4")
zad_64()



def zad_65():
    najmniejsza = [999999999,""]
    najwieksza = [-99999999,""]
    for el in kody:
        liczba = to_int(el[:-1],int(el[-1]))
        if liczba>najwieksza[0]:
            najwieksza[0] = liczba
            najwieksza[1] = el
        if liczba < najmniejsza[0]:
            najmniejsza[0] = liczba
            najmniejsza[1] = el
    print("NAJWIEKSZA: ",najwieksza)
    print("NAJMNIEJSZA: ",najmniejsza)
zad_65()
            


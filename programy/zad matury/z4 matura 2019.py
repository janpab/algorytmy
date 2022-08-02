'''
Matura czerwiec 2019, zadanie 4. Wybrane liczby
'''


with open(r"C:\Users\Jan\Desktop\J\KOREPETYCJE\algorytmy\programy\zad matury\liczby_przyklad.txt") as f:
    liczby = f.readlines()

liczby = [el.strip() for el in liczby]

with open(r"C:\Users\Jan\Desktop\J\KOREPETYCJE\algorytmy\programy\zad matury\pierwsze_przyklad.txt") as k:
    pierwsze = k.readlines()

pierwsze = [els.strip() for els in pierwsze]

def czy_pierwsza(a):
    if a == 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, int(a/2)+1, 2):
        if a % i == 0:
            return False
    return True



def zad_41():
    pierwsze_liczby = []
    for el in liczby:
        el = int(el)
        if el >=100 and el<=5000 and czy_pierwsza(el):
            pierwsze_liczby.append(el)
    [print(el) for el in pierwsze_liczby]
zad_41()
def zad_42():
    pierwsz_rev = []
    for el in pierwsze:
        rev_el = reversed(str(el))
        rev_el = int("".join(rev_el))
        if czy_pierwsza(rev_el):
            pierwsz_rev.append(el)
    print(pierwsz_rev)

zad_42()

def sum(a):
    suma = 0
    while a !=0:
        suma += a % 10 
        a //=  10
    return suma

def zad_43():
    licznik = 0
    for el in pierwsze:
        waga = sum(int(el))
        while not( waga >0 and waga <=9):
            waga = sum(waga)
        if waga == 1:
            licznik +=1
    print(licznik)
print("zad 4.3")
zad_43()

'''
Matura czerwiec 2016, zadanie 6. Systemy liczbowe
'''

'''
Matura czerwiec 2015, zadanie 6. Kody kreskowe
'''

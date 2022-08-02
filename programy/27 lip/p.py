'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w systemie binarnym.
Wykorzystaj algorytm Hornera.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby i odwrotnie.


ABCDE = A*2^4 + B*2^3 + C*2^2 + D*2^1 + E

2*(A*2^3 + B*2^2 + C*2^1 + D) + E
2*(2*(A*2^2 + B*2^1 + C) + D) + E
2*(2*(2*(A*2^1 + B) + C) + D) + E
2*(2*(2*(2*(A) + B) + C) + D) + E

x = 0
x = 2*x + A
x = 2*x + B
x = 2*x + C
x = 2*x + D
x = 2*x + E


 ABCDE
"10101"

'''

from audioop import reverse


def to_int(a):
    x = 0 
    for el in a: 
        x = 2*x + int(el)
    return x
print(to_int("1111"))

'''
Napisz funkcję obliczającą sumę wszytskich cyfr danej liczby.

123 % 10 = 3
123 // 10 = 12
12 
'''
def sum(a):
    suma = 0
    while a !=0:
        suma += a % 10 
        a //=  10
    return suma
print(sum(123),'sum')

'''
Wypisz wszystkie liczby mniejsze od 1000, których suma cyfr podniesiona do kwadratu 
i pomnożona razy 2 (2 * suma_cyfr ^ 2) jest równa danej liczbie.
'''

def sum2():
    for i in range(1000):
        suma = 0
        licz = i
        while licz !=0:
            suma += licz % 10 
            licz //=  10
        if i == (2* (suma**2)):
            print(i)
        

sum2()


'''
Napisz funkcję sumującą cyfry liczby podanej w parametrze. 
Następnie funkcja ma sumować cyfry tak otrzymanej sumy.
Proces sumowania powtarzamy aż do momentu otrzymania liczby jednocyfrowej.
Funkcja zwraca tak otrzymana liczbę jednocyfrową.
'''
def sum_p(a): # suma
    suma = 0
    while a !=0:
        suma += a % 10 
        a //=  10
    return suma

def sum3(a):# sumuje do 1 cyfrowa
    while not (a >= 0 and a <=9):
        a = sum_p(a)
    return a
print(sum3(12333)) 
#12
#3


'''
Wykorzystaj napisaną powyżej funkcję, do stwierdzenia, czy dana liczba 
jest podzielna przez 3 (korzystając z cechy podzielności liczby przez 3).
'''
def czy_podziel_trzy(a):
    if sum_p(a)%3 == 0:
        return True
    else:
        return False
print(czy_podziel_trzy(99))

'''
Matura maj 2015, zadanie 4. Liczby binarne
'''
with open(r"C:\Users\Jan\Desktop\J\KOREPETYCJE\algorytmy\programy\27 lip\liczby.txt") as f:
    linie = f.readlines()

linie = [el.strip() for el in linie]

def zad_41():
    licznik = 0
    for el in linie:
        zera = 0
        jeden = 0
        for i in el:
            if i == "0":
                zera +=1
            if i == "1":
                jeden +=1
        if zera> jeden:
            licznik +=1
    return licznik

print(zad_41())

def zad_42():
    licz_2 = 0
    licz_8 = 0
    for el in linie:
        if el[-1]=="0":
            licz_2+=1
        if el[-3:]=="000":
            licz_8+=1
    print(licz_8,licz_2)
zad_42()


#ZAD DOM
def to_int(bin):
    potega=0
    suma = 0 
    for c in reversed(bin):
        suma += int(c) * 2**potega
        potega+=1
    return suma

def zad_43():
    najmniejsza = [to_int(linie[0]),0]
    najwieksza = [to_int(linie[0]),0]
    for i in range(len(linie)-1):
        liczba = to_int(linie[i])
        if liczba > najwieksza[0]:
            najwieksza[0]= liczba
            najwieksza[1]= i+1
        if liczba < najmniejsza[0]:
            najmniejsza[0] = liczba
            najmniejsza[1]= i+1
    print("najwieksza: ", najwieksza[1])
    print("najmnijesza: ", najmniejsza[1])


zad_43()
'''
Matura czerwiec 2019, zadanie 4. Wybrane liczby
'''
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

'''
Matura czerwiec 2016, zadanie 6. Systemy liczbowe
'''

'''
Matura czerwiec 2015, zadanie 6. Kody kreskowe
'''

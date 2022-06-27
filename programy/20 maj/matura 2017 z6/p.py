from itertools import *
from re import L

with open(r'C:\Users\Ja\Desktop\KOREPETYCJE\programy\20 maj\matura 2017 z6\dane.txt') as f:
    piks = f.readlines()


def zadanie1():
    piksele =[]
    for el in piks:
        piksele.append(el.strip().split())
    piksele = list(chain(*piksele))
    piksele_int = [int(el) for el in piksele]
    print(max(piksele_int))
    print(min(piksele_int))


# piksele = [el.strip().split() for el in piks]#rozbija na liczby w stringu
# print(piksele[:3])
# piksele = [[int(el) for el in linia] for linia in piksele]#liczby konwertuje na inty
# print(piksele[:3])

# "210 206 214 212 216"


def zadanie2():
    licznik = 0
    for el in piks:
        linia = el.strip().split()
        if linia != linia[::-1]:
            licznik+=1
    print(licznik)

'''
345
123
643

'''
piksele = [el.strip().split() for el in piks]#rozbija na liczby w stringu
piksele = [[int(el) for el in linia] for linia in piksele]#liczby konwertuje na inty

def kontrastujacy(i, j):#wiersz kolumna tablicza[][]   
    if j < 319 and abs(piksele[i][j+1]-piksele[i][j])>128:
        return True
    if j > 0 and abs(piksele[i][j-1]-piksele[i][j])>128:
        return True
    if i < 199 and abs(piksele[i+1][j]-piksele[i][j])>128:
        return True
    if i > 0 and abs(piksele[i-1][j]-piksele[i][j])>128:
        return True
    return False
def zadanie3():
    licznik = 0
    for i, wiersz in enumerate(piksele):
        for j, el in enumerate(wiersz):
            if kontrastujacy(i, j):
                licznik +=1
    print(licznik)

'''
(1=i) [ 16 13 14 18 14 20 17]=wiersz 
 [j=1 16, j=2 13, j=3 14,j=4 18, j=5 14, j=6 20, j=7 17]=wiersz 
2 22 16 13 18 10 19 14
3 12 13 24 18 14 20 20
4 24 14 25 18 11 13 13

'''
# piksele2 = [el.strip().split() for el in piks]#rozbija na liczby w stringu
# print(piksele2)

# piksele2 = [[int(el) for el in linia] for linia in piksele]#liczby konwertuje na inty
#[pierwsze linia(od 0)][liczba w lini(od 0)]
def zadanie4():
    najdluzsze = 0
    for i in range(0,320):
        licznik = 1
        for k in range(1, 200):# 1,200 / 0,200?
            if piksele[k-1][i] == piksele[k][i]:
                licznik+=1
            else:
                if licznik > najdluzsze:
                    najdluzsze = licznik
                licznik = 1
    return najdluzsze
print(zadanie4())
# a = [[1, 2 ,3, 4,5, 6, 7] ,
#   [1 ,2, 3, 4, 5, 6, 7 ],
#   [1, 2, 3, 4, 5, 6, 7 ],
#   [1, 2,3, 4, 5, 6, 7 ]]
# n = 0
# for i in range (0, 8):
#     l = 1
#     for k in range(1,4):
#         if a[k-1][i] == a[k][i]:
#             print(a[k][i])
#             l+=1
#         else:
#             if l > n:
#                 n = l 
#             l = 1
# print(n)
    
            
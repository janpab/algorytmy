# sortowanie kubelkowe O(n)
# - zakres liczb musi być znany
# - liczby muszą być rozłożone w miarę równomiernie
'''
<0,10)        0-9
a = [0, 5, 4, 7]

N - kubłeków - tyle ile elemntów w zbiorze
[0]       0,1,2
[4]       3,4
[7,5]     5,6,7
[]        8,9

[0, 4, 5, 7]


rozmiar = 10/4 = 2.5
0 -> 0/2.5  , idx = 0
5 -> 5/2.5  , idx = 2

N - ilosc elementow zbioru
rozmiar = max/N
idx = liczba // rozmiar


'''

from re import L


a = [6,3,8,12,2,18,9,0,11, 11, 14, 13]
# od 0 do 20


# <0, max_)
def sort_kub(tab, max_):
    lista = [[] for k in range(len(tab))]   # tworzenie kubelków
    rozmiar = max_/len(tab)
    for i in range(len(tab)):
        idx = int(tab[i]//rozmiar)
        lista[idx].append(tab[i])
    lista_sorted= []
    for k in range(len(lista)):
        if len(lista[k])==1:
            lista_sorted.append(lista[k][0])
        if len(lista[k])>1:
            #bąbelkowe ZADDOM
            for j in range(len(lista[k])):
                min = lista[k][0]
                idx = 0 
                for l in range(len(lista[k])):
                    if lista[k][l]<min:
                        min = lista[k][l]
                        idx = l
                #print(idx, lista[k])
                del lista[k][idx]
                lista_sorted.append(min)
    print(lista_sorted)

#[[0], [3, 2], [], [6], [8], [9], [11, 11], [12, 13], [14], [], [18], []]

sort_kub(a, 20)


# [6,5,4]       []
# [6,5]            [4]
# [6]            [4, 5]
# []            [4, 5, 6]


# sortowanie przez scalanie O(n logn)

a = [1,2,3,6,8,11,23]               # N
b = [4,7,9,12,56,78,88]         # M

# N + M 
# [3, 4, 6, 7, 8, ...]

def scal(a, b):
    idx_a = 0
    idx_b = 0
    sorted = []
    while True:
        if idx_a > len(a)-1:
            #reszta z b
            for k in range(idx_b, len(b)):
                sorted.append(b[k])
            break
        if idx_b> len(b)-1:
            for k in range(idx_a, len(a)):
                sorted.append(a[k])
            break
        if a[idx_a]>b[idx_b]:
            sorted.append(b[idx_b])
            idx_b+=1
        else:
            sorted.append(a[idx_a])
            idx_a+=1
    print(sorted)
scal(a,b)

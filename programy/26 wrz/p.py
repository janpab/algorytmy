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
# sortowanie kubełkowe z bąbelkowym 
def sort_kub2(tab, max_):
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
                for l in range(len(lista[k])-1-j):
                    if lista[k][l]>lista[k][l+1]:
                        tmp = lista[k][l+1]
                        lista[k][l+1] = lista[k][l]
                        lista[k][l] = tmp
                #print(idx, lista[k])
            while len(lista[k])!=0:
                lista_sorted.append(lista[k][0])
                del lista[k][0]
                
    print(lista_sorted,"sort kub 2")

#[[0], [3, 2], [], [6], [8], [9], [11, 11], [12, 13], [14], [], [18], []]

#sort_kub2(a, 20)


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
#scal(a,b)


'''
[... ,1,2,76,3,2,6,89,56,3,3, ...]
      ^        ^           ^ 
     idx_l     idx_m      idx_r

1 podlista      [idx_l, idx_m]
2 podlista      [idx_m+1, idx_r]

'''
tab = [6,3,2,1, 2,6,9,12,16,19, 6,13,15,17, 4,2]
# 2 89 3

# l1 - 2,6,9,12,16,19
# l2 - 6,13,15,17

def scal1(tab, idx_l, idx_m, idx_r):
    lista1 = tab[idx_l:idx_m+1]
    lista2 = tab[idx_m+1:idx_r+1]
    idx_1 = 0
    idx_2 = 0
    idx_s = idx_l
    while True:
        if idx_1 >= len(lista1):
            for i in range(idx_2 ,len(lista2)):
                tab[idx_s] = lista2[idx_2]
                idx_2 +=1
                idx_s +=1
            break
        if idx_2 >= len(lista2):
            for k in range(idx_1, len(lista1)):
                tab[idx_s] = lista1[idx_1]
                idx_1+=1
                idx_s+=1
            break
        if lista1[idx_1]< lista2[idx_2]: ###
            tab[idx_s] = lista1[idx_1]
            idx_s += 1
            idx_1+=1
        else:
            tab[idx_s] = lista2[idx_2]
            idx_s +=1
            idx_2 +=1
#    print(tab)
    



#scal1(tab, 4, 9, 13)

tab = [6,3,2,1,2,6,19,2,6, 29,6,3,15,17,4,2]

# sortowanie_scalanie(left)
# sortowanie_scalenie(right)
# scal1(left, right)


def sortowanie_scalanie(tab, idx_l=0, idx_r=None):
    if idx_r is None:
        idx_r = len(tab) - 1
    
    if idx_r <= idx_l:    #warunek zakończenia - jednoelementowa tablica
        return 
    
    idx_m = (idx_l + idx_r) // 2
    sortowanie_scalanie(tab, idx_l, idx_m)          # sortowanie lewej częsci
    sortowanie_scalanie(tab, idx_m+1, idx_r)        # sortowanie prawej częsci

    scal1(tab, idx_l, idx_m, idx_r)                 # scalenie lewej i prawej części

        

print(tab)
sortowanie_scalanie(tab)
print(tab)



# a = [2,3,4]

# def fun(x):
#     x[0] = 0

# fun(a)
# print(a)

# sortowanie przez scalanie iteracyjnie
# rozmiar tablicy = 2**N
# [1, 6   ,8, 4,    2, 5,    8, 0]
# [1,6 ,4,8, 2,5, 0,8] # scalanie

# [1,6 ,4,8,     2,5, 0,8] 
# [1,4,6,8,      0,2,5,8] # scalenie

# [0,1,2,4,5,6,8]



# sortowanie szybkie - quicksort

'''
pivot = 5
[5,6,4,5,2,7,9]
 i       j
tab[i] >= pivot     pivot <= tab[j]

[2,6,4,5,5,7,9]
   i   j

[2,5,4,6,5,7,9]
     j i



'''


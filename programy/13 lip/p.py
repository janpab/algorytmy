# s = 'gsgdyernsduvsduiwuiweia'
# x = set()
# print("To",x)
# y = [[liter, x.add(liter)] for liter in s if liter not in x]# gdy nie w x litery dodaje do y litere do x(stos) i do y litere
# print("y -------------",y)
# print("x -------------",x)
# x_str = [el[0] for el in y] #pierwsze elementy z listy dodaje do x_str
# print("przed joinem",x_str) # w tablicy
# a = ''.join("po joinie",x_str) # łączy 
# print(a)

# #print(list(enumerate(s)))

'''
10. Matura maj 2016, Zadanie 1.2 Liczby skojarzone

Dwie różne liczby całkowite a i b większe od 1 nazwiemy skojarzonymi,
jeśli suma wszystkich różnych dodatnich dzielników a mniejszych od a jest równa b+1,
a suma wszystkich różnych dodatnich dzielników b mniejszych od b jest równa a+1.

Dana jest liczba całkowita a większa od 1. Ułóż i zapisz w wybranej przez siebie notacji 
algorytm, który znajdzie i wypisze liczbę b skojarzoną z a lub komunikat „NIE”, jeśli taka
liczba nie istnieje.
W zapisie algorytmu możesz korzystać tylko z następujących operacji arytmetycznych: 
dodawania, odejmowania, mnożenia, dzielenia całkowitego i obliczania reszty z dzielenia.
Uwaga: Przy ocenie algorytmu będzie brana pod uwagę liczba operacji arytmetycznych wykonywanych przez Twój algorytm.

n = i*m     => m = n/i


16      sqrt(4)
1   16
2   8
4   4   == sqrt(16)

16 
1 1 
2 2 
3 3 
4 4
5 5 #


140, 195
'''
def suma_dzielnikow(n):
    suma = 0
    i=1          
    while i*i <=n: #     while i*i <= n      i <= sqrt(n)
        if n % i == 0:
            suma+=i
            if i*i != n and n/i != n:
                suma += n / i
        i+=1
        
    return suma
    
def licz_skojarz(a):
    b= suma_dzielnikow(a)-1
    if a==(suma_dzielnikow(b)-1):
        print(b)
    else:
        print("NIE")

licz_skojarz(140)

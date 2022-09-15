'''
Napisz funkcję, która sprawdza, czy dana liczba jest liczbą doskonałą.
Liczba doskonała to liczba naturalna, która jest sumą wszystkich 
swych dzielników właściwych (to znaczy od niej mniejszych).
np.: 6=3+2+1, 28=14+7+4+2+1
'''
from math import sqrt
#i <= sqrt(n)
#print(int(sqrt(28)+1))
#1   28/1=28
#2   28/2=14
#4   28/4=7



# 16
# 4     16/4=4


# A = k*n => A/k = n
def dzielniki(n):
    suma = 0
    for i in range(1, int(sqrt(n))+1):
        if n%i ==0:
            suma+=i
            if n/i != i and n/i != n: #nie jest tą samą liczbą i nie jest powtarzającą się liczbą to 
                suma += n/i   # dodajemy tę liczbędo sumy
    return suma == n        
print(dzielniki(28))
#print(dzielniki(7))


'''
Napisz funkcję obliczającą NWD (największa liczba naturalna dzieląca każdą z nich) dwóch danych liczb.
Napisz osobne funkcje używając algorytmu Euklidesa w dwóch wersjach: z odejmowaniem, z dzieleniem.
Dla obu powyższych wersji algorytmu napisz osobne funkcje realizujące algorytm: iteracyjnie, rekurencyjne.
'''

# Jeżeli A>B i A%k == 0 i B%k == 0, to (A-B)%k == 0, koniec gdy A == B, NWD=A
# Jeżeli A%k == 0 i B%k == 0, to (A%B)%k == 0, koniec gdy B == 0, NWD=A

# 15, 3
# 15-3=12   12,3
# 9,3
# 6,3
# 3,3
def nwd(a, b):
    while a!=b:
        if a>b:
            a = a-b
        if b>a:
            b = b-a
    print(a)
#nwd(15,3)
def nwd(a,b):
    #kiedy sie konczy
    if a == b:
        return a
    # wywołania rekurencyjnie
    else:
        if a>b:
            return nwd(a-b, b)
        if b>a:
            return nwd(a, b-a)

def nwdm(a,b):
    while b != 0:
        c = a%b
        a = b
        b = c
        print(a,b)
    print("Koniec: ",a)
#nwdm(25,15)

def nwdmr(a,b):
    if b == 0:
        return a
    else:
        return nwdmr(b, a%b)

print(nwdmr(15,3))


'''
Napisz funkcję obliczającą NWW (najminejsza wspólna wielokrotność) dwóch danych liczb.

'''
# NWW(a, b) * NWD(a, b) = a * b
# NWW = a * b / NWD

def nww(a,b):
    return a * b /nwdmr(a,b)
print(nww(3,5))



'''
Napisz funkcję obliczającą silnię z danej liczby przekazanej w parametrze.
0! = 1, 
n! = 1*2*3*...*n , dla n>=1
Napisz dwie osobne funkcje realizujące algorytm: rekurencyjne, iteracyjnie.
'''

# n! = n*(n-1)!

# 3     3*silnia(2)
# 2     2*silnia(1)
# 1     1*silnia(0)
# 0


def silnia(a):
    if a == 0:
        return 1
    else:
        return a*silnia(a-1)


'''
Napisz funkcję obliczającą wartość ciągu Fibonaciego dla liczby N przekazywanej w parametrze.
Ciąg Fibonacciego definiowany jest następująco:
F(0) = 0
F(1) = 1
F(N) = F(N-1) + F(N-2)
Napisz dwie osobne funkcje realizujące algorytm: rekurencyjne, iteracyjnie.
'''

def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        n_2 = 0
        n_1 = 1
        for i in range(2,a+1):
            n = n_1 + n_2
            n_2 = n_1
            n_1 = n
    print(n)
fib(9)
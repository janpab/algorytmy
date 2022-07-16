'''
Napisz funkcję, która sprawdza, czy dana liczba jest liczbą pierwszą
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

'''
Napisz funkcję zwracającą listę wszystkich liczb pierwszych mniejszych lub równych N
'''
n=100
#print([i for i in range(1,n+1) if czy_pierwsza(i)])

#[2, 3, 5, 7]  p <= n
'''
Napisz funkcję zwracającą listę N początkowych liczb pierwszych.
'''
n=10
#len([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 10
tab_pierwszych = []
i=1
while len(tab_pierwszych) < 10:
    if czy_pierwsza(i):
        tab_pierwszych.append(i)
    i+=1
#print(tab_pierwszych)


'''
Napisz funkcję zwracającą listę wszystkich liczb pierwszych mniejszych lub równych N. 
Implementację należy wykonać za pomocą algorytmu sita Eratostenesa.
'''
#[X, X, 2, 3, X, 5, X, 7, X, X, X]
def sito(n): #n =10 len=11
    a = [True for i in range(1,n+1)]
    a[0] = None
    a[1] = None
    for k in range(2, len(a)):
        if a[k] != None: #k =2, j = [4,6,8,10]
            for j in range(2*k, len(a), k):
                a[j] = None
    b = [idx for idx, el in enumerate(a) if el!=None]
    print(b)
#sito(100)
                
'''
Napisz funkcję zwracającą w postaci listy rozkład liczby N na czynniki pierwsze.
'''
#10 = 2*5
#30 = 2*3*5
#7 = 7
#8 = 2*2*2

#                 []          n = 30
# 30 / 2 = 15     [2]         n=15
# 15 / 3 = 5      [2, 3]      n=5
# 5 / 5 = 1       [2, 3, 5]   n=1 KONIEC

# 12 / 2  = 6
# 6 / 2   = 3
# 3 / 3   = 1


# sqrt(N)
from math import sqrt
def czyn_pierwsze(n):
    tab = []
    orig_n = n
    while n > 1:
        #for i in range(2, int(sqrt(n))+1):  # i <= sqrt(n)
        i = 2
        while i*i <= orig_n:
            while n % i == 0:
                tab.append(i)
                n = int(n/i)
            i += 1
    if n > 1:
        tab.append(n)
    print(tab)
czyn_pierwsze(81)
czyn_pierwsze(30)
czyn_pierwsze(25)
czyn_pierwsze(16)


            
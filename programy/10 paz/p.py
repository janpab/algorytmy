# https://pl.wikipedia.org/wiki/Metoda_r%C3%B3wnego_podzia%C5%82u#/media/Plik:Bisection_method.png

# y = x*x - 2   [0, 2]
from re import A


def f(x):
    return x-2 
    
# a * (10 ** b) ->  aeb
# 20000 -> 2e4
# 0.0005 -> 5e-4
def bisekcja(f, a, b, epsilon=1e-10):  # a < b
    while b-a>=epsilon:
        m = (a+b)/2
        if f(a)*f(m) < 0:#różnych znakow
            b = m
        else:
            a = m
        
    return (a+b)/2
#print(bisekcja(f,0,3))

# obliczanie pierwistawa z liczby metodą Newtona-Raphsona
# a, b      P=a*b
# a=N, b=1
# a=(a+b)/2     b=N/a

# a=2       b=1
# a=1.5     b=2/1.5=1.333
# a=1.416   b=2/1.41=1.418

# a-b < epsilon      warunek zakończenia
# return (a+b)/2


def pierwiastek(n, epsilon=1e-10):
    a = n
    b = 1
    while a-b > epsilon:
        a = (a+b)/2    
        b = n/a
    return (a+b)/2

print(pierwiastek(2))



# a*a*a*a*a     algorytm naiwny - złożoność O(n)
# 
# szybkie podnoszenie do potęgi - złożoność O(log n)
# a ** 0 => 1
# a ** 2k => (a ** k) ** 2      - wykładnik parzysty    
#   a_k = a**k             a**2k = a_k * a_k
#
# a ** (2k+1) => a * (a ** k) ** 2      - wykładnik nieparzysty   
#      a_k = a**k             a**(2k+1) = a * a_k * a_k
#  

def potega(a,pot):
    if pot == 0:
        return 1
    a_k = potega(a,pot//2)
    if pot%2 == 0:        
        return a_k *a_k
    else:         
        return a_k*a_k*a
    
    
print(potega(2,9))


# wersja iteracyjna
# a**10
# 10 = 1010
#
# wykładnik parzysty
# 1010 = 101 * 2
# a ** 1010 = a ** (2 * 101) = (a*a) ** 101
#
# wykładnik nieparzysty
# 101 = 10 * 2 + 1
# a ** 101 = a ** (10*2 +1) = (a*a) ** 10 * a
# a ** (c+1) = a**c * a**1


# w = 1
# dla każdego bitu wykładnika, od prawej do lewej
#   jesli 1 bit z prawej == 1       # wykładni nieparzysty
#       w = w * a
#   a = a * a


def potega_2(a,pot):
    
    w = 1
    while pot > 0:
        
        if pot % 2 == 1:
            w = w * a
            
        a = a*a
        pot = pot // 2
    return w 

print(potega_2(2,8))


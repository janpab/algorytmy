'''
Napisz funkcję, który wypisze podaną w parametrze liczbę naturalną w systemie binarnym. 
Rozwiąż zadany problem w dwóch wersjach: iteracyjnie i rekurencyjnie.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby i odwrotnie.

12%2    0
6%2     0
3%2     1
1%2     1
0
1100
'''
def to_bin(a):
    bin= []
    while a!=0:
        if a%2==0:
            bin.append("0")
            a=a//2
        if a%2==1:
            bin.append("1")
            a=a//2
    bin.reverse()
    return "".join(bin)
print(to_bin(12))
    
'''
Napisz funkcję, który wypisze podaną w parametrze liczbę naturalną na napis
reprezentujący liczbę w systemiue pozycyjnym o podstawie p,
podstawa przekazywana jest w drugim parametrze, p <= 36.
Znaki reprezentujące cyfry większe od 10 odwzorowywane są za pomocą małych liter alfabetu.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby i odwrotnie.
'''
tab= {}
def to_base(a, p):
    base = []
    while a != 0:
        reszta = a % p
        if 0 <= reszta <= 9:
            base.append(chr(48 + reszta))
        else:
            base.append(chr(97 + (reszta - 10)))
        a //= p
    base.reverse()
    return "".join(base)

print(to_base(255, 16))


'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w systemie binarnym.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby.
'''

1100
# 0* 2**0 + 0 * 2**1 + 1 * 2**2 + 1 * 2**3
#bin ->int

def to_int(bin):
    potega=0
    suma = 0 
    for c in reversed(bin):
        suma += int(c) * 2**potega
        potega+=1
    return suma
print(to_int("1100"))


'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w dowolnym systemie pozycyjnym. Podstawa systemu przekazywana jest w drugim parametrze, p <= 36, 
Znaki reprezentujące cyfry większe od 10 odwzorowywane są za pomocą małych liter alfabetu.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby.
'''



def to_int(a, p):
    

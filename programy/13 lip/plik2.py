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
from curses.ascii import isdigit
from os import sep


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

print(to_base(1, 2),"bin")


'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w systemie binarnym.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby.
'''

# 1100
# 0* 2**0 + 0 * 2**1 + 1 * 2**2 + 1 * 2**3
#bin ->int

# def to_int(bin):
#     potega=0
#     suma = 0 
#     for c in reversed(bin):
#         suma += int(c) * 2**potega
#         potega+=1
#     return suma
# print(to_int("1100"))


'''
Napisz funkcję, która odczyta i przekonwertuje na liczbę (int) przekazany w parametrze napis reprezentujący 
liczbę naturalną w dowolnym systemie pozycyjnym. Podstawa systemu przekazywana jest w drugim parametrze, p <= 36, 
Znaki reprezentujące cyfry większe od 10 odwzorowywane są za pomocą małych liter alfabetu.
W zapisie programu nie możesz korzystać z funkcji języka konwertujących napisy na liczby.
'''
#

def to_int(a, p):# 2-9
    potega=0
    suma = 0 
    for c in reversed(a):
        if c.isdigit():
            suma += int(c) * p**potega
            potega+=1
        else:
            for k in range(0,33):
                if chr(97 + k) == c:
                    liczba_z_litery = 10+k

            suma += int(liczba_z_litery) * p**potega
            potega+=1

    return suma

print(to_int("66",8))



# 1     4
# 8     1
# 4 + 8 == 12

# 1     4     4   len(3)-1 = 2

# 16    8     1




'''
oct -> int
oct -> bin -> int

247

 2       4       7  
010   | 100  | 111
----------------
4 2 1 | 4 2 1 | 4 2 1    suma wag bitow to podstawa-1
                           
                                           hex F=15    podstawa -1 




010100111


hex -> int
hex -> bin -> int

C7A

   C         7         A 
1 1 0 0 | 0 1 1 1 | 1 0 1 0
8 4 2 1 | 8 4 2 1 | 8 4 2 1

1100 0111 1010

while dzielnik != (p/2)

dzielnik = 2
p    dzielnik
16 / 2  = 8     dzielnik *=2
16 / 4  = 4
16 / 8  = 2
16 / 16 = 1   





-----------------
bin => int  


def to_int(bin):
    potega=0
    suma = 0 
    for c in reversed(bin):
        suma += int(c) * 2**potega
        potega+=1
    return suma
print(to_int("1100"))
'''


# def to_bin2(a,p):
#     base = []
#     num = str(a)#"C7a"
#     for i in range(len(num)-1,-1,-1):# dla kazdego elementu z liczby 
#         print(num[i],len(num),"hello")
#         akt_liter = []
#         if num[i].isdigit(): #jesli jest to cyfra to oblicza cyfre na bin
#             print("if z number")
#             licz = int(num[i])
#             dzielnik = 2
#             suma = 0      #  a= C7A, p=16      mamy 7    16/2 = 8
#             while dzielnik <= p:  # 1. 16/2 = 8   
#                 if suma !=licz and suma + p//dzielnik<=licz:
#                     akt_liter.append("1")
#                     suma += p//dzielnik
#                 else:
#                     akt_liter.append("0")
#                 print("tick",p//dzielnik)
#                 dzielnik*=2
#             "".join(akt_liter)
#         else:# jesli jest to litera to konwertuje to na liczbę i pozniej na bin
#             print("if z liter")
#             for k in range(0,33):
#                 if chr(97 + k) == num[i]:
#                     liczba_z_litery = 10+k
#             print(liczba_z_litery," liczba_z_litery")
#             dzielnik = 2
#             suma = 0 
#             while dzielnik <= p:  # 1. 16/2 = 8   
#                 if suma !=liczba_z_litery and suma + p//dzielnik<=liczba_z_litery:
#                     akt_liter.append("1")
#                     suma += p//dzielnik
#                 else:
#                     akt_liter.append("0")
#                 print("tick",p//dzielnik)
#                 dzielnik*=2
#             "".join(akt_liter)
#         base.append(akt_liter)

#     if len(num)>2:
#         base.reverse()
#     return "".join(base)


# print(to_bin2("c",16))



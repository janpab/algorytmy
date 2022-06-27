t = input()
def isPalindrom(a):
    return a == a[::-1]

for i in range(int(t)):
    liczba = input()
    obliczenia = 0
    while not isPalindrom(liczba):
        liczba = str(int(liczba)+int(liczba[::-1]))
        obliczenia+=1
    print("%s %d"%(liczba,obliczenia))
def czy_pierwsza(liczba):# funkcja sprawdzajaca czy liczba jest pierwsza
    if liczba == 1: # 1 nie jest liczbą pierwszą
        return False
    if liczba == 2:#2 jest liczbą pierwsza
        return True 
    if liczba % 2 == 0:# wszystkie liczby podzielne przez 2 nie są liczbami pierwszymi 
        return False
    for i in range(3, int(liczba/2)+1):  
        if liczba % i == 0:
            return False
    return True



n = input()#sprawdza czy liczba jest pierwsza

for i in range(int(n)):
    liczba = input()#pobiera liczbe
    if czy_pierwsza(int(liczba)):# sprawdza za pomocą funkcji czy liczba jest pierwsza
        print("TAK")
    else: 
        print("NIE")
    
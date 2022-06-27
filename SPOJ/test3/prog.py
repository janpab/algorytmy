import sys

liczby= sys.stdin.readlines()

licznik = 0

index = 0

while licznik < 3:
    liczba = int(liczby[index].strip())

    if liczba == 42 and index>0 and int(liczby[index-1].strip()) != 42:
        licznik+=1
    
    print(liczba)

    index+=1

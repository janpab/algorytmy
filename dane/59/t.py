def tablica_cyfr(number):
    tablica = []
    liczby = str(number)

    for i in range(0,len(liczby)):
        tablica.append(liczby[i])
    return tablica

def check_power(number):
    power = 0
    tablica = tablica_cyfr(number)
    while len(tablica)!=1:
        power+=1
        wynik_mnozenia =1
        for i in range(len(tablica)):
            wynik_mnozenia *=int(tablica[i])
        tablica=tablica_cyfr(wynik_mnozenia)
    return power

print(check_power(678))
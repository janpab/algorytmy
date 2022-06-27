

# with open("liczby.txt") as f:
#     f.readlines()


    


#zadanie 1
def is_prime(number):
    if number<=1:
        return False

    if number ==2:
        return True
    
    if number % 2 ==0:
        return False
    
    for i in range(3, (number//2)+1):
        if number % i == 0:
            return False
    
    return True
def zadanie1():

    liczby = []

    with open("liczby.txt") as f: 
        liczby = f.readlines()

    licznik = 0
    

    for i in range(1000):
        liczba = int(liczby[i].strip())
        dzielniki = []
        for j in range(2,(liczba//2)+1):#sprawdzamy dzielniki, najwyższy dzielnik moze dopiero po podzieleniu naszej liczby przez 2
            if liczba%j == 0 and is_prime(j): #jeżeli liczba z pętli jest podzielna przez naszą liczbę bez reszty i jest liczbą pierwszą to 
                dzielniki.append(j) # dodajemy naszą liczbę do tablicy
                while liczba%j ==0: # kiedy liczba dzieli sie przez j 
                    liczba/=j # dzielimy liczbe przez j, zmniejszamy ją aby znalezc wszystkie dzielniki
            if liczba == 1:
                break       # kiedy liczba wynosi 1 to konczymy szukanie dzielnikow

        jest_parzysty = False
        for j in range(len(dzielniki)): # dla długości tablicy dzelnikow
            if dzielniki[j]%2==0: #jezeli ktorys z dzielnikow jest parzysty to 
                jest_parzysty = True # jest parzysty trye 
                break
        
        if len(dzielniki) == 3 and not jest_parzysty: # jezeli mamy 3 dzelniki i zaden z nich nie jest parzysty to 
            licznik+=1     # licznij zwieksza sie o 1

    print(licznik)# pokaz licznik
#zadanie 2
def is_palindrom(number):
    reverse_number = ""
    for i in range(len(str(number))-1, -1,-1):
        reverse_number += str(number)[i]
    reverse_number = int(reverse_number)
    if reverse_number == number:
        return True
    else:
        return False
def get_reverse(number):
    reverse_number = ''
    for i in range(len(str(number))-1, -1, -1):
        reverse_number += str(number)[i]
    
    return int(reverse_number)  
def zadanie2():
    liczby = []
    licznik = 0 #ile jest liczb dla ktorych suma danej liczby i liczby odwroconej jes palidromem
    with open("liczby.txt") as f: 
        liczby = f.readlines()

    for i in range(1000):
        liczba = int(liczby[i].strip())
        reverse_liczba = get_reverse(liczba)

        if is_palindrom(liczba+reverse_liczba):
            licznik+=1
        else:
            pass
    print("sumy z palindromem: ", licznik)
#zadanie 3
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
def zadanie3():
    liczby = []
    
    tablica_licznikow = [0, 0, 0, 0, 0, 0, 0, 0]


    minimalna = 9999999
    maksymalna = -9999999
    with open("liczby.txt") as f: 
        liczby = f.readlines()

    for i in range(1000):
        liczba = int(liczby[i].strip())
        
        print((str(i*0.1)[0:4])+"%")
        a = check_power(liczba)

        if a == 1:
            if liczba < minimalna:
                minimalna = liczba
            if liczba > maksymalna:
                maksymalna = liczba
        if a>0 and a<=8:
            tablica_licznikow[a-1]+=1

    for i in range(8):
        print("Ilosc ", i+1,"wynosi:", tablica_licznikow[i])
    print("najwieksza z 1 to:", maksymalna, "najmniejsza z 1 to:", minimalna)

zadanie3()



    


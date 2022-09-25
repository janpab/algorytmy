from re import L


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
    trojki = []
    with open("trojki.txt") as f:
        trojki = f.readlines()
    for i in range(1000):
        linia = trojki[i].strip()
        trojki1 = linia.split()
        wynik = int(trojki1[2])
        liczba1 = trojki1[0]
        liczba2 = trojki1[1]
        suma = 0
        for j in range(len(liczba1)):
            suma += int(liczba1[j])
        for k in range(len(liczba2)):
            suma += int(liczba2[k])
        if suma == wynik:
            print(linia) 
def zadanie2():
    trojki = []
    with open("trojki.txt") as f:
        trojki = f.readlines()
    for i in range(1000):
        linia = trojki[i].strip()
        trojki1 = linia.split()
        wynik = int(trojki1[2])
        liczba1 = int(trojki1[0])
        liczba2 = int(trojki1[1])
        if is_prime(liczba1) and is_prime(liczba2) and wynik==liczba1*liczba2:
            print(linia)
def zadanie3():
    trojki = []
    with open("trojki.txt") as f:
        trojki = f.readlines()

    para = False
    for i in range(1000):
        linia = trojki[i].strip()
        trojki1 = linia.split()
        
        a = int(trojki1[0])
        b = int(trojki1[1])
        c = int(trojki1[2])
        if para and c*c== a*a+b*b:
            print(trojki[i-1].strip())
            print(linia)
           
            print()
            para = False
            i+=1
        if c*c== a*a+b*b:
            para = True
        else:
            para = False
        
        

        
        
        
def zadanie4():
    trojki = []
    licznik = 0
    dlugosc_ciagu = 0
    najdluzszy_ciag = 0

    with open("trojki.txt") as f:
        trojki = f.readlines()
    for i in range(1000):
        linia = trojki[i].strip()
        trojki1 = linia.split()
        a = int(trojki1[0])
        b = int(trojki1[1])
        c = int(trojki1[2])

        if a + b >c and a + c >b and b+c >a:# to jest trojkat
            licznik += 1
            dlugosc_ciagu +=1
        else:
            if dlugosc_ciagu>najdluzszy_ciag:
                najdluzszy_ciag = dlugosc_ciagu
            dlugosc_ciagu=0
    print(najdluzszy_ciag, licznik)
print("Z1")
zadanie1()
print("Z2")
zadanie2()
print("Z3")
zadanie3()
print("Z4")
zadanie4()
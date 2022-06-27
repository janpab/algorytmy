import math
t = input()#testy

for i in range(int(t)):
    goscieIciastka = input()# liczbaGosci  liczbaCiastekwpudełku
    goscie = int(goscieIciastka.split(" ")[0])
    ciastka = int(goscieIciastka.split(" ")[1])

    doba = 86400
    suma = 0
    for j in range(goscie):#w zaleznosci od liczby gosci czas zjedzenia jednego ciastka
        sekundy = input()
        suma += doba//int(sekundy) #czas zjedzenia wszystkich ciastek w pudełku
    suma = suma / ciastka #czas zjedzenia pojedynczego ciastka w pudełku
    suma = math.ceil(suma)#zaokrąglenie
    print(suma)



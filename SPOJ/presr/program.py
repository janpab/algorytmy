t = input()#liczba testow

for i in range(int(t)):
    predkosci = input()#pobiera predkosci w formacie 30 40
    v1 = int(predkosci.split(" ")[0])#oddziela predkosci na 2 rozne liczby 
    v2 = int(predkosci.split(" ")[1])

    vsr = 2 * (v1*v2)/(v1 + v2)#oblicza predkosc srednia
    print(int(vsr))
import math
t = input()

for i in range(int(t)):
    line = input()
    tablica_liczb = line.split(" ")[1:]
    ilosc_liczb = len(tablica_liczb)
    suma = 0
    for j in range(ilosc_liczb):
        suma +=int(tablica_liczb[j]) #oblicza sume liczb potrzebnej do obliczenia sredniej
    srednia = suma/ilosc_liczb # srednia
    najblizsza = int(tablica_liczb[0])
    najblizsza_r = abs(srednia-najblizsza)
    for k in range(ilosc_liczb): # ? szuka najblizszej liczby z tablicy do sredniej
        c = abs(srednia - int(tablica_liczb[k]))
        
        if c < najblizsza_r:
            najblizsza_r = c
            najblizsza = tablica_liczb[k]

    print(najblizsza)



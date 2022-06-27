import sys
lines = sys.stdin.readlines()

def przesun(znak):
    numer_znaku = ord(znak)+3
    if numer_znaku > 90:
        numer_znaku -= 26
    
    return chr(numer_znaku)

for line in lines:
    line = line.strip()
    wynik = ""
    for i in range(len(line)):
        znak = line[i]
        if ord(line[i])>=65 and ord(line[i])<=90:
            #przesuwamy
            znak = przesun(line[i])
        wynik+=znak
    print(wynik)
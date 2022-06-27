t = input()

def getSkrocone(litera,ilosc):
    if ilosc == 1:
        return litera
    elif ilosc == 2:
        return litera + litera
    else:
        return litera + str(ilosc)

for i in range(int(t)):
    literki = input()

    skrocone = ""

    litera = literki[0]
    ilosc = 1
    for j in range(1,len(literki),1):
        if literki[j] == litera:
            ilosc +=1
        else:
            skrocone+=getSkrocone(litera,ilosc)
            litera = literki[j]
            ilosc = 1
    skrocone+=getSkrocone(litera,ilosc)
    print(skrocone)

def to_dec(num,podstawa): #int,int > int
    is_minus = False
    if num<0:
        is_minus = True
    num = str(num).replace('-','')
    wynik = 0
    mnoznik = 1
    for i in range (len(num)-1,-1,-1):
        wynik+=int(num[i])*mnoznik
        mnoznik*=podstawa
    if is_minus:
        return wynik * -1
    else:
        return wynik
        


def konwertuj(num,podstawa,docelowy): #int,int,int > int
    dec = to_dec(num,podstawa)
    
    is_minus = False
    if dec<0:
        is_minus = True
        dec*=-1
    
    wynik = ""

    while dec!=0:
        wynik = str(dec%docelowy) + wynik
        dec = dec//docelowy
    
    if is_minus:
            return int(wynik) * -1
    else:
        return int(wynik)









print(konwertuj(3321,4,9))


print(konwertuj(-101,2,4))

#print(to_dec(-3321,4))
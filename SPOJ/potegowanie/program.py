t = input()

cykle = [
    [0],#0
    [1],#1
    [2,4,8,6],#2
    [3,9,7,1],#3
    [4,6],#4
    [5],#5
    [6],#6
    [7,9,3,1],#7
    [8,4,2,6],#8
    [9,1]#9
]

for i in range(int(t)):
    liczby = input()
    podstawaPot = str(liczby.split(" ")[0])
    wykladPot = int(liczby.split(" ")[1])
    ost_cyfra = int(podstawaPot[len(podstawaPot)-1])# podstawa pot ="200" OST CYFRA = 3-1 = 2   "200"[2] =0 
    dlugosc_cyklu = len(cykle[ost_cyfra])#len(cykle) = 10 
    indeks = (wykladPot % dlugosc_cyklu) - 1
    print(cykle[ost_cyfra][indeks])

    

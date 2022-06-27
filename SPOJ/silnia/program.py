t = input() #ilość testów

SILNIE = ["0 1","0 1","0 2","0 6","2 4","2 0","2 0","4 0","2 0","8 0"]#możliwe końcówki liczb do 10

for i in range(int(t)):
    n = input()#silnia
    if int(n)<10:#Jeżeli silnie miejsza od 10
        print(SILNIE[int(n)])# to wybieram koncowke silni z tablicy
    else:#w przeciwnym wypadku końcówka wnosi 00
        print("0 0")

t = input()

for i in range(int(t)):
    liczby = input().split(" ")[1:]#liczby bez pierwszej wpisanej
    wynik = ""
    for i in range(1,len(liczby),1):
        wynik += liczby[i] + " "
    print(wynik + liczby[0])
    


    
    
    
t = input()# liczba testów

for i in range(int(t)): #robi tyle razy ile wpiszemy w konsoli
    suma = 0
    n = input() #ilość liczb w linii
    liczby_w_linii = input() #liczby w linii
    liczby = liczby_w_linii.split(' ') #zamienia liczby w lini na osobne liczby
    for j in range(int(n)): #sumuje liczby w linii
        suma+=int(liczby[j])
    print(suma)

    


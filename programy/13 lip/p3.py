def to_int(a, p):# 2-9
    potega=0
    suma = 0 
    for c in reversed(a):
        if c.isdigit():
            print(c)
            suma += int(c) * p**potega
            potega+=1
        else:
            for k in range(0,33):
                if chr(97 + k) == c:
                    liczba_z_litery = 10+k
            print(c,"literka", liczba_z_litery)

            suma += int(liczba_z_litery) * p**potega
            potega+=1

    return suma

print(to_int("c7a",16))
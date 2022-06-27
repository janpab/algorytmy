liczby = input().split(" ")

a = float(liczby[0])
b = float(liczby[1])
c = float(liczby[2])

if a == 0:
    if b == c:
        print("NWR")
    else:
        print("BR")
else:
    print("%.2f" % round(((c-b)/a),2))





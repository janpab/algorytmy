import sys

zestawy = sys.stdin.readlines()

for liczby in zestawy:

    liczby = liczby.strip()
    a = float(liczby.split(" ")[0])
    b = float(liczby.split(" ")[1])
    c = float(liczby.split(" ")[2])

    delta = (b*b) - (4 * a * c)

    if delta > 0:
        print(2)
    elif delta == 0:
        print(1)
    else:
        print(0)
    
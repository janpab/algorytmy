import sys

dzialania = sys.stdin.readlines()

rejestr = [0]*10

for dzialanie in dzialania:
    f = dzialanie.split(' ')[0]
    l1 = int(dzialanie.split(" ")[1])
    l2 = int(dzialanie.split(" ")[2].strip())

    if f == "z":
        rejestr[l1] = l2
    else:
        if f == "/":
            f = "//"
        print(eval("rejestr[%d]%srejestr[%d]" % (l1,f,l2)))


import sys
def kalkulator(a,b,c):
    if (a == "+"):
        return b + c
    elif (a == "-"):
        return b - c
    elif (a == "*"):
        return b * c
    elif (a == "/"):
        return b//c
    elif (a == "%"):
        return b%c

lines = sys.stdin.readlines()

for line in lines:
    a = str(line.split(" ")[0])
    b= int(line.split(" ")[1])
    c = int(line.split(" ")[2].strip())
    print(kalkulator(a,b,c))




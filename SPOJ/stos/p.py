import sys

def stosdzialanie():
    pass

lines = sys.stdin.readlines()
stos = []

i = 0

while i<len(lines):
    dzialanie = lines[i].strip()
    if dzialanie == "+": #plus
        i+=1
        liczba = lines[i].strip()
        if len(stos)>=10:
            print(":(")
        else:
            stos.append(liczba)
            print(":)")
    else: #minus
        if len(stos) == 0:
            print(":(")
        else:
            print(stos[len(stos)-1])
            stos.pop()
    i+=1

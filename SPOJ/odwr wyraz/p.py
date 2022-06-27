import sys

def odwrocone(wyraz):
    odwr = ""
    for i in range (len(wyraz)-1,-1,-1):
        odwr += wyraz[i]
    return odwr

lines = sys.stdin.readlines()

for line in lines:
    wyraz = line.strip()
    print(odwrocone(wyraz))
    

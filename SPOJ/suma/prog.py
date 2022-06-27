import sys
suma = 0
lines = sys.stdin.readlines()

for i in range(len(lines)):
    
    a = int(lines[i].strip())
    suma += a
    print(suma)
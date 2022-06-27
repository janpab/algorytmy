import sys

#a<b+c
#b<a+c
#c<b+a

lines= sys.stdin.readlines()

for line in lines:
    numbers = line.split(" ")
    a = float(numbers[0].strip())
    b = float(numbers[1].strip())
    c = float(numbers[2].strip())

    if a<b+c and b<a+c and c<b+a:
        print(1)
    else:
        print(0)
    
    
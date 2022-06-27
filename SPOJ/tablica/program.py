t = input()

for i in range(int(t)):
    s = input()
    xn = int(s)
    n = 0
    while xn!=1:

        n +=1
        if xn %2 == 0:
            xn = xn //2 
        else:
            xn = 3 * xn +1
    print(n)
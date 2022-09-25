def write_fib(n):
    tab = [[],[]]
    tab[1] = 1
    tab[1] = 1
    print(tab)
    for i in range(1,n+1):
        tab[0].append(i)
    for j in range(2,n):
        tab[1].append(tab[1][n]+tab[1][n-1])
    return tab

print(write_fib(10))

        
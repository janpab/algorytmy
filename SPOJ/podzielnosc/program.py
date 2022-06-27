t = input()

for i in range(int(t)):
    linia = input()

    n = int(linia.split()[0])
    x = int(linia.split()[1])
    y = int(linia.split()[2])

    for j in range(1, n, 1):
        if j%x==0 and j%y!=0:
            print(j,end=" ")
    print('')
    
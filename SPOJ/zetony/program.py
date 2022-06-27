def nwd(a, b):
    while b:
        a, b = b, a%b
    return a


t = input() #testy

for i in range(int(t)):
    zetony = input() 
    a = int(zetony.split(" ")[0])
    b = int(zetony.split(" ")[1]) 

    print(nwd(a,b)*2)
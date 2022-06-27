def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a



t = input()

for i in range(int(t)):
    c = input()

    xyz = int(c.split(" ")[0])
    abc = int(c.split(" ")[1])

    print(nwd(xyz, abc))



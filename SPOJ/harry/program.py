t = input()

for i in range(int(t)):
    ckw = input()
    c = int(ckw.split(" ")[0])
    k = int(ckw.split(" ")[1])
    w = int(ckw.split(" ")[2])

    if (c * w > k):
        print("no")
    else:
        print("yes")
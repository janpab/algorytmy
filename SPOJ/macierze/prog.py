kolIwier = input().split(" ")

n = int(kolIwier[0])
m = int(kolIwier[1])

t = []

for i in range(n):
    t.append(input().split(" "))

for i in range(m):
    for j in range(n):
        print(t[j][i], end=" ")
    print()
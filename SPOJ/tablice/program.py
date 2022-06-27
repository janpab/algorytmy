t=input()

for i in range(int(t)):
    line = input()
    tablica = line.split(' ')
    rewers = ""
    for j in range(len(tablica)-1,0,-1):
        rewers+=tablica[j]+ " "
    print(rewers)
    
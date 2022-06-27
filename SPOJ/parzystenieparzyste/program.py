t = input()

for i in range(int(t)):
    liczby = input()

    liczby = liczby.split(' ')[1:]
    parzyste = ""
    nparzyste = ""
    for j in range(len(liczby)):
        if ((j+1)%2 ==0):
            parzyste+=str(liczby[j])+" "
        else:
            nparzyste+=str(liczby[j])+" "
    print(parzyste+nparzyste)
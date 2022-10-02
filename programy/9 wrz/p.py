a = [5,3,1,2,4]
#czy wystepuje, 1 index
def tab(a,tab):
    for i in range(len(tab)):
        if tab[i] == a:
            return i
    return -1

tab = [1,2,3,4,5,6,7,9,10]
#przeszukiwanie binarne
def prz_bin(tab,a):
    idx_l = 0
    idx_r =len(tab)-1
    
    while True:
        idx = (idx_l+idx_r)//2
        if tab[idx]==a:
            return idx
        if tab[idx]<a:
            idx_l = idx+1
        if tab[idx]>a:
            idx_r = idx-1
        if idx_r < idx_l:
            return -1
    
#print(prz_bin(tab, 10))
#sortowanie bąbelkowe
a = [5,3,1,2,4]
# a = [3,5,1,2,4]
# a = [3,1,5,2,4]
# a = [3,1,2,5,4]
# a = [3,1,2,4,5]

def sort_bab(tab):
    for i in range(len(tab)):#wszystkie przebiegi
        for k in range(len(tab)-1):#1 przebieg    
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1] = tab[k]
                tab[k] = tmp
    print(tab)
#sort_bab(a)


def sort_bab2(tab):
    for i in range(len(tab)):#wszystkie przebiegi
        for k in range(len(tab)-1-i):#1 przebieg    
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1] = tab[k]
                tab[k] = tmp
                
    print(tab)
#sort_bab2(a)

#sortowanie przez wstawianie
a = [5,   3,1,2,4]
# a = [3,5,   1,2,4]
# a = [1,3,5,   2,4]
# a = [1,2,3,5,   4]
# a = [1,2,3,4,5   ]

def sort(tab):
    for i in range(len(tab)-1):
        ### wyszukiwanie liniowe
        for k in range(i+1):
            if tab[k]>tab[i+1]:
                idx= k
                num = tab[i+1]
                break
        ###
        for j in range(i,k-1,-1):
            tab[j+1] = tab[j]
        tab[idx]= num
    print(tab,"sort")
#sort(a)

        #zad dom funkcja sortowanie przez wstawianie,zamiast liniowego wyszukiwanie binarne 


# a = [3,5,   1,2,4]
# a = [1,3,5,   2,4]
# a = [1,2,3,5,   4]
# a = [1,2,3,4,5   ]

a = [5,3,1,2,4]



def sort_bin(tab):
    for i in range(len(tab)-1):
        ### wyszukiwanie liniowe
        #for k in range(i+1):
        #    if tab[k]>tab[i+1]:
        #        idx= k
        #        num = tab[i+1]
        #        break
        ###
        
        num = tab[i+1]
        idx_l = 0 
        idx_r = i
        while True:
            idx = (idx_l+idx_r)//2
            if tab[idx]==num:
                break
            if tab[idx]<num:
                idx_l = idx+1
            if tab[idx]>num:
                idx_r = idx-1
            if idx_r < idx_l:
                idx = idx_l
                break
        for j in range(i,idx-1,-1):#1 w prawo
            tab[j+1] = tab[j]
        tab[idx]= num
        print(tab,"sort bin")
sort_bin(a)

# sortowanie przez wyszukiwanie

# a = [3,5,1,2,4]           
# a = [1, 3,5,2,4]      i=1, idx=3      [3,2]
#tab[3] = tab[2]
#tab[2] = tab[1]

# a = [1,2, 3,5,4]
# a = [1,2,3, 5,4]
# a = [1,2,3,4, 5]


def sort_wyszuk(tab):

    for i in range(len(tab)): #1 prawa czesc
        min = tab[i]
        idx = i #najmniejszy
        for k in range(i,len(tab)):
            if tab[k]<min:
                min = tab[k]
                idx = k
        for j in range(idx,i,-1):
            tab[j] =  tab[j-1]  
        tab[i] = min
    print(tab,"sort wyszuk")
sort_wyszuk(a)


#MAJ 2019 cz1 zad 1
#jaś - parzyste
#
tab = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

def wysz_bin(tab):
    idx_l = 0
    idx_r = len(tab)-1
    while True:
        idx_m = (idx_l+idx_r)//2
        if tab[idx_m]%2 == 0:
            idx_r = idx_m
        else:
            idx_l = idx_m+1
        if idx_l==idx_r:
            return tab[idx_l]
print(wysz_bin(tab),"wysz bin j i m")


# matura maj 2017 zad. 1.2
# matura czerwiec 2016 zad. 2 dziwny porządek 






#ZAD 1.2 Prostokąt maj 2017

#sortuje tablicę
def sort_bab2(tab):
    for i in range(len(tab)):#wszystkie przebiegi
        for k in range(len(tab)-1-i):#1 przebieg    
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1] = tab[k]
                tab[k] = tmp
                
    return(tab)
#znajduje 2 najwieksze nie podzielne przez p 
#złożoność binarna
def prz_bin_do_zad(tab,p):
    idx_l = 0
    idx_r =len(tab)-1
    maxi1 = 0
    maxi2 = 0
    while True:
        idx = (idx_l+idx_r)//2
        # if tab[idx]==a:
        #     return idx
        if tab[idx]%p!= 0:# jeżeli ta liczba jest nie podzielna to szukamy jeszcze wiekszej nie podzelnej po prawej
            if maxi1<tab[idx]:
                maxi1 = tab[idx]
            elif maxi2< tab[idx]:
                maxi2 = tab[idx]
            idx_l = idx+1
 
        if tab[idx]%p == 0: # jeżeli tafiamy na liczbe podzielną przez p to najwieksza podzielna moze byc i po prawej i po lewej
            pass
        if idx_r < idx_l:
            return maxi1, maxi2
        if idx_l > idx_r:
            return maxi1,maxi2
#złożoność liniowa
def szuk_prostok(tab, p):
    max1 = 0
    max2 = 0
    for i in range(len(tab)-1):
        if tab[i]>max1 and tab[i]%p != 0:
            max2 = max1
            max1 = tab[i]
        elif tab[i]>max2 and tab[i]%p != 0:
            max2 = tab[i]
        
    print("prostokąt: ", max1,max2)


p = 7
ab = [6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18]
#prz_bin(ab, )
s_ab = sort_bab2(ab)
#print(s_ab)
#[4, 5, 6, 7, 8, 9, 10, 12, 14, 18, 28]
#print(prz_bin_do_zad(ab,7))


szuk_prostok(ab, p)



#zad 3 matura czerwiec 2016
#znajduje najmniejszą nieparzystą lub najwiekszą parzystą
min_np = 0
max_parz= 0 
t = [ 3, 6, 8, 11, 15, 20, 35, 70, 100, 1000]
for i in range(len(t)-1):
    liczba = tab[i]
    if liczba % 2 == 0:
        if liczba > max_parz:
            max_parz = liczba
    else:
        if liczba < min_np:
            min_np = liczba

if min_np != 0:
    print(min_np)
else:
    print(max_parz)

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
print(wysz_bin(tab))


# matura maj 2017 zad. 1.2
# matura czerwiec 2016 zad. 2 dziwny porządek 

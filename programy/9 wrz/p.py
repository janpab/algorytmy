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
print(prz_bin(tab, 10)
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
sort_bab(a)


def sort_bab2(tab):
    for i in range(len(tab)):#wszystkie przebiegi
        for k in range(len(tab)-1-i):#1 przebieg    
            if tab[k] > tab[k+1]:
                tmp = tab[k+1]
                tab[k+1] = tab[k]
                tab[k] = tmp
                
    print(tab)
sort_bab2(a)

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
sort(a)

        #zad dom funkcja sortowanie przez wstawiania,zamiast liniowego wyszukiwanie binarne 




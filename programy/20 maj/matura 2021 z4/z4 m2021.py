




def zad41():
    instrukcje =[]
    with open('instrukcje.txt') as f:
        instrukcje = f.readlines()

    #instrukcje2 =[]
    #for el in instrukcje:
    #    instrukcje2.append(el.strip())
    #print(instrukcje2)  


    instrukcje2 = [el.strip() for el in instrukcje]
    ilosc_dopisz = 0
    ilosc_usun = 0
    for el in instrukcje2:
        print(el.split())
        ins, par = el.split() 
        if ins == 'DOPISZ':
            ilosc_dopisz +=1
        if ins == 'USUN':
            ilosc_usun +=1

    #ilosc_dopisz  = len([el.split()[0] for el in instrukcje if el.split()[0] == 'DOPISZ'])
    
    print(ilosc_dopisz-ilosc_usun)
    
#zad41()

def zad42():
    instrukcje =[]
    with open('instrukcje.txt') as f:
        instrukcje = f.readlines()
    instrukcje2 = [el.strip() for el in instrukcje]
    lista = []   #długośc podciągu
    licznik = 1
    ins = None
    for el in instrukcje2:
        if el[0] == ins:
            licznik += 1
        else:
            ins = el[0]
            lista.append(licznik)
            licznik = 1


    print(max(lista))

def zad43():
    instrukcje =[]
    with open('przyklad.txt') as f:
        instrukcje = f.readlines()
    instrukcje2 = [el.strip().split() for el in instrukcje]
    
    x = {}
    for el in instrukcje2:
        #print(el, el[0], el[0] == 'DOPISZ')
        if el[0] == 'DOPISZ':
            
            literka = el[1]
            #print(el, literka)
            if literka in x:
                x[literka] += 1
            else:
                x[literka] = 1
    #max(x)

    print(x)  
    ilosc, literka =  max([[v, k] for k, v in x.items()])#
    a, b = [3, 'U']
    print(literka)
    

    tuple()
    lista = [1, 2, 3]
    krotka = (1, 2, 3)


def zad44():
    instrukcje =[]
    with open('instrukcje.txt') as f:
        instrukcje = f.readlines()
    instrukcje2 = [el.strip().split() for el in instrukcje]
    #alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z']
    from string import ascii_uppercase
    #from string import ascii_lowercase
    alfabet = list(ascii_uppercase)

    napis = []
    for el in instrukcje2:
        
        if el[0] =='DOPISZ':
            napis.append(el[1])
        elif el[0] =='USUN':
            #napis.remove(napis[-1])
            napis.pop()
        elif el[0] == 'ZMIEN':
            napis[-1]=el[1]
        elif el[0] == 'PRZESUN':
            litera = el[1]
            zamiana = ''    #literka na ktorą przesuniemy
            if el[1] == 'Z':
                zamiana = 'A'
            else:
                #for i in range(len(alfabet)):
                #    if alfabet[i] == el[1]:
                #        zamiana = alfabet[i+1]
                idx = alfabet.index(el[1])
                zamiana = alfabet[idx+1]
                        
            # for lit in napis:
            #     if lit == el[1]:
            #         print(lit)
            #         lit = zamiana
            #         print(lit)
            
            #for k in range(len(napis)): #!!!!!!!!
            #    if napis[k] == el[1]:
            #        napis[k] = zamiana
            #        break
            idx = napis.index(el[1])#na ktorym miejscu wys dany element
            napis[idx] = zamiana
    #napis_s = ''
    #for els in napis:
    #    napis_s+=els
    napis_s = ''.join(napis)#stringi w liscie -> string

    print(napis_s)
zad44()
    

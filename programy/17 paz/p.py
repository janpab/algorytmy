# szyfry podstawieniowe
# szyfr Cezara

# ord('a') => kod ascii
# chr(kod_ascii) => literka
print(ord('a')) #97
print(ord('z'))#122
def szyfruje(a,k):
    a_ch =[]
    for ch in a:
        if ord(ch) + k >= ord('z'):
            b = ord(ch)+k-(ord('z')-ord('a')+1)
            print(ord(ch),k,ord('z'),ord('a')+1)
        else:
            b = ord(ch)+k
            
        a_ch.append(chr(b))
    return "".join(a_ch)
#z 122 2 122 98
#z ord('z') k 122-97+
# 122 +2 - 35
#124 -35
print(szyfruje("zrogram",2), "TO")
            
def deszyfruje(a,k):
    a_ch =[]
    for ch in a:
        if ord(ch) - k < ord('a'):
            b = ord(ch)-k+(ord('z')-ord('a')+1)
        else:
            b = ord(ch)-k
            
        a_ch.append(chr(b))
    return "".join(a_ch)
    
print(deszyfruje("rtqitco",2))


alfabet = '''aąbcćdeęfghijklmnńoópqrsśtuvwxyzźżAĄBCĆDEĘFGHIJKLMNOÓPQRSŚTUVWXYZŹŻ0123456789'''

# print("eeeo",[i for i in range (len(alfabet)) if alfabet[i]=="9"])

def szyfruje_alf(a,k):
    a_ch =[]
    ostatni_idx = [i for i in range (len(alfabet)) if alfabet[i]=="9"]
    ostatni_idx = int(ostatni_idx[0])
    for ch in a:
        idx_ch = [i for i in range (len(alfabet)-1) if alfabet[i]==ch]
        idx_ch = int(idx_ch[0])
        if idx_ch + k >= ostatni_idx:            
            b = idx_ch+k-len(alfabet)    # b = ord(ch)+k-(ord('z')-ord('a')+1)
        else:
            b = idx_ch+k
            
        a_ch.append(alfabet[b])
    return "".join(a_ch)
print('szyfruje_alf',szyfruje_alf("program",2))

def deszyfruje_alf(a,k):
    a_ch =[]
    ostatni_idx = [i for i in range (len(alfabet)) if alfabet[i]=="9"]#76
    ostatni_idx = int(ostatni_idx[0])
    for ch in a:
        idx_ch = [i for i in range (len(alfabet)-1) if alfabet[i]==ch]
        idx_ch = int(idx_ch[0])
        
        if idx_ch + k > ostatni_idx:
            b = idx_ch-k+len(alfabet)
        else:#OK
            b = idx_ch-k
   
        a_ch.append(alfabet[b])
    return "".join(a_ch)

print('deszyfruje_alf',deszyfruje_alf("rśpiśbń",2))


# szyfr permutacyjny
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
klucz = 'YPDARFBLWQETZGSVIMKHNXJUOC'    # dowolna permutacja alfabetu


a ={'A':'Y',
    }
def permutacja_szyfruje(klucz, wyraz):
    a = {}
    b=[]
    for i in range(len(alfabet)):
        a [alfabet[i]] = klucz[i]
    for el in wyraz:
        b.append(a[el])
    return "".join(b)

print(permutacja_szyfruje(klucz, "PROGRAM"))

def permutacja_deszyfruje(klucz,wyraz):
    a = {}
    b=[]
    for i in range(len(alfabet)):
        a [klucz[i]] = alfabet[i]
    for el in wyraz:
        b.append(a[el])
    return "".join(b)
print(permutacja_deszyfruje(klucz, "VMSBMYZ"))

#
# SZYFRY PRZESTAWIENIOWE
#

# przestawiamy litery parzysta z nieparzystą

# PR OG RA M
# RP GO AR M

def szyfr_przestawieniowy(wyraz):
    a = []

    for i in range(0,len(wyraz),2):
        if i <len(wyraz)-1:
            a.append(wyraz[i+1])
        a.append(wyraz[i])
        
    return "".join(a)
print(szyfr_przestawieniowy("PROGRAM0"))
print(szyfr_przestawieniowy("RPGOAR0M"))


# szyfr kolumnowy
str = 'tekstdozaszyfrowania12'

# teks
# tdoz
# aszy
# frow
# ania
# 12
chr(0)
# ttafaedstn ...

def kolumnowy(wyraz, kol):
    a = []
    odp = []
    for k in range(len(wyraz)):
        if k%kol == 0:
            b = [wyraz[k]]
            a.append(b)
        else:
            b.append(wyraz[k])
    for i in range(kol):
        for j in range(len(a)):
            if i < len(a[j]):
                odp.append(a[j][i])
            
    return "".join(odp)
    #print(a)

print(kolumnowy(str, 4))   

# ttafa1
# edsrn2
# kozoi
# szywa
# ttafa1
# edsrn2
# kozoi
# szywa

#len(wyraz) - (len(wyraz) // kol )*kol
# len(wyraz) % 4
a =len('tekstdozaszyfrowania12') % 4
print(a)

def kolumnowy(wyraz, kol):
    a = []
    odp = []
    ilosc_w_ostatniej_kol = 0
    max_ostatnia_kolumna = len(wyraz) % kol
    kol += 1
    for k in range(len(wyraz)):
        if (k%kol == 0) or (k%kol == kol-1 and ilosc_w_ostatniej_kol > max_ostatnia_kolumna):
            b = [wyraz[k]]
            a.append(b)
        else:
            if k%kol == kol-1:
                ilosc_w_ostatniej_kol += 1
            b.append(wyraz[k])
    print(a)
    
kolumnowy('ttafa1edsrn2kozoiszywa', 4)
# teks
# tdoz
# aszy
# frow
# ania
def szyfruj_kol(tekst, num_k):
    num_w = len(tekst) // num_k + 1
    szyfr = []
    for ik in range(num_k):
        for iw in range(num_w):
            idx = iw*num_k + ik
            if idx < len(tekst):
                szyfr.append(tekst[idx])
    return ''.join(szyfr)

print(szyfruj_kol('tekstdozaszyfrowania12', 4))



def deszyfruj_kol(szyfr, num_k):
    num_w = len(szyfr) // num_k + 1
    tekst = [' '] * len(szyfr)
    szyfr_i = 0
    for ik in range(num_k):
        for iw in range(num_w):
            idx = iw*num_k + ik
            if idx < len(tekst):
                tekst[idx] = szyfr[szyfr_i]
                szyfr_i += 1
    return ''.join(tekst)
print(deszyfruj_kol('ttafa1edsrn2kozoiszywa', 4))


# wydawanie reszty metodą zachłanną
nominaly = [10, 5, 2, 1]

'''
79 zł
79 // 10  = 7 monet po 10 zł

79 - 7*10 = 9 zł
79 // 5 = 1 moneta po 5 zł

9 - 1*5 = 4 zł
79 // 2 = 2 monety po 2 zł

4 - 2*2 = 0zł

'''
def reszta(kwota):
    nominaly = [10, 5, 2, 1]
    #while kwota != 0:
    for els in nominaly:            
        ilosc_monet = kwota//els
        if ilosc_monet > 0:
            print(f'Wydajemy {ilosc_monet} po {els}')
        moneta = els            
        kwota = kwota - (ilosc_monet * moneta)
reszta(79)

# wyszukiwanie wzorca w tekscie
wzorzec = '123'
tekst = 'bjjb123kbjkvb123klbjklb123'
for idx in range(len(tekst)):
    if tekst[idx:].startswith(wzorzec):
        print(idx)


'''
i = 0
bjjb123kbjkvb123klbjklb123
    b != 1 break

i = 1 
jjb123kbjkvb123klbjklb123
    j != 1 break

i = 4
123kbjkvb123klbjklb123
    1 == 1 ok
    2 == 2 ok
    3 == 3 ok

'''


def wzorzec1(wzorzec, tekst):
    jest_wzorzec = False
    for i in range(len(tekst)):        
        a = True
        
        for k in range(len(wzorzec)): 
            if wzorzec[k] != tekst[i+k]:
                a = False
                break # wzorzec nie pasuje
        if a: # wzorzec znaleziony
            print(i)
            jest_wzorzec = True
    if not jest_wzorzec:
        print("nie ma wzorca")


wzorzec1(wzorzec,"999")


                
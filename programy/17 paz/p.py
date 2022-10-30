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
        else:
            b = ord(ch)+k
            
        a_ch.append(chr(b))
    return "".join(a_ch)
    
print(szyfruje("program",2))
            
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
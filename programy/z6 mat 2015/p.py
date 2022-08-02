'''
Matura czerwiec 2015, zadanie 6. Kody kreskowe
'''
with open("kody.txt") as f:
    kody = f.readlines()

kody = kody.strip()

def zad6_1():
    for k in range(0,len(kody)-1,2):
            


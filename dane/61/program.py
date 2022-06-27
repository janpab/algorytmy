
from tkinter.tix import Tree

from attr import has


def is_artmetyczny(number):
    is_artmetyczny = True
    roznice = []
    for i in range(0, len(number)-1):
        roznice.append(int(number[i])-int(number[i+1]))
    for i in range(len(roznice)):
        if roznice[0]==roznice[i]:
            is_artmetyczny = True
        else:
            is_artmetyczny=False
            break
    return is_artmetyczny
def has_cubed_number(ciag):
    a = False
    for i in range(len(ciag)):
        for j in range(101):
            if j*j*j ==int(ciag[i]):
                a = True
    return a 
def find_supreme_with_cubed(ciag):
    najwieksza = -99999
    for i in range(len(ciag)):
        for j in range(101):
            if j*j*j ==int(ciag[i]):
                if j>najwieksza:
                    najwieksza = int(ciag[i])
    return najwieksza
def find_wrong_numer(ciag):
    dobra_roznica = -999999
    roznice = []
    for i in range(0, len(ciag)-1):
        roznice.append(int(ciag[i])-int(ciag[i+1]))
    for j in range(len(roznice)-1):
        if roznice[j] == roznice[j+1]:
            dobra_roznica = roznice[j]
            break
    for k in range(0, len(ciag)-1):
        if int(ciag[k]) + (dobra_roznica)*-1 != int(ciag[k+1]):
            return ciag[k+1]




def zadanie1():
    liczby = []
    ilosc_artmetycznych = 0
    najwieksza_roznica = -9999999
    with open("ciagi.txt") as f: 
        liczby = f.readlines()
    for i in range(1,200,2):
        ciag = liczby[i].split() #TABLICA
        for i in range(len(ciag)):#ZMIENIA LICZBY NA INTY
            ciag[i] = int(ciag[i])
        if is_artmetyczny(ciag):
            ilosc_artmetycznych +=1
            if ciag[0]>najwieksza_roznica:
                najwieksza_roznica=int((ciag[0])-int(ciag[1])) *-1 
    print("Ilość ciągów artmetycznych: ",ilosc_artmetycznych,"najwieksza roznica: ", najwieksza_roznica)
def zadanie2():
    liczby = []
    with open("ciagi.txt") as f: 
        liczby = f.readlines()
    
    for i in range(1,200,2):
        ciag = liczby[i].split()
        if has_cubed_number(ciag):
            print(find_supreme_with_cubed(ciag))

def zadanie3():
    liczby = []
    with open("bledne.txt") as f: 
        liczby = f.readlines()

    for i in range(1,40,2):
        ciag = liczby[i].split()
        print(find_wrong_numer(ciag))
        


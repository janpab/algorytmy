


def zadanie1():
    obrazki = []
    rewers = 0
    najwieksza_c = -999999

    with open("dane_obrazki.txt") as f:
        obrazki = f.readlines()
    
    obrazki2 = []
    for i in range(len(obrazki)):
        obrazki2.append(obrazki[i].strip())
    czarny=0
    bialy=0
    for j in range(len(obrazki2)):
        ciag = obrazki2[j]#wybieram ciag z obrazka
        ciag = ciag[:-1]
        if len(ciag)==19:#jeżeli ciag ma dlugosc 20 to oznacza ze jest to koniec obrazka (bity parzystosci)
            if czarny>bialy:
                rewers+=1
            if czarny>najwieksza_c:
                najwieksza_c=czarny
            czarny = 0
            bialy = 0
            continue
        if ciag =="":
            continue
            
        for l in range(len(ciag)):
            if ciag[l]=="1":
                czarny +=1
            if ciag[l]=="0":
                bialy+=1
    print(rewers, najwieksza_c)
def zadanie2():
    rekur = 0            
    obrazki = []
    with open("dane_obrazki.txt") as f:
        obrazki = f.readlines()
    obrazki1=[]
    for i in range(len(obrazki)):
        obrazki1.append(obrazki[i].strip())
    is_rek = True
    for j in range(len(obrazki1)):
        ciag = obrazki1[j]
        ciag = ciag[:-1]
        if len(ciag)==19:
            if is_rek:
                rekur+=1
            is_rek = True
            continue
        if ciag == "":
            continue
        if is_rek and ciag[:10]==ciag[10:]:
            is_rek = True
        else:
            is_rek = False
        print(ciag[:10],ciag[10:])
        print(ciag,len(ciag),is_rek)
    print(rekur)
def zadanie3():
    obrazki = []
    with open("dane_obrazki.txt") as f:
        obrazki = f.readlines()
    obrazki1=[]
    
    for i in range(len(obrazki)):
        obrazki1.append(obrazki[i].strip())
    print(obrazki1)
    poprawne = 0
    poprawny = True
    obrazek = []
    for j in range(len(obrazki1)):
        ciag = obrazki1[j]
        ilosc_czarnych = 0
        if ciag != "":
            obrazek.append(ciag)
            print(ciag, obrazek)
        if ciag == "":
            for k in range(len(obrazek)):#analizuje obrazek w oparciu o boczne bity parzystosci
                for l in range(len(obrazek[k:-1])-1):#analizuje linie bez ostatniej linii bitow parzystosci
                    if obrazek[k][l] == "1":#
                        ilosc_czarnych +=1
                if ilosc_czarnych%2==0 and obrazek[-1]=="0" and poprawny:
                    poprawny= True
                else:
                    poprawny = False
            for m in range(len(obrazek)):



        






        # if len(ciag1)==19:
        #     if poprawny:
        #         poprawne+=1
        #     poprawny = True
        #     continue
        # for k in range(len(ciag1)):
        #     if ciag1[k]=="1":
        #         ilosc_czarnych+=1
        # if ilosc_czarnych%2 == 0 and bit_parzystosci=="0" and poprawny:
        #     poprawny = True
        # else:
        #     poprawny = False
        
            

zadanie3()
            

            

    
        

            
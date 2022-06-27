t = input()

for i in range(int(t)):
    pesel = input()
    ww = 0
    ww += int(pesel[0])*1 
    ww += int(pesel[1])*3
    ww += int(pesel[2])*7
    ww += int(pesel[3])*9
    ww += int(pesel[4])*1
    ww += int(pesel[5])*3
    ww += int(pesel[6])*7
    ww += int(pesel[7])*9 
    ww += int(pesel[8])*1
    ww += int(pesel[9])*3
    ww += int(pesel[10])*1


    if (str(ww)[-1] == "0"):
        print("D")
    else:
        print("N")
    
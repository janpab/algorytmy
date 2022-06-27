t = input()


def zadanie(pierwszy, drugi, dlugosc):
    #funkcja ma drukowac wynik dla podanych lancuchow
    wynik = ""
    for i in range(dlugosc):
        wynik += pierwszy[i]
        wynik += drugi[i]

    print(wynik)


for i in range(int(t)):
    lancuch = input()

    lancuch_1 = str(lancuch.split(" ")[0])

    lancuch_2 = str(lancuch.split(" ")[1])

    if len(lancuch_2) >= len(lancuch_1):
        zadanie(lancuch_1, lancuch_2, len(lancuch_1))
    else:
        zadanie(lancuch_1, lancuch_2, len(lancuch_2))

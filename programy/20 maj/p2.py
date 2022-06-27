'''
Napisz funkcję, która sprawdza czy dany napis jest palindromem
(palindrom to napis, który czytany od lewej do prawej strony jest taki sam jak czytany od prawej do lewej).


abcba

'''
s = 'abcba'
list1 = list(s)
list2 = list(reversed(list1))
#list1 = [1,2,3,4]
#for i in reversed(list1):
#    print(i)
print(list1 == list2)


'''
Napisz funkcję, która sprawdza czy dane dwa napisy są anagramami
(anagram, to słowo powstałe przez przestawienie liter wyrazu wykorzystujące wszystkie litery,
np. kebab - 'babek', keson - nosek, arak - kara, bark - krab)

'''
s1 = 'kebab'
s2 = 'babek'
print(sorted(s1) == sorted(s2))

'''
Napisz funkcję, która dla danej listy liczb całkowitych zwraca listę liczb z przedziału od 5 do 10

'''
l = [34, 2, 5, 9, 34, 7, 2234, 9, 6, 3, 4]

a = [i for i in l if i>=5 and i<=10]
print(a)

'''
Napisz funkcję, która dla listy list zwraca listę list zawierającą tylko te podlisty, w których na ostatniej
pozycji znajduje się liczba parzysta
np. [[1,2,3], [4,5,6], [4,2,4], [6,3], [23,45,67]] -> [[4,5,6], [4,2,4]]

'''
l = [[1,2,3], [4,5,6], [4,2,4], [6,3], [23,45,67]]

print([i for i in l if i[-1]%2 ==0])

'''
Dana jest lista, w której znajdują się pary (liczba, napis), np.:
[(68, 'dnmjhmj'), (45, 'uwdgttwklpoerstw'), (3, 'asq'), (21, 'klllllllrtmmmwer'), (9, 'gtttwrtyx')]
Zwróć listę wszystkich napisów o długości takiej długości jak liczba w danej parze.

'''
l = [(68, 'dnmjhmj'), (45, 'uwdgttwklpoerstw'), (3, 'asq'), (21, 'klllllllrtmmmwer'), (9, 'gtttwrtyx')]

print([i[1] for i in l if len(i[1])==i[0]])


'''
Napisz funkcję, która z podanego stringu usuwa wszystkie duplikaty liter i zwraca nowy, tak zmieniony string.

'''

s = 'gsgdyernsduvsduiwuiweia'
x = set()
#x.add(1)
#1 in x

y = [[l, x.add(l)] for l in s if l not in x]
print(y)
print(x)
x_str = [el[0] for el in y]
a = ''.join(x_str)
print(a)

#print(list(enumerate(s)))

for idx, el in enumerate(s):
    print(idx, el)

'''
Dany jest napis
'PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ'
wypisz listę indeksów (pozycji liczonych od 0), na których znajduje się litera 'P'

'''
s = 'PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ'

print([isx for isx, el in enumerate(s) if el=='P'])


'''
Napisz funkcję, która dla danego napisu, w którym znajdują się słowa oddzielone spacjami, zwróci napis,
w którym wszystkie pierwsze litery każdego ze słów zostaną zamienione na duże litery
np. 'raz dwa trzy' -> 'Raz Dwa Trzy'

'''
s = 'raz dwa trzy'

#s[-1] 'y'
#s[:-1]
s = s.split()
print(s)

print(' '.join([el[0].upper() + el[1:] for el in s]))



'''
Z1 . Napisz funkcję, która sprawdza czy dany napis jest palindromem
(palindrom to napis, który czytany od lewej do prawej strony jest taki sam jak czytany od prawej do lewej).


abcba

'''
print("Z1")
s = 'abcba'
list1 = list(s)
list2 = list(reversed(list1))#reversed odwraca liste
#list1 = [1,2,3,4]
#for i in reversed(list1):
#    print(i)
print(list1 == list2)


'''
Z2 . Napisz funkcję, która sprawdza czy dane dwa napisy są anagramami
(anagram, to słowo powstałe przez przestawienie liter wyrazu wykorzystujące wszystkie litery,
np. kebab - 'babek', keson - nosek, arak - kara, bark - krab)

'''
print("Z2")
s1 = 'kebab'
s2 = 'babek'
print(sorted(s1) == sorted(s2))# sorted sortuje litery alfabetycznie

'''
Z3 . Napisz funkcję, która dla danej listy liczb całkowitych zwraca listę liczb z przedziału od 5 do 10

'''
print("Z3")
l = [34, 2, 5, 9, 34, 7, 2234, 9, 6, 3, 4]

a = [i for i in l if i>=5 and i<=10]
print(a)

'''
Z4 . Napisz funkcję, która dla listy list zwraca listę list zawierającą tylko te podlisty, w których na ostatniej
pozycji znajduje się liczba parzysta
np. [[1,2,3], [4,5,6], [4,2,4], [6,3], [23,45,67]] -> [[4,5,6], [4,2,4]]

'''
print("Z4")
l = [[1,2,3], [4,5,6], [4,2,4], [6,3], [23,45,67]]

print([i for i in l if i[-1]%2 ==0])
'''
Z5 . Dana jest lista, w której znajdują się pary (liczba, napis), np.:
[(68, 'dnmjhmj'), (45, 'uwdgttwklpoerstw'), (3, 'asq'), (21, 'klllllllrtmmmwer'), (9, 'gtttwrtyx')]
Zwróć listę wszystkich napisów o długości takiej długości jak liczba w danej parze.

'''
print("Z5")
l = [(68, 'dnmjhmj'), (45, 'uwdgttwklpoerstw'), (3, 'asq'), (21, 'klllllllrtmmmwer'), (9, 'gtttwrtyx')]

print([i[1] for i in l if len(i[1])==i[0]])
'''
Z6 . Napisz funkcję, która z podanego stringu usuwa wszystkie duplikaty liter i zwraca nowy, tak zmieniony string.

'''
print("Z6")
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
Z7 . Dany jest napis
'PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ'
wypisz listę indeksów (pozycji liczonych od 0), na których znajduje się litera 'P'

'''
print("Z7")
s = 'PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ'

print([isx for isx, el in enumerate(s) if el=='P'])
'''
Z8 . Napisz funkcję, która dla danego napisu, w którym znajdują się słowa oddzielone spacjami, zwróci napis,
w którym wszystkie pierwsze litery każdego ze słów zostaną zamienione na duże litery
np. 'raz dwa trzy' -> 'Raz Dwa Trzy'

'''
print("Z8")
s = 'raz dwa trzy'

#s[-1] 'y'
#s[:-1]
s = s.split()
print(s)

print(' '.join([el[0].upper() + el[1:] for el in s]))

'''
Z9 . Napisz funkcję, która znajduje najdłuższe słowo w danym ciągu znaków

'''
print("Z9")
s = 'jhbdf sdjfb kjsdb fjksdbf ksjbdf ksjdbf sdjkbf sdkjbfhvhvhv'
t_s = s.split()
print(t_s)
t_len = [[len(el),el] for el in t_s ]
print(t_len)
print(max(t_len))
a = max(t_len)
print(a[0], a[1])


from itertools import *

l = [1,2,3]
a, b, c = l
def xx(a, b, c):
    print(a, b, c)

xx(*l)


lista1 = [1,2,3]
lista2 = [9,8,7]
print(list(chain(lista1, lista2)))

'''
Z10 . Napisz funkcję, która znajdzie maksymalną wartość w zagnieżdżonej liście liczb, np.:
lista = [[3,6,7], [6,78,4,3,67], [5,54,7,3,3,6], [4,2,2,4,5,7,4,6,9,9,5,4,3]]

'''
print("Z10")
lista = [[3,6,7], [6,78,4,3,67], [5,54,7,3,3,6], [4,2,2,4,5,7,4,6,9,9,5,4,3]]

#chain(lista[0], lista[1], ...)
# 'avbc' + 'ffgfg' + 'rtrtrt'


print(max(chain(*lista)))

'''
Z11 . Napisz funkcję, która dla danego napisu zwroci napis z podwojonymi wszystkimi słowami
np. 'To jest TEXT' -> 'To To jest jest TEXT TEXT'

[['To', 'To'] , ....]
' '.join()
'''
print("Z11")
def fun(a):
    lista_s = a.split()
    lista_pod = [[el, el] for el in lista_s]
    #print(lista_pod)
    
    lista = ' '.join(chain(*lista_pod))
    print(lista)
fun('To jest TEXT')


lista = [[3,6,7], [6,78,4,3,67], [5,54,7,3,3,6], [4,2,2,4,5,7,4,6,9,9,5,4,3]]
print(list(zip(*lista)))


l2 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

print([max(col) for col in zip(*l2)])


lista3 = [4,6,3,7,9,0,6,5,34]

'''
Z12 . Dana jest lista liczb całkowitych. Zwróć największą różnicę pomiędzy kolejnymi liczbami.

'''
print("Z12")
print(lista3[1:])
print(lista3[:-1])
print(list(zip(lista3[:-1], lista3[1:])))
t = list(zip(lista3[:-1], lista3[1:]))

roz = [abs(el[0]-el[1]) for el in t]

print(max(roz))

lista3 == sorted(lista3) # czy lista jest posortowana
print(all([el1 > el2 for el1, el2 in zip(lista3[1:], lista3[:-1])]))

# all() - wszytskie są prawdziwe
# any() - co najmniej jedna jest True
# abs()
#[6, 3, 7, 9, 0, 6, 5, 34]
#[4, 6, 3, 7, 9, 0, 6, 5]
'''
Z13 . Napisz funkcję, która w liście zamieni miejscami każdy element parzysty z nieparzystym.
Zakładamy, że lista ma parzystą ilośc elementów.
(tzn. 1 z 2, 3 z 4, itd)

'''
print("Z13")
lista4 = [1,2,3,4,5,6,7,8]

t = list(zip(lista4[1:],lista4[:-1]))
z = list(chain(*t))
print(z)


s = 'abcdef'

print(list(enumerate(s)))

'''
Z14 . Dana jest lista napisów:
['PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ',
'VXWTUWWWSYPUYYTQWQWYRPVTRTTA',
'FFMEJJHFJNKFHKFLMINGJJLJELKLHFLJHGJJIEKEELJFMIFKENINFKGLEENKHMHMMFIFIP',
'DGFGDBACBEGAHAHHAEFHECBFBFGBDAGFHHFAEEDEEDFFCHGEDBCCCGDBHAAHAACL',
'QRTWTPPURPUXWWRWOPOVXTVPXTWTOTUOOPROTOPXVUOWWWTOPOTWPTQOSWOVRPQTUTVVTSVUSRWSS',
'JMSQLPQPMSRNRNNRRKOJJPSRSNQNSJNROQJNKJKLLJOJKNJJLSPPLQMOMNKRRKMJJSNNLQOJJQOMPKRQRLLQSLJMMKJU',
'JFLKHEKHIDJGJMKFFDJGO',
'RRYVWYSPSYUQRWXQUXPUYVWQTUVWUPQQSWYXXVSTRPUQSSPXSYRRWUQRYXSRPTPTXSSPQPPYQUQPPTYPXUXXVXSXVRTUA',
'YVUTUTSTRUVUURYXSYTSUSYYRXWVUWUTYA',
'PSMUQPPSSPTQNTNVTMNUVSUPNRNVNOOTVRSQPSNNVUPPPVTSMRUTUVMRNRMQTQQVMSSMOSRTRT',
'GEEGHDEDGGAGBBDCFGHEDIGADHBCEDDEHFEGEAFDDEGEDBFGGAEAGIDIDFADHIGDHHGADFFAADHDIACECIAFFCEFADDAIL',
'XVTYYVVWTYTWUWTWTTVXTUTXYYTXVTWWXUVYYXWVYXUUXWWYYVUWYTYVUWUYUUWXUYVYYWTWUWTXVVYTUVWA',
'VRUWUYYXRRYYUVWYXWTVYWRWSYA',
'CBCCACDHFAAHFGEEGEEHAHCAEDDHBGDEFGHFBGEGAFGGCHEHEBCGCHGL']
Wypisz słowo będące złączeniem co dziesiątej litery (liczymy litery od początku napisu zaczynając od 1) każdego napisu
występującego na co drugiej pozycji (parzysty).

'''
print("Z14")
lista5 = ['PPWROWRSUXXPTXXUOQSRWPTXUOTVWVWSSUUSXTWTUOUROQXUTOVVSRRXXRXWURXWRTTORTSOXTTSUWSSXVZ',
'VXWTUWWWSYPUYYTQWQWYRPVTRTTA',
'FFMEJJHFJNKFHKFLMINGJJLJELKLHFLJHGJJIEKEELJFMIFKENINFKGLEENKHMHMMFIFIP',
'DGFGDBACBEGAHAHHAEFHECBFBFGBDAGFHHFAEEDEEDFFCHGEDBCCCGDBHAAHAACL',
'QRTWTPPURPUXWWRWOPOVXTVPXTWTOTUOOPROTOPXVUOWWWTOPOTWPTQOSWOVRPQTUTVVTSVUSRWSS',
'JMSQLPQPMSRNRNNRRKOJJPSRSNQNSJNROQJNKJKLLJOJKNJJLSPPLQMOMNKRRKMJJSNNLQOJJQOMPKRQRLLQSLJMMKJU',
'JFLKHEKHIDJGJMKFFDJGO',
'RRYVWYSPSYUQRWXQUXPUYVWQTUVWUPQQSWYXXVSTRPUQSSPXSYRRWUQRYXSRPTPTXSSPQPPYQUQPPTYPXUXXVXSXVRTUA',
'YVUTUTSTRUVUURYXSYTSUSYYRXWVUWUTYA',
'PSMUQPPSSPTQNTNVTMNUVSUPNRNVNOOTVRSQPSNNVUPPPVTSMRUTUVMRNRMQTQQVMSSMOSRTRT',
'GEEGHDEDGGAGBBDCFGHEDIGADHBCEDDEHFEGEAFDDEGEDBFGGAEAGIDIDFADHIGDHHGADFFAADHDIACECIAFFCEFADDAIL',
'XVTYYVVWTYTWUWTWTTVXTUTXYYTXVTWWXUVYYXWVYXUUXWWYYVUWYTYVUWUYUUWXUYVYYWTWUWTXVVYTUVWA',
'VRUWUYYXRRYYUVWYXWTVYWRWSYA',
'CBCCACDHFAAHFGEEGEEHAHCAEDDHBGDEFGHFBGEGAFGGCHEHEBCGCHGL']


f = [el [9] for idx, el in enumerate(lista5) if idx % 2 == 0]
print(f)

set()
'''
Z15
W porzednim zadaniu znajdź słowo, w którym występuje największa liczba różnych liter.

'''
print("Z15")
tt = [[len(set(el)), el] for el in lista5]
print(tt)
print(max(tt))
'''
Z16
Wyszukaj najdłuższy podciąg tych samych liter w napisie.
s = 'aabbbbbccccddeeffffff'
'''
print("Z16")
s = 'aabbbbbccccddeeffffff'
print()
print([[k, v] for k, v in groupby(s)])
#print(list(groupby(s)))
print([[len(list(v)), k] for k, v in groupby(s)])


'''
Mamy daną listę liczb całkowitych. Wyszukaj najdłuższy podciąg liczb parzystych występujących kolejno po sobie.
x= [1,2,3,4,6,2,4,5,7,8,0,3,4,2]

'''
print("Z17")
x= [1,2,3,4,6,2,4,5,7,8,0,3,4,2]

def jest_parzysta(a):
    return a % 2 == 0

a = [(k, list(v)) for k, v in groupby(x, key=jest_parzysta)]
podciag = [el[1] for el in a if el[0]]
naj = [len(podciag[0]),podciag[0]]
for el in podciag:
    if len(el)>naj[0]:
        naj = [len(el),el]

print(a)
print(podciag)
print(naj[1])
            
print(max([[len(el), el] for el in podciag]))
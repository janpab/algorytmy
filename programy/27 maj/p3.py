'''
Napisz funkcję, która znajduje najdłuższe słowo w danym ciągu znaków

'''

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
Napisz funkcję, która znajdzie maksymalną wartość w zagnieżdżonej liście liczb, np.:
lista = [[3,6,7], [6,78,4,3,67], [5,54,7,3,3,6], [4,2,2,4,5,7,4,6,9,9,5,4,3]]

'''
lista = [[3,6,7], [6,78,4,3,67], [5,54,7,3,3,6], [4,2,2,4,5,7,4,6,9,9,5,4,3]]

#chain(lista[0], lista[1], ...)
# 'avbc' + 'ffgfg' + 'rtrtrt'


print(max(chain(*lista)))


'''
Napisz funkcję, która dla danego napisu zwroci napis z podwojonymi wszystkimi słowami
np. 'To jest TEXT' -> 'To To jest jest TEXT TEXT'

[['To', 'To'] , ....]
' '.join()
'''
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
Dana jest lista liczb całkowitych. Zwróć największą różnicę pomiędzy kolejnymi liczbami.

'''
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
Napisz funkcję, która w liście zamieni miejscami każdy element parzysty z nieparzystym.
Zakładamy, że lista ma parzystą ilośc elementów.
(tzn. 1 z 2, 3 z 4, itd)

'''
lista4 = [1,2,3,4,5,6,7,8]

t = list(zip(lista4[1:],lista4[:-1]))
z = list(chain(*t))
print(z)


s = 'abcdef'

print(list(enumerate(s)))



'''
Dana jest lista napisów:
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
W porzednim zadaniu znajdź słowo, w którym występuje największa liczba różnych liter.

'''

tt = [[len(set(el)), el] for el in lista5]
print(tt)
print(max(tt))


'''
Wyszukaj najdłuższy podciąg tych samych liter w napisie.
s = 'aabbbbbccccddeeffffff'
'''
s = 'aabbbbbccccddeeffffff'
print()
#print([[k, v] for k, v in groupby(s)])
print(list(groupby(s)))
print([[len(list(v)), k] for k, v in groupby(s)])


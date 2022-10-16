# https://pl.wikipedia.org/wiki/Metoda_r%C3%B3wnego_podzia%C5%82u#/media/Plik:Bisection_method.png

# y = x*x - 2   [0, 2]
def f(x):
    return x-2 
    
# a * (10 ** b) ->  aeb
# 20000 -> 2e4
# 0.0005 -> 5e-4
def bisekcja(f, a, b, epsilon=1e-10):  # a < b
    while b-a>=epsilon:
        m = (a+b)/2
        if f(a)*f(m) < 0:#różnych znakow
            b = m
        else:
            a = m
        
    return (a+b)/2
print(bisekcja(f,0,3))


def a (x):
    x = x + 1
    y = 1 + x * 2
    return y

def b (n):
    y = 0
    if (n<40):
        y = 2 * n
    elif (n<10):
        y = n
    else:
        y = 1 
    return y
	
def c (w):
    z = b(a(w))
    if (z<10):
        z = z + w
    return  z

bla = input('Skriv: ')
k = c(bla) + b(bla)
print k

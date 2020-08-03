import random

bokstaver = "abcdefghijklmnopqrstuvwxyz"
kategori = ["byer", "land", "dyr","bilmerker","felles bekjent","kunstverk","politiker","hobby","grunnstoff","butikker","sanger","verb","fag paa","jobber","adjektiv","filmer","serier","boker","artister","kjendis","band","matrett","fugl","fisk","historisk person","frukt/gronnsak","hovedkarakter i film","skuespiller"]
kontinent = [" i asia"," i afrika"," i sor-amerika"," i nord-amerika"," i osiania"," i europa",""]
land = [" i usa", " i norge", " i england",""]
fag = [" ungdomskolen"," videregaende"," universitet"]
antb = input("Skriv antall bokstaver: ")
antk = input("Skriv antall kategorier: ")
letters = []
categories = []

def bokstav(n):
    if n not in letters:
        return n
    else:
        return bokstav(bokstaver[random.randint(0,25)])
for i in range(antb):
    n = bokstaver[random.randint(0,25)]
    letters.append(bokstav(n))

def category(x):
    if x in bla:
        x = category(kategori[random.randint(0,len(kategori)-1)])
    y = random.randint(0,1)
    bla.append(x)
    if x == "fag paa":
        x += fag[random.randint(0,len(fag)-1)]
    elif (x == "land" or x == "byer" or x == "dyr") and (y == 0):
        x += kontinent[random.randint(0,len(kontinent)-1)]
    elif (x == "land" or x == "byer" or x == "dyr" or x == "kjendis") and (y == 1):
        x += land[random.randint(0,len(land)-1)]
    if x not in categories:
        return x
    else:
        return category(kategori[random.randint(0,len(kategori)-1)])

bla = []
for i in range(antk):
    print "IKKE KOEDD MED KODEN MIN"
    x = kategori[random.randint(0,len(kategori)-1)]
    categories.append(category(x))

strb = "\nBokstavene er: "
for k in range(antb):
    strb += letters[k] + ", "
strk = "\nKategoriene er: "
for j in range(antk):
    strk += categories[j] + ", "
print strb
print strk
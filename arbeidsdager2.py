def leap(y):
	return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

def sjekk(aar):
	dag = 0
	for i in range(1900,aar):
		if leap(i) == True:
			dag += 2
		else:
			dag += 1
	verdi = dag%7
	return verdi

def erArbeidsdag(dag):
	if (dag == 5) or (dag == 6):
		return False
	else:
		return True

ukedag = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lordag", "Sondag"]
aar = input ("Skriv inn et aarstall: ")
dag = sjekk(aar)
print ukedag[dag]
if erArbeidsdag(dag):
	print "Denne dagen er arbeidsdag"
else:
	print "Denne dagen er ikke arbeidsdag"

def bla(aar, dager):
	ukedag = sjekk(aar)
	dato = []
	maned = [31,28,31,30,31,30,31,31,30,31,30,31]
	if leap(aar):
		maned[1] = 29
	for i in range(0,12):
		for x in range(0,maned[i]):
			if erArbeidsdag(ukedag):
				dato.append((x,i))
			ukedag += 1
			if ukedag >= 8:
				ukedag -= 7
	return dato
	
print bla(aar,0)

dager = []
x = 1
count = input("Hvor mange dager jobber du i uken? ")
for i in range(0, count):
	x = input("Skriv inn et dagsnummer for dagene du jobber (1-7): ")
	dager.append(ukedag[x-1])	
print dager
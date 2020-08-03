#4a
def sjekkDag(aar):
	dag = 0
	for i in range(1900,aar):
		if leap(i) == True:
			dag += 2
		else:
			dag += 1
	verdi = dag%7
	return verdi


#4b
def erArbeidsdag(dag):
	if (dag == 6) or (dag == 7):
		return False
	else:
		return True

#4c
aarstall = input ("Skriv inn et aarstall: ")
dag = sjekkDag(aarstall)
print dag
if erArbeidsdag(dag):
	print "Denne dagen er arbeidsdag"
else:
	print "Denne dagen er ikke arbeidsdag"

def Tuple(start, slutt, ukedager):
	arbeid = []
	for i in range(start, slutt):
		if (erArbeidsdag(i)):
			arbeid.append(ukedager[i-1])
	return tuple(arbeid)

def Arbeids(aarstall, ukedager):
	start = sjekkDag(aar)
	slutt = start
	liste = []
	liste.append(Tuple(start, 8, ukedager))
	for i in range(0, 52):
		liste.append(Tuple(1, 8, ukedager))
	liste.append(Tuple(1, start+1, ukedager))
	return liste

ukedag = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lordag", "Sondag"]
aar = input("Skrv inn aarstall for aa printe arbeidsdagene i aaret: ")
print Arbeids(aar, ukedag)

dager = []
x = 1
count = input("Hvor mange dager jobber du i uken? ")
for i in range(0, count):
	x = input("Skriv inn et dagsnummer for dagene du jobber: ")
	dager.append(ukedag[x-1])
	

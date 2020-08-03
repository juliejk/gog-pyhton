def leap(y):
	return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

def sjekk(aar):
	dag = 0
	for i in range(1900,aar):
		dag += 1
		if leap(i) == True:
			dag += 1
	return dag%7

ukedag = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lordag", "Sondag"]
print ukedag[sjekk(input ("Skriv inn et aarstall: "))]
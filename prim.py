import math
prim = input('Skriv et tall: ')

def sjekk(tall):
	if tall > 1:
		for i in range (2, int(math.sqrt(tall)+1)):
			if (tall%i == 0):
				return False
		return True
		
print sjekk(prim)

def modulo(tall):
	liste = []
	for i in range(2,tall):
		if (tall%i == 0):
			liste.append(i)
	return liste
	
print modulo(prim)
	
def primtall(tall):
    liste = []
    for i in range(2,tall):
        if sjekk(i):
            liste.append(i)
    return liste

print primtall(prim)
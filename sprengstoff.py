from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
		self.vekt = vekt 
		self.neste = None 

def spor(kubbe):
	maks = kubbe.vekt
	while (kubbe.neste != None):
		kubbe = kubbe.neste
		if maks < kubbe.vekt:
			maks = kubbe.vekt
	return maks

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print spor(forste)

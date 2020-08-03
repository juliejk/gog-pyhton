from time import sleep

def filtrerEtterOrdlengde(liste, antallBokstaver):
	for i in range(0, len(liste)):
		if liste[i] == antallBokstaver:
			liste[0:i] = []
			break
	for i in range(0, len(liste)):
		if liste[i] == str(int(antallBokstaver)+1):
			liste[i:len(liste)] = []
			break
	liste.pop(0)
	return liste
def finnOrd(liste, letters):
	feilOrd = []
	for i in range(0, len(liste)):
		words = liste[i]
		for k in range(0, len(words)):
			letter = words[k]
			if letter not in letters:
				liste[i] = ""
	for i in range(0, liste.count("")):
		liste.remove("")
	for words in liste:
		templetters = letters
		for i in words:
			if (i in templetters):
				templetters = templetters.replace(i, '', 1)
			else:
				feilOrd.append(words)
	feilOrd = list(set(feilOrd))
	for i in liste:
		if i not in feilOrd:
			final.append(i)
	return final
def validNumber(number):
	if number not in "1234567890":
		return False
	if (int(number)>1 and int(number)<9):
		return True
	else:
		return False
def validLetters(letters):
	for char in letters:
		if char not in "abcdefghijklmnopqrstuvwxyz":
			return False
	if (len(letters) != 12):
		return False
	return True

try:
	f = open("words.txt", 'r+')
except:
	print "Mangler ordliste :("
	exit()

string = ''
final = []
antall = raw_input("Antall bokstaver: ")
while not validNumber(antall):
	antall = raw_input("Antall bokstaver (2-8): ")

for line in f:
	string+=line
liste=string.splitlines()

liste = filtrerEtterOrdlengde(liste, antall)

letters = raw_input("Bokstaver: ").lower()
while not validLetters(letters):
	letters = raw_input("Bokstaver (12stk): ").lower()

final = finnOrd(liste, letters)
print "\n"
if len(final)==0:
	print "FANT IKKE ORD :("
elif (len(final)==1):
	print "Ordet er: "
	print final[0]
else:
	print str(len(final))+" ord funnet: "
	for bla in final:
		sleep(0.1)
		print bla
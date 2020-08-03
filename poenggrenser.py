from collections import Counter
import re

def tull(x):
	fil = open(x)
	alle = fil.read()
	liste = re.findall('"Alle"', alle)
	return len(liste)	

print tull('poenggrenser_2011.csv')

def bla(x):
	fille = open(x)
	sum = 0
	count = 0
	while 1:
		gjen = fille.readline()
		if gjen == '':
			break
		if gjen.find("NTNU") != -1:
			poeng = gjen[gjen.rfind(',')+1:len(gjen)].strip('\n')
			if poeng.find("Alle") == -1:
				sum += float(poeng)
				count += 1
		
	gjom = round(sum/count,2)
	return gjom

print bla('poenggrenser_2011.csv')
		

def kodd(x):
	fille = open(x)
	max = 0
	min = 70
	maxstudie = ''
	minstudie = ''

	for i in range(0, 1109):
		gjen = fille.readline()
		poeng = gjen[gjen.rfind(',')+1:len(gjen)].strip('\n')
		studie = gjen[gjen.find('"')+1:gjen.find('",')]
		try:
			if float(poeng) > max:
				max = float(poeng)
				maxstudie = studie
			if float(poeng) < min:
				min = float(poeng)
				minstudie = studie
		except:
			pass

	return 'Laveste krav er %s %s og hoyeste krav er %s %s' % (min,minstudie,max,maxstudie)


print kodd('poenggrenser_2011.csv')

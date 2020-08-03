ord = raw_input('Skriv et ord: ')

def rever(tull):
    rev = ''
    for i in range(len(tull)):
        rev += tull[len(tull)-i-1]
    return rev

print rever(ord)

if rever(ord) == ord:
    print ord, "er et palindrom"
 
else:
    print ord, "er ikke et palindrom"

s = raw_input('skriv et ord til: ')
s2 = raw_input('skriv enda et ord: ')

def tostreng(tull,tull2):
    bla = len(tull2)
    for i in range (len(tull)):
        if tull[i:i+bla] == tull2:
            return i
        elif tull[i:i+bla] != tull2:
            mess = -1
    return mess
   
def like(tull,tull2):
	if len(tull) == len(tull2):
		for i in range(len(tull)):
			if tull[i] != tull2[i]:
				return '0'
			else:
				mess2 = '1'
	else:
		mess2 = '0'
	return mess2

print tostreng(s,s2)
print like(s,s2)

import re
regString = raw_input('Skriv en setning: ')
regString = re.findall('([A-Za-z0-9 ]+)', regString)
print ''.join(regString).lower()
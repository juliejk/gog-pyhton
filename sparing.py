def postSum(A,r,k):
	tV = []
	for i in range(1,k+1):
		V = A*((1+(r/1200.))**(i*12))
		tV.append(round(V,2))
	return tV


A = input('Skriv inn hvor mye penger du satte inn pa konto(startsum): ')
r = input('Hvor mange prosent rente har du?: ')
k = input('Hvor mange ar skal du ha pengene i banken?: ')
print postSum(A,r,k)


def slutt(s):
	start = 1000
	while 1:
		if postSum(start,5,20)[19] < s:
			start+=1000
		else:
			break
	return start

s = input('Skriv en oonsket sluttsum etter 20aar med 5% rente: ')
print slutt(s)
import random

def pinneVekt(x):
	for i in range(len(x)):
		if sum(x[0:i+1]) > sum(x)/2:
			break
	return i+(((sum(x[i:len(x)])-sum(x[0:i]))/2.)/float(x[i]))

def pinneTest(midtpunkt,stang):
	if len(stang) == 1:
		return midtpunkt == .5
	vSum = 0
	i=0
	for i in range(int(midtpunkt)):
		vSum+=stang[i]
	vSum+=stang[i+1]*(midtpunkt-int(midtpunkt))
	return vSum == sum(stang)/2.

lengde = random.randint(1,10)
stang = []
for i in range(lengde):
	stang.append(random.randint(1,9))

midt = pinneVekt(stang)
print "Dette er stanga:",stang, "og midtpunktet er", midt
#print "yes" if pinneTest(midt, stang) else "no"
import random

def masse(x):
	for i in range(len(x)):
		if sum(x[0:i+1]) > sum(x)/2:
			break
	return i+(((sum(x[i:len(x)])-sum(x[0:i]))/2.)/float(x[i]))

print masse([1])
print masse([1,2])
print masse([1,2,3,4])

lengde = random.randint(1,10)

stang = []
for i in range(lengde):
	stang.append(random.randint(1,9))

midt = masse(stang)
print "Dette er stanga:",stang, "og midtpunktet er", midt
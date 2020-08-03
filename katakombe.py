import random

N = input('How many rooms do you want the game to contain? ')
door = []

def lagdoor(rader, kolonne):    
	for rad in range(0,rader):
		door.append(lagrad(kolonne))
	return door

def lagrad(kolonne):
	rad = ["" for n in range(0,kolonne)]
	for i in range(0, len(rad)):
		if random.randint(0,2) == 0:
			rad[i] = "B"
		elif random.randint(0,2) == 1:
			rad[i] = "0"
		else:
			rad[i] = "F"
	rad[random.randint(0,kolonne-1)] = "T"
	return rad

door = lagdoor(N,4)
tall = 1

for i in range(len(door)):
	print 'Welcome to Room',str(i+1)+'!'
	print "You can choose between door 1-4"
	while tall == 1:
		dor = input('Which door do you want to open? ')-1
		door[N-1][dor] = "M"
		if dor+1 > len(door[i]) or dor+1 < 1:
			print 'You approach door',dor+1,'when you realize it didn\'t exist in the first place. Pay attention, scrub.'
			continue
		if door [i][dor] == 'T':
			print 'The room looks safe. You decide to enter...'
		elif door [i][dor] == '0':
			print 'You approach door',dor+1,'when you realize it didn\'t exist in the first place. Pay attention, scrub.'
		elif door [i][dor] == 'B':
			print 'Behind the door you opened, you find a bottomless hole. You decide to open another door...'
		elif door [i][dor] == 'F':
			print 'IT\'S A TRAP! You slam the door shut and look for another door...'
		if (door[i][dor] == 'T'):
			raw_input('Press Enter to enter... ')
			break
		elif (door[i][dor] == 'M'):
			print "Congratz mate! You got through all the room!"
			tall = 2
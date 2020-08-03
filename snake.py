import random

snakex = [3,3,3,2,1]
snakey = [2,3,4,4,4]

def lag_tomt_brett(size):
	brett = [[1]*size for i in range(size)]
	return brett

def legg_ut_epler(size, epler):
	brett = lag_tomt_brett(size)
	for i in range(epler):
		eplex = random.randint(0, size-1)
		epley = random.randint(0, size-1)
		brett[epley][eplex] = 5
	return brett

def sjekk_eple(snakex, snakey, brett):
	hodex = snakex[0]
	hodey = snakey[0]
	if brett[hodey][hodex] == 5:
		return True
	else:
		return False
	
def tegn_orm(snakex, snakey, brett):
	lengde = len(snakex)
	for i in range(lengde):
		x = snakex[i]
		y = snakey[i]
		if i == lengde - 1:
			brett[y][x] = 1
		else:
			brett[y][x] = 0
	return brett
	
def sjekk_krasj(snakex, snakey, retning):
	tempx = snakex[0]
	tempy = snakey[0]
	if retning == 'w':
		tempx = tempx - 1
	elif retning == 'e':
		tempx = tempx - 1
	elif retning == 'n':
		tempy = tempy - 1
	elif retning == 's':
		tempy = tempy + 1
	for i in range(len(snakex)):
		if tempx == snakex[i] and tempy == snakey[i]:
			return True
	return False
	
def flytt_orm(snakex,snakey,retning):
	tempx = snakex[0]
	tempy = snakey[0]
	for i in range(len(snakex)-1,0, -1):
		snakex[i] = snakex[i-1]
		snakey[i] = snakey[i-1]
	snakex[0] = tempx
	snakey[0] = tempy
	if retning == 'n':
		snakey[0] = snakey[0] - 1
	elif retning == 's':
		snakey[0] = snakey[0] + 1
	elif retning == 'w':
		snakex[0] = snakex[0] - 1
	elif retning == 'e':
		snakex[0] = snakex[0] + 1
	return snakex, snakey
	
brett = legg_ut_epler(10, 10)
ut = tegn_orm(snakex, snakey, brett)
for i in range(len(ut)):
    print ut[i]

retning='e' 
print sjekk_krasj(snakex, snakey, retning)


snakex, snakey = flytt_orm(snakex, snakey, retning)

ut = tegn_orm(snakex, snakey, brett)
for i in range(len(ut)):
    print ut[i]
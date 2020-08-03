def distance_points(distance, kpoint,meter_value):
	return 60 + (distance - kpoint) * meter_value

def style_points(liste):
	min = min(liste)
	max = max(liste)
	sum = 0
	if (i != min and  i != max):
		sum = sum + i
	return sum

import random

def number_in_list(number, list):
	for i in range(len(list)):
		if list[i] == number:
			return True
	return False

def random_list(number):
	list = []
	while len(list) < number:
		tall = random.randint(1,number)
		if not number_in_list(tall, list):
			list.append(tall)
	return list

def new_level(list):
	rad1 = []; rad2 = []; rad3 = []; rad4 = []
	for i in range(4):
		rad1.append(list[i])
		rad2.append(list[i+4])
		rad3.append(list[i+8])
		if i+12 < 15:
			rad4.append(list[i+12])
		else :
			rad4.append(0)
	level = [rad1, rad2, rad3, rad4]
	return level
		
def move_tile(level,direction):
	x = 0
	y = 0
	for i in range(len(level)):
		for j in range(4):
			if (level[i][j] == 0):
				y = i
				x = j
	if (direction == 'l' and x>0):
		level[y][x] = level[y][x-1]
		level[y][x-1] = 0
	elif (direction == 'r' and x<3):
		level[y][x] = level[y][x+1]
		level[y][x+1] = 0
	elif (direction == 'u' and y>0):
		level[y][x] = level[y-1][x]
		level[y-1][x] = 0
	elif (direction == 'd' and y<3):
		level[y][x] = level[y+1][x]
		level[y+1][x] = 0
	else:
		print 'Ulovlig trekk'
    
	return level
		
def correct_place(level):
	liste = [[1,2,3,4],[5,6,7,8],[9,10,11,12,],[13,14,15,0,]]
	antall = 0
	for i in range(len(level)):
		for j in range(4):
			if (level[i][j] == liste[i][j]):
				antall = antall + 1
	return antall


tekst = raw_input('Hvilken retningn: ')
rader = move_tile(new_level(random_list(15)),tekst)
for i in rader:
	print i
print correct_place(rader)
forrigebrett = new_level((random_list(15))
while (correct_place(rader)) < 15:
	direction = raw_input("Skriv inn retning du vil flytte 0'en (u, d, r, l): ")
	nyttbrett = move_tile((forrigebrett), direction)
	forrigebrett = move_tile((nyttbrett), direction)
	print nyttbrett	

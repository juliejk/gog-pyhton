import random

def init_life(numRows, numCols):
	world = []
	for r in range(numRows):
		row = []
		for c in range(numCols):
			row.append(random.randint(0, 1))
		world.append(row)
	return world

def print_world(world):
	for r in range(len(world)):
		for c in range(len(world[r])):
			if world[r][c]:
				print '*'
			else:
				print ' '
		print 

def next_life(world, targetRow, targetCol):
	numLiveNeighbours = 0
	numRows = len(world)
	numCols = len(world[0])
	
	for r in range(targetRow - 1, targetRow + 2):
		for c in range(targetCol - 1, targetCol + 2):
			actualRow = r % numRows
			actualCol = c % numCols
			if (r != targetRow or c != targetCol) and world[actualRow][actualCol]:
				numLiveNeighbours += 1
				
	if world[targetRow][targetCol]:
		if numLiveNeighbours == 2 or numLiveNeighbours == 3:
			return 1
		else:
			return 0
	else:
		if numLiveNeighbours == 3:
			return 1
		else:
			return 0

def life(world):
	newWorld = []
	numRows = len(world)
	numCols = len(world[0])
	for r in range(numRows):
		newWorld.append([0]*numCols)
	for r in range(numRows):
		for c in range(numCols):
			newWorld[r][c] = next_life(world, r, c)
	return newWorld

world = init_life(5, 8)
print_world(world)
for x in range(10):
	world = life(world)
	print_world(world)
	print'-----------------'
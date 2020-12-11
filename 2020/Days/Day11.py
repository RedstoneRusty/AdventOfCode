import	copy,\
		\
		CoreLib

class SeatingSystem(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [[0 if char == '.' else 1 for char in line] for line in CoreLib.InputLineSplit(input)]

	def GetNumOccupiedAdjacent(self, seating, x, y):
		numOccupiedAdjacent = 0
		for i in range(-1, 2):
			toCheckX = x + i
			if toCheckX < 0 or toCheckX >= self.width:
				continue
			for j in range(-1, 2):
				toCheckY = y + j
				if toCheckY < 0 or toCheckY >= self.height:
					continue
				if i == 0 and j == 0:
					continue
				if seating[toCheckY][toCheckX] == 2:
					numOccupiedAdjacent += 1
		return numOccupiedAdjacent

	def GetNumOccupiedLOS(self, seating, x, y):
		numOccupiedLOS = 0
		for slopeX in range(-1, 2):
			for slopeY in range(-1, 2):
				if slopeX == 0 and slopeY == 0:
					continue
				magnitude = 0
				while True:
					magnitude += 1
					toCheckX = x + (magnitude * slopeX)
					toCheckY = y + (magnitude * slopeY)
					if toCheckX < 0 or toCheckX >= self.width or toCheckY < 0 or toCheckY >= self.height:
						break
					if seating[toCheckY][toCheckX] == 2:
						numOccupiedLOS += 1
						break
					elif seating[toCheckY][toCheckX] == 1:
						break
		return numOccupiedLOS

	def SimulateUntilStable(self, seating, maxOccupied, testAdjacentFunc):
		nextSeating = copy.deepcopy(seating)
		numChanged = 1
		while numChanged:
			numChanged = 0
			for x in range(self.width):
				for y in range(self.height):
					if seating[y][x] == 0:
						continue
					numOccupiedAdjacent = testAdjacentFunc(seating, x, y)
					if numOccupiedAdjacent == 0 and seating[y][x] == 1:
						nextSeating[y][x] = 2
						numChanged += 1
					elif numOccupiedAdjacent >= maxOccupied and seating[y][x] == 2:
						nextSeating[y][x] = 1
						numChanged += 1
			seating = copy.deepcopy(nextSeating)
		return seating

	def Run(self, args):
		part = args
		seating = copy.deepcopy(self.inputData)
		self.width = len(seating[0])
		self.height = len(seating)
		if part == 1:
			stableSeating = self.SimulateUntilStable(seating, 4, self.GetNumOccupiedAdjacent)
			return len([x for y in stableSeating for x in y if x == 2])
		elif part == 2:
			stableSeating = self.SimulateUntilStable(seating, 5, self.GetNumOccupiedLOS)
			return len([x for y in stableSeating for x in y if x == 2])

class Day11(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(SeatingSystem, 0, [1, 2])]
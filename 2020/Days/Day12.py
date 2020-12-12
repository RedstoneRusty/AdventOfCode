import CoreLib

class RainRisk(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [(line[:1], int(line[1:])) for line in CoreLib.InputLineSplit(input)]

	def GetShipManhattan(self):
		diffX = 0
		diffY = 0
		dirs = ['E', 'S', 'W', 'N']
		facingIdx = 0
		for instruction, value in self.inputData:
			if instruction == 'F':
				instruction = dirs[facingIdx]
			if instruction == 'N':
				diffY += value
			elif instruction == 'S':
				diffY -= value
			elif instruction == 'E':
				diffX += value
			elif instruction == 'W':
				diffX -= value
			elif instruction == 'R':
				facingIdx += int(value / 90)
				facingIdx %= len(dirs)
			elif instruction == 'L':
				facingIdx -= int(value / 90)
				facingIdx %= len(dirs)
		return abs(diffX) + abs(diffY)

	def GetWaypointManhattan(self, waypointStart):
		diffX = 0
		diffY = 0
		waypointX = waypointStart[0] #These are offsets from the ship's current pos, not absolutes.
		waypointY = waypointStart[1]
		for instruction, value in self.inputData:
			if instruction == 'F':
				diffX += (waypointX * value)
				diffY += (waypointY * value)
			elif instruction == 'N':
				waypointY += value
			elif instruction == 'S':
				waypointY -= value
			elif instruction == 'E':
				waypointX += value
			elif instruction == 'W':
				waypointX -= value
			elif instruction == 'R':
				while value > 0:
					value -= 90
					temp = waypointX
					waypointX = waypointY
					waypointY = -temp
			elif instruction == 'L':
				while value > 0:
					value -= 90
					temp = waypointX
					waypointX = -waypointY
					waypointY = temp
		return abs(diffX) + abs(diffY)

	def Run(self, args):
		part = args[0]
		if part == 1:
			return self.GetShipManhattan()
		elif part == 2:
			return self.GetWaypointManhattan(args[1])

class Day12(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(RainRisk, 0, [(1, 0), (2, (10, 1))])]
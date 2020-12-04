import CoreLib

class TobogganTrajectory(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [char for char in [line for line in CoreLib.InputLineSplit(input)]]

	def TreeAtPos(self, x, y):
		return self.inputData[y][x % self.width] == '#'

	def TreesInSlope(self, startX, startY, diffX, diffY):
		numTrees = 0
		while startY < self.height:
			if self.TreeAtPos(startX, startY):
				numTrees += 1
			startX += diffX
			startY += diffY
		return numTrees

	def Run(self, args):
		slopes = args
		numSlopes = len(slopes)
		self.width = len(self.inputData[0])
		self.height = len(self.inputData)
		treesProduct = 1
		for slope in slopes:
			treesProduct *= self.TreesInSlope(0, 0, slope[0], slope[1])
		return treesProduct

class Day3(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(TobogganTrajectory, 0, [[(3, 1)], [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])]
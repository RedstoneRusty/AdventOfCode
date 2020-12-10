import CoreLib

class AdapterArray(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [int(num) for num in CoreLib.InputLineSplit(input)]
		self.inputData.append(max(self.inputData) + 3)
		self.inputData.append(0)
		self.inputData.sort()

	def GetAllCombos(self):
		currentStreak = 0
		permutations = 1
		for i in self.differences:
			if i == 3:
				if currentStreak > 1:
					permutations *= (sum(range(currentStreak)) + 1)
				currentStreak = 0
			elif i == 1:
				currentStreak += 1
		return permutations

	def Run(self, args):
		part = args
		if part == 1:
			self.differences = [self.inputData[i + 1] - self.inputData[i] for i in range(len(self.inputData) - 1)]
			return self.differences.count(1) * self.differences.count(3)
		elif part == 2:
			return self.GetAllCombos()

class Day10(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(AdapterArray, 0, [1, 2])]
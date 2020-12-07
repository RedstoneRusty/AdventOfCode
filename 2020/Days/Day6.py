import CoreLib

class CustomCustoms(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [[set(person) for person in CoreLib.InputLineSplit(group)] for group in CoreLib.InputEmptyLineSplit(input)]

	def Run(self, args):
		part = args
		if part == 1:
			return sum([len(set.union(*group)) for group in self.inputData])
		elif part == 2:
			return sum([len(set.intersection(*group)) for group in self.inputData])

class Day6(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(CustomCustoms, 0, [1, 2])]
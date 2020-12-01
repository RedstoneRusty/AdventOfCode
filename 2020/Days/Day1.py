import CoreLib

class ReportRepair(CoreLib.BasePuzzle):
	def __init__(self, input, args):
		super().__init__(input, args)
		self.numfactors = args[0]

	def ParseInput(self, input):
		self.inputData = [int(num) for num in CoreLib.InputLineSplit(input)]

	def Run(self):
		desiredSum = 2020
		if self.numfactors == 2:
			compatiblePairs = [(x, y) for xIndex, x in enumerate(self.inputData) for yIndex, y in enumerate(self.inputData[xIndex + 1:]) if x + y == desiredSum]
			return compatiblePairs[0][0] * compatiblePairs[0][1]
		elif self.numfactors == 3:
			compatiblePairs = [(x, y, z) for xIndex, x in enumerate(self.inputData) for yIndex, y in enumerate(self.inputData[xIndex + 1:]) for zIndex, z in enumerate(self.inputData[yIndex + 1:]) if x + y + z == desiredSum]
			return compatiblePairs[0][0] * compatiblePairs[0][1] * compatiblePairs[0][2]
		else:
			raise NotImplementedError('Invalid number of factors set for {0}'.format(type(self).__name__))

class Day1(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(ReportRepair, 0, [2]), (ReportRepair, 0, [3])]
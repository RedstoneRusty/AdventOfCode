import	functools,\
		itertools,\
		more_itertools,\
		operator,\
		\
		CoreLib

class ReportRepair(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [int(num) for num in CoreLib.InputLineSplit(input)]
		self.inputData.sort() # sorting the data makes itertools.combinations work like 10x faster for whatever reason

	def CheckSum2(self, factors):
		return factors[0] + factors[1] == self.desiredSum

	def CheckSum3(self, factors):
		return self.desiredSum - factors[0] - factors[1] in self.inputData

	def Run(self, args):
		numFactors = args[0]
		self.desiredSum = args[1]
		res = more_itertools.first_true(itertools.combinations(self.inputData, 2), pred = self.CheckSum2 if numFactors == 2 else self.CheckSum3 if numFactors == 3 else self.InvalidNumFactors)
		return res[0] * res[1] * (self.desiredSum - res[0] - res[1] if numFactors == 3 else 1)

class Day1(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(ReportRepair, 0, [(2, 2020), (3, 2020)])]
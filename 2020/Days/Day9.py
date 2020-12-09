import	itertools,\
		more_itertools,\
		\
		CoreLib

class CustomCustoms(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [int(num) for num in CoreLib.InputLineSplit(input)]

	def FindSum(self, iter, expected):
		return more_itertools.first_true(itertools.combinations(iter, 2), pred = (lambda x: x[0] + x[1] == expected))

	def Run(self, args):
		part = args
		lenInput = len(self.inputData)
		if part == 1:
			for i in range(25, lenInput):
				if self.FindSum(self.inputData[i - 25: i], self.inputData[i]) == None:
					self.weakness = self.inputData[i]
					return self.inputData[i]
		elif part == 2:
			sequenceLength = 2
			while sequenceLength < lenInput:
				for i in range(lenInput - sequenceLength):
					sequence = self.inputData[i:i + sequenceLength]
					if sum(sequence) == self.weakness:
						return max(sequence) + min(sequence)
				sequenceLength += 1

class Day9(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(CustomCustoms, 0, [1, 2])]
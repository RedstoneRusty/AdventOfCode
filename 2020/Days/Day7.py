import CoreLib

class HandyHaversacks(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.lineDict = dict(line.split(' contain', 1) for line in CoreLib.InputLineSplit(input.replace(' bags', '').replace(' bag', '').replace('.', '')))
		self.bagDict = {k: [(int(vals[0]), vals[1]) for vals in [child.strip().split(' ', 1) for child in v.split(',') if 'no other' not in child]] for (k, v) in self.lineDict.items()}

	def FindTotalCouldContain(self, toCheck):
		for key, value in self.lineDict.items():
			if toCheck in value and key not in self.colorsFound:
				self.colorsFound.add(key)
				self.FindTotalCouldContain(key)

	def FindTotalBags(self, toCheck, multiplier):
		self.totalBags += multiplier
		for amount, color in self.bagDict[toCheck]:
			self.FindTotalBags(color, multiplier * amount)

	def Run(self, args):
		part = args
		if part == 1:
			self.colorsFound = set()
			self.FindTotalCouldContain('shiny gold')
			return len(self.colorsFound)
		elif part == 2:
			self.totalBags = 0
			self.FindTotalBags('shiny gold', 1)
			return self.totalBags - 1

class Day7(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(HandyHaversacks, 0, [1, 2])]
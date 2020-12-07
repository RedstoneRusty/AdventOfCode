import	functools,\
		\
		CoreLib

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

	def FindTotalBags(self, toCheck):
		totalBags = 1
		for amount, color in self.bagDict[toCheck]:
			totalBags += self.FindTotalBags(color) * amount
		return totalBags

	def Run(self, args):
		part = args
		if part == 1:
			self.colorsFound = set()
			self.FindTotalCouldContain('shiny gold')
			return len(self.colorsFound)
		elif part == 2:
			self.FindTotalBags = functools.lru_cache()(self.FindTotalBags)
			return self.FindTotalBags('shiny gold') - 1

class Day7(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(HandyHaversacks, 0, [1, 2])]
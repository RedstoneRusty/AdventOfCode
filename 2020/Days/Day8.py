import CoreLib

class HandheldHalting(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [line.split(' ', 1) for line in CoreLib.InputLineSplit(input)]

	def GetAccum(self, program):
		accumulator = 0
		numInstructions = len(program)
		instructionIdx = 0
		linesRun = set()
		while instructionIdx < numInstructions:
			if instructionIdx in linesRun:
				break
			linesRun.add(instructionIdx)
			instruction, argument = program[instructionIdx]
			if instruction == 'jmp':
				instructionIdx += int(argument)
			else:
				if instruction == 'acc':
					accumulator += int(argument)
				instructionIdx += 1
		else:
			return accumulator, numInstructions
		return accumulator, len(linesRun)

	def Run(self, args):
		part = args
		if part == 1:
			return self.GetAccum(self.inputData)[0]
		elif part == 2:
			numInstructions = len(self.inputData)
			maxRun = 0
			for i in range(numInstructions):
				if self.inputData[i][0] == 'jmp':
					self.inputData[i][0] = 'nop'
					accumulator, linesRun = self.GetAccum(self.inputData)
					self.inputData[i][0] = 'jmp'
					if linesRun == numInstructions:
						return accumulator
				elif self.inputData[i][0] == 'nop':
					self.inputData[i][0] = 'jmp'
					accumulator, linesRun = self.GetAccum(self.inputData)
					self.inputData[i][0] = 'nop'
					if linesRun == numInstructions:
						return accumulator
			print(maxRun, numInstructions)
			return None

class Day8(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(HandheldHalting, 0, [1, 2])]
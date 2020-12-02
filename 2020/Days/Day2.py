import CoreLib

class PasswordPhilosophy(CoreLib.BasePuzzle):
	def __init__(self, input, args):
		super().__init__(input, args)
		self.part = args[0]

	def ParseLine(self, line):
		policy, password = line.split(': ')
		policyRange, policyChar = policy.split(' ')
		policyMin, policyMax = policyRange.split('-')
		return int(policyMin), int(policyMax), policyChar, password

	def ParseInput(self, input):
		self.inputData = [self.ParseLine(line) for line in CoreLib.InputLineSplit(input)]

	def ValidCharPos(self, pos1, pos2, policyChar, password):
		if pos1 >= len(password) or pos2 >= len(password):
			return False
		inPos1 = password[pos1] == policyChar
		inPos2 = password[pos2] == policyChar
		return inPos1 != inPos2

	def Run(self):
		if self.part == 1:
			return len([password for policyMin, policyMax, policyChar, password in self.inputData if password.count(policyChar) in range(policyMin, policyMax + 1)])
		elif self.part == 2:
			return len([(policyMin, policyMax, policyChar, password) for policyMin, policyMax, policyChar, password in self.inputData if self.ValidCharPos(policyMin - 1, policyMax - 1, policyChar, password)])

class Day2(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(PasswordPhilosophy, 0, [1]), (PasswordPhilosophy, 0, [2])]
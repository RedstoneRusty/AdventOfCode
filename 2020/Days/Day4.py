import CoreLib

class PassportProcessing(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [passport.replace('\n', ' ') for passport in CoreLib.InputEmptyLineSplit(input)]

	def IsValidHeight(self, value):
		if 'cm' in value:
			return 150 <= int(value.replace('cm', '')) <= 193
		elif 'in' in value:
			return 59 <= int(value.replace('in', '')) <= 76
		return False

	def IsValidHair(self, value):
		return '#' == value[0] and len([char for char in value if 'a' <= char <= 'f' or '0' <= char <= '9']) == 6 == len(value) - 1

	def IsValidPID(self, value):
		validChars = [char for char in value if '0' <= char <= '9']
		return len(validChars) == 9 == len(value)

	def PassportContainsAllValidFields(self, passport):
		for key, value in [passportField.split(':') for passportField in passport.split(' ') if passportField != '']:
			if key in self.mustContain:
				self.passportDict[key] = value
		hasAllFields = '' not in self.passportDict.values()
		if self.part == 1 or not hasAllFields:
			return hasAllFields
		valid = 1920 <= int(self.passportDict['byr']) <= 2002
		valid &= 2010 <= int(self.passportDict['iyr']) <= 2020
		valid &= 2020 <= int(self.passportDict['eyr']) <= 2030
		valid &= self.IsValidHeight(self.passportDict['hgt'])
		valid &= self.IsValidHair(self.passportDict['hcl'])
		valid &= self.passportDict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		valid &= self.IsValidPID(self.passportDict['pid'])
		return valid

	def Run(self, args):
		self.part = args
		self.mustContain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
		self.passportDict = {key: '' for key in self.mustContain}
		validCount = 0
		for passport in self.inputData:
			for key in self.mustContain:
				self.passportDict[key] = ''
			if self.PassportContainsAllValidFields(passport):
				validCount += 1
		return validCount

class Day4(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(PassportProcessing, 0, [1, 2])]
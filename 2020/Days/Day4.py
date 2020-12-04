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
		if '#' in value:
			validChars = [char for char in value.replace('#', '') if 'a' <= char <= 'f' or '0' <= char <= '9']
			return len(validChars) == 6 == len(value) - 1
		return False

	def IsValidPID(self, value):
		validChars = [char for char in value if '0' <= char <= '9']
		return len(validChars) == 9 == len(value)

	def PassportContainsAllValidFields(self, passport):
		mustContain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
		passportDict = dict(field.split(':') for field in passport.split(' ') if field != '')
		hasAllFields = all(passportField in passportDict.keys() for passportField in mustContain)
		if self.part == 1 or not hasAllFields:
			return hasAllFields
		valid = 1920 <= int(passportDict['byr']) <= 2002
		valid &= 2010 <= int(passportDict['iyr']) <= 2020
		valid &= 2020 <= int(passportDict['eyr']) <= 2030
		valid &= self.IsValidHeight(passportDict['hgt'])
		valid &= self.IsValidHair(passportDict['hcl'])
		valid &= passportDict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		valid &= self.IsValidPID(passportDict['pid'])
		return valid

	def Run(self, args):
		self.part = args
		validCount = 0
		for passport in self.inputData:
			if self.PassportContainsAllValidFields(passport):
				validCount += 1
		return validCount

class Day4(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(PassportProcessing, 0, [1, 2])]
import CoreLib

class PassportProcessing(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = [passport.replace('\n', ' ') for passport in CoreLib.InputEmptyLineSplit(input)]
		self.mustContain = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
		self.passportDict = {key: '' for key in self.mustContain}
		self.passportsWithAllFields = 0
		self.passportsWithValidFields = 0

	def IsValidHeight(self, value):
		if 'cm' in value:
			return 150 <= int(value.replace('cm', '')) <= 193
		elif 'in' in value:
			return 59 <= int(value.replace('in', '')) <= 76
		return False

	def IsValidHair(self, value):
		try:
			return value[0] == '#' and len(value[1:]) == 6 and int(value[1:], 16) > -1
		except:
			return False

	def IsValidPID(self, value):
		try:
			return len(value) == 9 and int(value) > -1
		except:
			return False

	def CheckPassportFields(self, passport):
		for key, value in [passportField.split(':') for passportField in passport.split(' ') if passportField != '']:
			if key in self.mustContain:
				self.passportDict[key] = value
		hasAllFields = '' not in self.passportDict.values()
		if not hasAllFields:
			return
		self.passportsWithAllFields += 1
		if not 1920 <= int(self.passportDict['byr']) <= 2002: return
		if not 2010 <= int(self.passportDict['iyr']) <= 2020: return
		if not 2020 <= int(self.passportDict['eyr']) <= 2030: return
		if not self.IsValidHeight(self.passportDict['hgt']): return
		if not self.IsValidHair(self.passportDict['hcl']): return
		if not self.passportDict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return
		if not self.IsValidPID(self.passportDict['pid']): return
		self.passportsWithValidFields += 1

	def Run(self, args):
		part = args
		if part == 1:
			for passport in self.inputData:
				for key in self.mustContain:
					self.passportDict[key] = ''
				self.CheckPassportFields(passport)
			return self.passportsWithAllFields
		return self.passportsWithValidFields

class Day4(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(PassportProcessing, 0, [1, 2])]
import os

class BasePuzzle:
	def __init__(self, input, args):
		self.ParseInput(input)

	def ParseInput(self, input):
		raise NotImplementedError('Puzzle {0} has not implemented a ParseInput method'.format(type(self).__name__))

	def Run(self):
		raise NotImplementedError('Puzzle {0} has not implemented a Run method'.format(type(self).__name__))

class BaseDay:
	def RunTests(self):
		for root, dirs, files in os.walk(os.path.abspath(os.getcwd() + '/Data/')):
			dayStr = type(self).__name__
			releventData = [ReadWholeFile(os.path.join(root, file)) for file in files if file == '{0}.txt'.format(dayStr) or '{0}_'.format(dayStr) in file]
			print('{0}:'.format(dayStr))
			for index, puzzle in enumerate(self.puzzles):
				puzzleClass = puzzle[0]
				dataIndex = puzzle[1]
				args = puzzle[2]
				instance = puzzleClass(releventData[dataIndex], args)
				result = instance.Run()
				print('\tPart {0}: {1}'.format(index + 1, result))

# Utility Functions
def InputLineSplit(input):
	return [e for e in input.replace('\r', '').split('\n') if e != '']

def ReadWholeFile(path):
	with open(path, 'r') as file:
		return file.read()
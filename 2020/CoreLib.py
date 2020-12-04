import	os,\
		time

class BasePuzzle:
	def __init__(self):
		pass

	def ParseInput(self, input):
		raise NotImplementedError('Puzzle {0} has not implemented a ParseInput method'.format(type(self).__name__))

	def Run(self, args):
		raise NotImplementedError('Puzzle {0} has not implemented a Run method'.format(type(self).__name__))

class BaseDay:
	def RunTests(self):
		startAllTests = time.perf_counter_ns()
		endIOTime = 0
		for root, dirs, files in os.walk(os.path.abspath(os.getcwd() + '/Data/')):
			dayStr = type(self).__name__
			releventData = [ReadWholeFile(os.path.join(root, file)) for file in files if file == '{0}.txt'.format(dayStr) or '{0}_'.format(dayStr) in file]
			endIOTime = time.perf_counter_ns()
			print('{0}:'.format(dayStr))
			partNum = 1
			for puzzle in self.puzzles:
				puzzleClass = puzzle[0]
				dataIndex = puzzle[1]
				args = puzzle[2]
				startParseTime = time.perf_counter_ns()
				instance = puzzleClass()
				instance.ParseInput(releventData[dataIndex])
				endParseTime = time.perf_counter_ns()
				for permutation in args:
					startPuzzleRun = time.perf_counter_ns()
					result = instance.Run(permutation)
					print('\tPart {0}:'.format(partNum))
					print('\t\tAnswer: {0}'.format(result))
					endPuzzleRun = time.perf_counter_ns()
					print('\t\tSolve Time: {0} ms'.format((endPuzzleRun - startPuzzleRun) / 1000000))
					partNum += 1
				print('\tData Parse Time: {0} ms'.format((endParseTime - startParseTime) / 1000000))
		endAllTests = time.perf_counter_ns()
		print('\tIO Time: {0} ms'.format((endIOTime - startAllTests) / 1000000))
		print('\tTotal Elapsed: {0} ms'.format((endAllTests - startAllTests) / 1000000))

# Utility Functions
def InputLineSplit(input):
	return [e for e in input.replace('\r', '').split('\n') if e != '']

def InputEmptyLineSplit(input):
	return [e for e in input.replace('\r', '').split('\n\n') if e != '']

def RemoveEmptyElements(input):
	return [element for element in input if element != '']

def ReadWholeFile(path):
	with open(path, 'r') as file:
		return file.read()
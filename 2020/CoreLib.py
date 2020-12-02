import os, time

class BasePuzzle:
	def __init__(self, input, args):
		self.ParseInput(input)

	def ParseInput(self, input):
		raise NotImplementedError('Puzzle {0} has not implemented a ParseInput method'.format(type(self).__name__))

	def Run(self):
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
			for index, puzzle in enumerate(self.puzzles):
				puzzleClass = puzzle[0]
				dataIndex = puzzle[1]
				args = puzzle[2]
				startParseTime = time.perf_counter_ns()
				instance = puzzleClass(releventData[dataIndex], args)
				endParseTime = time.perf_counter_ns()
				startPuzzleRun = time.perf_counter_ns()
				result = instance.Run()
				print('\tPart {0}:'.format(index + 1))
				print('\t\tAnswer: {0}'.format(result))
				endPuzzleRun = time.perf_counter_ns()
				print('\t\tData Parse Time: {0} us'.format((endParseTime - startParseTime) / 1000))
				print('\t\tSolve Time: {0} us'.format((endPuzzleRun - startPuzzleRun) / 1000))
		endAllTests = time.perf_counter_ns()
		print('\tIO Time: {0} us'.format((endIOTime - startAllTests) / 1000))
		print('\tTotal Elapsed: {0} us'.format((endAllTests - startAllTests) / 1000))

# Utility Functions
def InputLineSplit(input):
	return [e for e in input.replace('\r', '').split('\n') if e != '']

def ReadWholeFile(path):
	with open(path, 'r') as file:
		return file.read()
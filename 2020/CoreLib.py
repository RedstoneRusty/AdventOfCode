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
	def RunTests(self, numLoops):
		avgMS = 0
		for root, dirs, files in os.walk(os.path.abspath(os.getcwd() + '/Data/')):
			dayStr = type(self).__name__
			startIOTime = time.perf_counter_ns()
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
					results = set()
					timingsMS = list()
					for i in range(numLoops):
						startPuzzleRun = time.perf_counter_ns()
						results.add(instance.Run(permutation))
						endPuzzleRun = time.perf_counter_ns()
						timingsMS.append((endPuzzleRun - startPuzzleRun) / 1000000)
					print('\tPart {0}:'.format(partNum))
					for r in results:
						print('\t\tAnswer: {0}'.format(r))
					avgSolve = sum(timingsMS) / numLoops
					print('\t\tSolve Time (min, avg, max): {0:.4f} ms, {1:.4f} ms, {2:.4f} ms'.format(min(timingsMS), avgSolve, max(timingsMS)))
					avgMS += avgSolve
					partNum += 1
				parseMS = (endParseTime - startParseTime) / 1000000
				print('\tData Parse Time: {0:.4f} ms'.format(parseMS))
				avgMS += parseMS
			IOMS = (endIOTime - startIOTime) / 1000000
			print('\tIO Time: {0:.4f} ms'.format(IOMS))
			avgMS += IOMS
			print('\tTotal Elapsed: {0:.4f} ms'.format(avgMS))
			return avgMS

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
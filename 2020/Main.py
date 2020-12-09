import	importlib,\
		importlib.util,\
		os,\
		sys,\
		time,\
		\
		CoreLib

def importDay(dayNum):
	modName = 'Day{0}'.format(dayNum)
	modSpec = importlib.util.spec_from_file_location(modName, '{0}/Days/{1}.py'.format(os.path.abspath(os.getcwd()), modName))
	dayMod = importlib.util.module_from_spec(modSpec)
	modSpec.loader.exec_module(dayMod)
	return getattr(dayMod, modName)()

def main(args):
	# Determine which days were requested to test.
	dayNumsToRun = args
	numLoops = 100
	if (len(dayNumsToRun) == 0):
		dayNumsToRun = [i for i in range(1, 10)]
	days = [importDay(int(day)) for day in dayNumsToRun]

	# Run the tests.
	print('Running all tests {0} times:'.format(numLoops))
	avgTimeMS = 0
	for day in days:
		avgTimeMS += day.RunTests(numLoops)
	print('Average Total Elapsed: {0:.4f} ms'.format(avgTimeMS))

if __name__ == '__main__':
	fileDir = os.path.dirname(os.path.abspath(__file__))
	cwd = os.path.abspath(os.getcwd())
	if fileDir != cwd:
		raise AssertionError('This script\'s working directory must be the directory where Main.py is. File path is currently {0} and working directory is {1}'.format(fileDir, cwd))
	main(sys.argv[1:])
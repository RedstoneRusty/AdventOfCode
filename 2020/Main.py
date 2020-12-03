import	importlib,\
		os,\
		sys,\
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
	if (len(dayNumsToRun) == 0):
		dayNumsToRun = [i for i in range(1, 4)]
	days = [importDay(int(day)) for day in dayNumsToRun]

	# Run the tests.
	for day in days:
		day.RunTests()

if __name__ == '__main__':
	fileDir = os.path.dirname(os.path.abspath(__file__))
	cwd = os.path.abspath(os.getcwd())
	if fileDir != cwd:
		raise AssertionError('This script\'s working directory must be the directory where Main.py is. File path is currently {0} and working directory is {1}'.format(fileDir, cwd))
	main(sys.argv[1:])
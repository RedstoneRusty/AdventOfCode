import sys

def part1():
	dataFile = open('data.txt', 'r')
	data = dataFile.read().split(',')
	dataFile.close()
	instruction = 0
	
	#substitutions
	data[1] = 12
	data[2] = 2
	
	while instruction < len(data):
		opcode = int(data[instruction])
		if opcode == 99:
			break
		param0 = int(data[int(data[instruction + 1])])
		param1 = int(data[int(data[instruction + 2])])
		resultPosition = int(data[instruction + 3])
		if opcode == 1:
			data[resultPosition] = param0 + param1
		elif opcode == 2:
			data[resultPosition] = param0 * param1
		else:
			raise ValueError('')
		instruction += 4
	print(data[0])

def part2():
	dataFile = open('data.txt', 'r')
	ogData = dataFile.read().split(',')
	dataFile.close()
	found = False
	for i in range(0, 100):
		if found: break
		for j in range(0, 100):
			if found: break
			data = ogData[:]
			instruction = 0
			
			#substitutions
			data[1] = i
			data[2] = j
			
			while instruction < len(data):
				opcode = int(data[instruction])
				if opcode == 99:
					break
				param0 = int(data[int(data[instruction + 1])])
				param1 = int(data[int(data[instruction + 2])])
				resultPosition = int(data[instruction + 3])
				if opcode == 1:
					data[resultPosition] = param0 + param1
				elif opcode == 2:
					data[resultPosition] = param0 * param1
				else:
					raise ValueError('')
				instruction += 4
			if int(data[0]) == 19690720:
				found = True
				print('{:02d}{:02d}'.format(i, j))
				break

def main(args):
	part1()
	part2()

if __name__ == '__main__':
	main(sys.argv[1:])
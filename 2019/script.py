import sys, os, datetime

def LoadData():
	beginTime = datetime.datetime.now()
	data = {}
	for root, dirs, files in os.walk('.\\Input'):
		for dir in dirs:
			inputFile = open('Input\\{}\\data.txt'.format(dir), 'r')
			data[dir] = inputFile.read()
			inputFile.close()
	print('Loaded data in {} ms'.format((datetime.datetime.now() - beginTime).microseconds / 1000))
	return data

def PrintDay(num, data):
	beginTime = datetime.datetime.now()
	results = globals()['Day{}'.format(num)](data['Day{}'.format(num)])
	elapsed = (datetime.datetime.now() - beginTime).microseconds / 1000
	toPrint = 'Day {}:'.format(num)
	if len(results) == 1:
		print('{} {}'.format(toPrint, results[0]))
	else:
		for i in range(len(results)):
			toPrint += '\n\t{}. {}'.format(i + 1, results[i])
		print(toPrint)
	print('Took {} ms'.format(elapsed))
	print()
	return elapsed

def FuelFromMass(mass):
	return (int(mass) // 3) - 2

def Day1(data):
	data = data.splitlines()
	part1Fuel = 0
	totalFuel = 0
	for moduleMass in data:
		moduleFuel = FuelFromMass(moduleMass)
		part1Fuel += moduleFuel
		fuelFuel = moduleFuel
		while True:
			fuelFuel = FuelFromMass(fuelFuel)
			if fuelFuel > 0:
				moduleFuel += fuelFuel
			else:
				break
		totalFuel += moduleFuel
	return part1Fuel, totalFuel

def OpCode1(index, data):
	data[data[index + 3]] = int(data[int(data[index + 1])]) + int(data[int(data[index + 2])])
	return index + 4, data

def OpCode2(index, data):
	data[data[index + 3]] = int(data[int(data[index + 1])]) * int(data[int(data[index + 2])])
	return index + 4, data

def RunProgram(data):
	instruction = 0
	functions = {x:globals()['OpCode{}'.format(x)] for x in [1, 2]}
	while True:
		opcode = int(data[instruction])
		if opcode == 99:
			return data
		try:
			instruction, data = functions[opcode](instruction, data)
		except KeyError:
			print('Bad OpCode {} at instruction {}.'.format(opcode, instruction))
			return data

def Day2(data):
	data = [int(x) for x in data.split(',')]
	partOne = data[:]
	partOne[1], partOne[2] = 12, 2
	partOne = RunProgram(partOne)
	
	for i, j in [(x, y) for x in range(100) for y in range(100)]:
		partTwo = data[:]
		partTwo[1], partTwo[2] = i, j
		partTwo = RunProgram(partTwo)
		if int(partTwo[0]) == 19690720:
			break
	return partOne[0], '{:02d}{:02d}'.format(i, j)

def GetWireIntersections(data):
	wires = []
	directions = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
	for d in range(len(data)):
		currentCoords = (0, 0)
		wires.append({})
		distanceTraveled = 0
		for i in data[d]:
			direction, magnitude = i[0], int(str(i[1:]))
			for k in range(magnitude):
				currentCoords = (currentCoords[0] + directions[direction][0], currentCoords[1] + directions[direction][1])
				distanceTraveled += 1
				wires[d][currentCoords] = distanceTraveled
	intersections = [x for x in list(set(wires[0].keys()) & set(wires[1].keys()))]
	manhattenDistance = [abs(x[0]) + abs(x[1]) for x in intersections]
	distanceOnWires = [wires[0][x] + wires[1][x] for x in intersections]
	return manhattenDistance, distanceOnWires

def Day3(data):
	data = [x.split(',') for x in data.splitlines()]
	intersections, distanceOnWires = GetWireIntersections(data)
	return min(intersections), min(distanceOnWires)

def main(args):
	data = LoadData()
	
	totalElapsed = 0
	
	for i in range(3):
		totalElapsed += PrintDay(i + 1, data)
	print('Total Elapsed ms: {}'.format(totalElapsed))

if __name__ == '__main__':
	main(sys.argv[1:])
import sys

def FuelFromMass(mass):
	return (int(mass) // 3) - 2

def main(args):
	dataFile = open('data.txt', 'r')
	data = dataFile.read().splitlines()
	dataFile.close()
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
	print(part1Fuel)
	print(totalFuel)

if __name__ == '__main__':
	main(sys.argv[1:])
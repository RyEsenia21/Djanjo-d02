from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
	
	def __init__(self):
		self.count = 10
		print('coffee machine created')

	class EmptyCup(HotBeverage):
		name = 'empty cup'
		price = 0.90
		def description(self):
			return 'An empty cup?! Gimme my money back!'

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__('This coffee machine has to be repaired.')

	def serve(self):
		Parameters = [Coffee(), Tea(), Chocolate(), Cappuccino(), self.EmptyCup()]
		if self.count:
			self.count = self.count - 1
			return random.choice(Parameters)
		else:
			raise self.BrokenMachineException()
	
	def repair(self):
		self.count = 10
		print('repaired the coffee machine')


def main():
	cofee_machine = CoffeeMachine()
	try:
		for i in range(12):
			beverage = cofee_machine.serve()
			print(beverage)
	except Exception as Ex:
		print(Ex)
		cofee_machine.repair()
	try:
		for i in range(12):
			beverage = cofee_machine.serve()
			print(beverage)
	except Exception as Ex:
		print(Ex)
		cofee_machine.repair()


if __name__ == '__main__':
	main()

class Intern:
	Name = None

	def __init__(self, Name = "My name? I’m nobody, an intern, I have no name."):
		self.Name = Name

	def __str__(self):
		return self.Name

	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def make_coffee(self):
		return self.Coffee()

def main():
	try:
		Mark = Intern('Mark')
		NoName = Intern()
		print(Mark.__str__())
		print(NoName.__str__())
		print(Mark.make_coffee())
		NoName.work()
	except Exception as Ex:
		print(Ex)

if __name__ == '__main__':
	main()
	
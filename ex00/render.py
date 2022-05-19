from settings import name, surname, age, profession
import sys
import os

def render():
	if len(sys.argv) == 2 and sys.argv[1].split('.')[-1] == 'template' and os.path.isfile(sys.argv[1]):
			f = open(sys.argv[1], 'r')
			template = f.read().format(name = name, surname = surname, age = age, profession = profession)
			f.close()
			f = open('myCV.html', 'w')
			f.write(template)
	else:
		print("Error")

if __name__ == '__main__':
	render()
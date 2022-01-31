from os import path
from utilities.category import category

def create_file(*filename):
	for name in filename:
		if not path.exists(name):
			with open(name, "w") as f:
				f.write("")

create_file("./categories.txt")

while True:
	print('''
[1] Register a new category
[2] Exit
	''')
	user_choice = int(input(">> "))

	if user_choice == 1:
		category()
	elif user_choice == 2:
		break
	
print("You left the application.")

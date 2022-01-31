from controller import ControllerCategory
from DAO import DaoCategory
from random import randint
from category import category

def generate_number(param):
	''' Generates a random number between 
		1.000 and 5.000 for Client instances and
		10.000 and 50.000 for Employee instances. '''

	if param == "client":
		return randint(1_000, 5_000)
	elif param == "employee":
		return randint(10_000, 50_000)


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

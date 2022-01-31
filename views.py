from utilities.category import category

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

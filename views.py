from controller import ControllerCategory
from DAO import DaoCategory


while True:
	user_choice = int(input("Enter 1 for register a new category, 2 for view all categories, 3 for remove a category or 0 to exit: "))

	if user_choice == 1:
		category_name = input("Enter the name of the category: ")
		ControllerCategory.register_new_category(category_name)

	elif user_choice == 2:
		categories = DaoCategory.read()
		for category in categories:
			print(category.category_name)

	elif user_choice == 3:
		category_to_remove = input("Enter the name of the category to remove: ")
		ControllerCategory.remove_category(category_to_remove)

	elif user_choice == 0:
		break

print("You left the application.")

from controller import ControllerCategory

def category():
	while True:
		user_choice = int(input("Enter 1 for register a new category, 2 for view all categories, 3 for update a category, 4 for delete a category or 0 to back to the main menu: "))

		if user_choice == 1:
			category_name = input("Enter the name of the category: ")
			ControllerCategory.register_new_category(category_name)

		elif user_choice == 2:
			ControllerCategory.read_categories()

		elif user_choice == 3:
			category_to_update = input("Enter the name of the category to update: ")
			new_category = input("Enter the new name of the category: ")
			ControllerCategory.update_category(category_to_update, new_category)

		elif user_choice == 4:
			category_to_remove = input("Enter the name of the category to remove: ")
			ControllerCategory.remove_category(category_to_remove)

		elif user_choice == 0:
			break

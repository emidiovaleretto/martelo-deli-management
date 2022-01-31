from DAO import  DaoCategory

class ControllerCategory:

	def register_new_category(category):

		''' This method will register a new category in the system 
			and will save it in the categories.txt file. '''

		exists = False

		response = DaoCategory.read()

		for cat in response:
			if cat.category_name == category:
				exists = True

		if not exists:
			DaoCategory.save(category)
			print("Category saved successfully!")
		else:
			print("Category already exists!")

	def read_categories():

		''' This method will list all the categories from 
			categories.txt file. '''

		response = DaoCategory.read()

		if len(response) <= 0:
			print("There are no categories in the system!")
		else:
			for category in response:
				print(f"Category: {category.category_name}")

	def update_category(category_to_update, new_category):
		''' This function updates an existing category based from
		    the categories.txt file '''

		response = DaoCategory.read()
		categories = list(filter(lambda x: x.category_name == category_to_update, response))

		if len(categories) <= 0:
			print("Category not found!")
		else:
			for i in range(len(response)):
				if response[i].category_name == category_to_update:
					response[i].category_name = new_category
					break
			print("Category updated successfully!")

			with open("categories.txt", "w") as f:
				for i in response:
					f.writelines(f"{i.category_name}\n")
	
	def remove_category(category_to_remove):

		''' This method will remove a category from the system 
			and will remove it from the categories.txt file. '''

		data = DaoCategory.read()
		categories = list(filter(lambda x: x.category_name == category_to_remove, data))

		if len(categories) <= 0:
			print("Category not found!")
		else:	
			for i in range(len(data)):
				if data[i].category_name == category_to_remove:
					del data[i]
					break
			print("Removed category successfully!")

			with open("categories.txt", "w") as f:
				for i in data:
					f.writelines(f"{i.category_name}\n")

from DAO import  DaoCategory, DaoSales
from models import Product, Category, Client, Employee, Sales, Stock

class ControllerCategory:

	def register_new_category(self, category):

		''' This method will register a new category in the system 
			and will save it in the categories.txt file. '''

		exists = False

		response = DaoCategory.read()

		for category_name in response:
			if category_name == category:
				exists = True

		if not exists:
			DaoCategory.save(category)
			print("Category saved successfully!")
		else:
			print("Category already exists!")

	def remove_category(self, category_to_remove):

		''' This method will remove a category from the system 
			and will remove it from the categories.txt file. '''

		data = DaoCategory.read()
		categories = filter(lambda x: x.category == category_to_remove, data)

		if len(categories) == 0:
			print("Category not found!")
		else:	
			for i in range(len(categories)):
				if categories[i] == category_to_remove:
					del categories[i]
					break
				print("Removed category successfully!")

			with open("categories.txt", "w") as f:
				for i in data:
					f.writelines(f"{i.category}\n")




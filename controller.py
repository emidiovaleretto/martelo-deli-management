from DAO import  DaoCategory
from models import Category, Product

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

		if len(response) == 0:
			print("There are no categories in the system!")
		else:
			for category in response:
				print(f"Category: {category.category_name}")

	def update_category(category_to_update, new_category):
		''' This function updates an existing category based from
		    the categories.txt file '''

		response = DaoCategory.read()
		categories = list(filter(lambda x: x.category_name == category_to_update, response))

		if len(categories) > 0:
			cat = list(filter(lambda x: x.category_name == new_category, response))
			if len(cat) == 0:
				response = list(map(lambda x: Category(new_category) if x.category_name == category_to_update else x, response))
				print("Category updated successfully!")
			else:
				print("Category already exists. Please, choose another name.")
		else:
			print("Category not found!")

		with open("categories.txt", "w") as f:
			for i in response:
				f.writelines(f"{i.category_name}\n")
	
	def remove_category(category_to_remove):

		''' This method will remove a category from the system 
			and will remove it from the categories.txt file. '''

		response = DaoCategory.read()
		categories = list(filter(lambda x: x.category_name == category_to_remove, response))

		if len(categories) <= 0:
			print("Category not found!")
		else:	
			for i in range(len(response)):
				if response[i].category_name == category_to_remove:
					del response[i]
					break
			print("Removed category successfully!")

			with open("categories.txt", "w") as f:
				for i in response:
					f.writelines(f"{i.category_name}\n")

class ControllerStock:
	
	def create_stock(product: Product, n_product_stock: int):
		'''This function creates a stock for a given 
		   product and returns the quantity.'''
		...

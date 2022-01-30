from DAO import  DaoCategory

class ControllerCategory:

	def register_new_category(self, category):

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



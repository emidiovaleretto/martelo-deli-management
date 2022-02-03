from DAO import DaoClient, DaoCategory
from models import Category, Client


class ControllerClient:

	def create_new_client(self, client):
		'''This method will create a new client instance and
		   save it to the cliets.txt file'''

		exists = False

		response = DaoClient.read()

		for clt in response:
			if int(clt.client_number) == client.client_number or clt.name == client.name:
				exists = True
		
		if not exists:
			DaoClient.save(client)
			print("Client saved successfully!")
		else:
			print(f"It seems that the client name OR the client number you want to register is already in use. \nCheck the those data and try again.")

	def read_clients(self):
		'''This method will read the clients.txt file and
		   return a list of client instances'''

		clients = DaoClient.read()
		
		if len(clients) == 0:
			print("There are no clients registered yet.")
		else:
			for client in clients:
				print(f"Name: {client.name}\n"
					  f"Email: {client.email}\n"
				      f"Client number: {client.client_number}\n")

	def update_client(self, client_number, email_to_update, new_email):
		'''This method will update the client email 
		   in the clients.txt file'''

		clients = DaoClient.read()

		clt_number = list(filter(lambda x: int(x.client_number) == client_number, clients))

		if clt_number:
			clients = list(map(lambda x: Client(x.name, new_email, x.client_number) if x.email == email_to_update else x, clients))
			print("Client email updated successfully!")
		else:
			print(f"Client number {client_number} not found.")

		with open("clients.txt", "w") as f:
			for client in clients:
				f.writelines(f"{client.name} | "
						  	 f"{client.email} | "	
						 	 f"{client.client_number}\n")
		

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

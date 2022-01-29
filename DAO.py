from models import *
from random import randint

def generate_number(param):
	''' Generates a random number between 
		1.000 and 5.000 for Client instances and
		10.000 and 50.000 for Employee instances. '''
		
	if param == "client":
		return randint(1_000, 5_000)
	else:
		return randint(10_000, 50_000)

class DaoClient:
					
	@classmethod
	def save(cls, client: Client):
		with open("clients.txt", "a") as f:
			f.writelines(f"{client.name} | "
						 f"{client.email} | "	
						 f"{client.client_number}\n")

	@classmethod
	def read(cls):
		with open("clients.txt", "r") as f:
			cls.client_data = f.readlines()
			cls.client_data = list(map(lambda x: x.replace('\n', ''), cls.client_data))
			cls.client_data = list(map(lambda x: x.split(' | '), cls.client_data))
			
			client_data = []

			for client in cls.client_data:
				client_data.append(Client(client[0], client[1], client[2]))

			return client_data	

class DaoEmployee:

	@classmethod
	def save(cls, employee: Employee):
		with open("employees.txt", "a") as f:
			f.writelines(f"{employee.name} | "
						 f"{employee.email} | "
						 f"{employee.employee_number}\n")

	@classmethod
	def read(cls):
		with open("employees.txt", "r") as f:
			cls.employees = f.readlines()
			cls.employees = list(map(lambda x: x.replace('\n', ''), cls.employees))
			cls.employees = list(map(lambda x: x.split(' | '), cls.employees))
		
			employees = []

			for employee in cls.employees:
				employees.append(Employee(employee[0], employee[1], employee[2]))

			return employees

class DaoCategory:
	
	@classmethod
	def save(cls, category: Category):
		with open("categories.txt", "a") as f:
			f.writelines(f"{category.name}\n")

	@classmethod
	def read(cls):
		with open("categories.txt", "r") as f:
			cls.categories = f.readlines()
			cls.categories = list(map(lambda x: x.replace('\n', ''), cls.categories))
			
			categories = []

			for category in cls.categories:
				categories.append(Category(category))

			return categories

class DaoSales:

	@classmethod
	def save(cls, sale: Sales):
		with open("sales.txt", "a") as f:
			f.writelines(f"{sale.sold_item.product_name} | "
						 f"{sale.sold_item.product_price} | "
						 f"{sale.sold_item.product_category} | "
						 f"{sale.seller.name} | "
						 f"{sale.buyer.name} | "
						 f"{sale.n_sold_items} | "
						 f"{sale.sale_date}\n"
						 )

	@classmethod
	def read(cls):
		with open("sales.txt", "r") as f:
			cls.sales_data = f.readlines()
			cls.sales_data = list(map(lambda x: x.replace('\n', ''), cls.sales_data))
			cls.sales_data = list(map(lambda x: x.split(' | '), cls.sales_data))

			sales = []

			for sale in cls.sales_data:
				sales.append(sale)

			return sales

class DaoStock:

	@classmethod
	def save(cls, product: Product):
		with open("stock.txt", "a") as f:
			f.writelines(f"{product.product.product_name} | "
						 f"{product.product.product_price} | "
						 f"{product.product.product_category} | "
						 f"In Stock: {product.product_stock}\n")

	@classmethod
	def read(cls):
		with open("stock.txt", "r") as f:
			cls.stock = f.readlines()
			cls.stock = list(map(lambda x: x.replace('\n', ''), cls.stock))
			cls.stock = list(map(lambda x: x.split(' | '), cls.stock))

			stock = []

			for item in cls.stock:
				stock.append(item)

			return stock

from datetime import now

class Person:
	def __init__(self, name):
		self.name = name

class Employee(Person):
	def __init__(self, name, employee_number):
		self.employee_number = employee_number
		super(Employee, self).__init__(name)

class Client(Person):
	def __init__(self, name, client_number):
		self.client_number = client_number
		super(Client, self).__init__(name)

class Category:
	def __init__(self, category_name):
		self.category_name = category_name

class Product:
	def __init__(self, product_name, product_price, product_category):
		self.product_name = product_name
		self.product_price = product_price
		self.product_category = product_category

class Stock:
	def __init__(self, product: Product, n_product_stock):
		self.product = product
		self.product_stock = n_product_stock

class Sales:
	def __init__(self, sold_item: Product, seller, buyer: Client, sale_date = now()):
		self.product = sold_item
		self.seller = seller
		self.buyer = buyer
		self.sale_date = sale_date



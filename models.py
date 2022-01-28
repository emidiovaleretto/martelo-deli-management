from datetime import datetime

class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email

class Employee(Person):
	def __init__(self, name, email, employee_number):
		super(Employee, self).__init__(name, email)
		self.employee_number = employee_number

class Client(Person):
	def __init__(self, name, email, client_number):
		super(Client, self).__init__(name, email)
		self.client_number = client_number

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
	def __init__(self, sold_item: Product, seller, buyer: Client, n_sold_items, sale_date = datetime.now().strftime("%d/%m/%Y")):
		self.sold_item = sold_item
		self.seller = seller
		self.buyer = buyer
		self.n_sold_items = n_sold_items
		self.sale_date = sale_date



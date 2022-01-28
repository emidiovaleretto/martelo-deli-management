from models import *
from random import randint

def generate_number(param):
	''' Generates a random number between 10.000 and 50.000 '''
	if param == "client":
		return randint(10_00, 50_00)
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

DaoClient.save(Client("Conor", "conor@gmail.com", generate_number("client")))
DaoClient.save(Client("John", "john@gmail.com", generate_number("client")))
DaoClient.save(Client("Mary", "mary@gmail.com", generate_number("client")))

DaoEmployee.save(Employee("Conor", "conor@gmail.com", generate_number("employee")))
DaoEmployee.save(Employee("John", "john@gmail.com", generate_number("employee")))
DaoEmployee.save(Employee("Mary", "mary@gmail.com", generate_number("employee")))
from models import *
from random import randint

def generate_number():
	''' Generates a random number between 10.000 and 50.000 '''
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

DaoClient.save(Client("Conor", "conor@gmail.com", generate_number()))
DaoClient.save(Client("Aoife", "aoife@gmail.com", generate_number()))
DaoClient.save(Client("Clare", "clare@gmail.com", generate_number()))
# Simple text file database
# Written by Owen McKenney

import random
import string

class Database():

	def __init__(self, db_name):
		self.db_name = db_name
		self.formatted_data = "["
		self.num_lines = 0

	def setup(self, header):
		if self.num_lines == 0:
			f = open(self.db_name, "a")
			f.write(header)
			f.close()

	def format_data(self, **kwargs):
		data_id = str(random.randint(0,9)) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)

		for key, value in kwargs.items():
			if type(value) == str:
				value = value.replace(" ", "_")

			self.formatted_data += key + ":" + str(value) + ", "

		self.formatted_data = self.formatted_data[0:1] + "data_id:" + data_id + ", " + self.formatted_data[1:len(self.formatted_data) - 2] + "]"

	def find_num_lines(self):
		f = open(self.db_name, "r")
		x = f.readlines()
		self.num_lines = len(x)
		print(self.num_lines)
		f.close()

	def send_data(self):
		database = open(self.db_name, "a")
		database.write("\n" + self.formatted_data)
		database.close()

	def delete_data(self, data_id):
		with open(self.db_name, 'r') as f:
			lines = f.readlines()
			f.close()
		with open(self.db_name, 'w') as f:
			for line in lines:
				if data_id not in str(line.strip("\n")):
					f.write(line)
			f.close()
			
#db = Database("data.txt")
#db.find_num_lines()
#db.setup("To Do:")
#db.format_data(todo="mmm monke poop", done=False)
#db.send_data()
#db.delete_data("3VM")


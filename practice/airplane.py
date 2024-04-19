
class flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passenger = []
	def add_passenger(self, name):
		if not self.open_seat():
			return False
		self.passenger.append(name)
		return True
	def open_seat(self):
		return self.capacity- len(self.passenger)

a = flight(3)

name = ['mike', 'jhon', 'watson', 'smith']

for i in name:
	if a.add_passenger(i):
		print(f"passenger {i} is added")
	else:
		print(f'passenger {i} is not added because capacity left 0')
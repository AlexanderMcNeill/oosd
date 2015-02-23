class Card:

	def __init__(self, house, value):
		self.house = house
		self.value = value

	def display(self):
		print(str(self.value) + " of " + self.house + "'s")
		
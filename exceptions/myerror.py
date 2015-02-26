class MyError(IndexError):
	ERROR_MESSAGE = "You threw my error"

	def __init__(self, data):
		self.data = data

	def __str__(self):
		return self.ERROR_MESSAGE
class Person:

    def __init__(self, first_name, last_name):
    	self.first_name = first_name
    	self.last_name = last_name
    	self.dead = False

    def change_name(self, first_name, last_name):
    	self.first_name = first_name
    	self.last_name = last_name
        
    def increment_age(self):
    	self.age+= 1
    	return self.age

    def kill(self):
    	self.dead = True
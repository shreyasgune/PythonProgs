class PartyAnimal:
	x=0
	name = ""

	def __init__(self,nam):
		self.name = nam 
		print self.name,"constructed"

	def party(self):
		self.x = self.x + 1
		print self.name,"party count",self.x

	# def __del__(self):
	# 	print "I am destructed",self.x

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()

s = PartyAnimal("Shreyas")
s.party()

j = PartyAnimal("Kanou")
j.party()
s.party()
class PartyAnimal:
	x = 0

	def party(self):
		self.x = self.x + 1
		print "So far",self.x

an = PartyAnimal()
print "an",an.party()

bn = PartyAnimal()
print "bn",bn.party()

print "Type", type(an)
print "Dir", dir(an)
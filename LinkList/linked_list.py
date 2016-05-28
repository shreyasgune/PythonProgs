class Node(object):

	def __init__(self, data=None, next = None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next



class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self,data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node 

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count 

	def search(self,data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		return current

	def show(self):
		current = self.head
		while current is not None:
			print current.get_data(),"->",
			current = current.get_next()

	def delete(self,data):
		current = self.head
		previous = None
		found = False

		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()

		if current is None:
			self.head = current.get_next()
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

s = LinkedList()
s.insert(1)
s.insert(2)
s.insert(3)

s.show()
print '\n'
s.delete(2)
s.insert(4)
s.show()
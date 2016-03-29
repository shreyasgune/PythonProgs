class Node(object):
	def __init__(self,data,next):
		self.data = data
		self.next = next

class SingleList(object):

	head = None
	tail = None 

	def show(self):
		print "Showing list :: "
		current_node = self.head
		while current_node is not None:
			print current_node.data,"->",
			current_node = current_node.next
		print "EndOfList"

	def append(self,data):
		node = Node(data,None)
		if self.head is None:
			self.head = self.tail = node 
		else:
			self.tail.next = node
		self.tail = node 

	def remove(self,node_value):
		current_node = self.head
		previous_node = None
		while current_node is not None:
			if current_node.data == node_value:
				if previous_node is not None:
					previous_node.next = current_node.next
				else:
					self.head = current_node.next
			previous_node = current_node
			current_node = current_node.next	




s = SingleList()
s.append(1)
s.append(2)
s.append(3)
s.show()
s.remove(1)
s.remove(2)
s.show()

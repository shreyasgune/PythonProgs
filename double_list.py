class Node(object):
	def __init__(self,data,prev,next):
		self.data = data
		self.prev = prev
		self.next = next

class DoubleList(object):

	head = None
	tail = None 

	def append(self,data):
		new_node = Node(data,None,None)

		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.prev = self.tail
			new_node.next = None
			self.tail.next = new_node
			self.tail = new_node
	def show(self):
		print "Show List Data::"
		current_node  = self.head
		while current_node is not None:
			# print current_node.prev.data if hasattr(current_node.prev,"data") else None,"->",
			print current_node.data,"->",
			# print current_node.next.data if hasattr(current_node.next,"data") else None,"->",

			current_node = current_node.next
		print "EOX"

	def remove(self,node_value):
		current_node = self.head

		while current_node is not None:
			if current_node.data == node_value:
				if current_node.prev is not None:
					curprev = current_node.prev
					curnext = current_node.next
					curprev.next = curnext
					curnext.prev = curprev
				else:
					self.head = current_node.next
					current_node.next.prev = None

			current_node = current_node.next

s = DoubleList()

s.append(10)
s.append(20)
s.append(30)
s.show()
s.append(40)
s.show()
s.remove(40)
s.show()

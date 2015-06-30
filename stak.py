#class for defining a stack
class Stack:
	def __init__(self):
		self.items = []

	#method to push an item on a stack
	def push(self,item):
		self.items.append(item)

	#method to pop 
	def pop(self):
		return self.items.pop()

	#method to check if the stack is empty
	def isEmpty(self):
		return (self.items == [])

	#method to get the top of the stack
	def topOfStack(self):
		return len(self.items)

	def __str__(self):
		return str(self.items)

if __name__ == "__main__":
	stck = Stack()
	stck.push(5)
	stck.push(10)
	stck.push(20)
	stck.push(30)

	print stck

	stck.pop

	print stck

	print stck.topOfStack()


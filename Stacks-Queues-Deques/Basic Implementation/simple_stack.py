"""
------------------------------------------------------------------------------
Stacks, Queues, and Deques - Implementation of a Stack
------------------------------------------------------------------------------
Gianluca Capraro - July, 2019
------------------------------------------------------------------------------
The purpose of this script is to serve as a reference for understanding the
properties of Stacks and to demonstrate how a simple stack can be implemented 
using Python.
------------------------------------------------------------------------------
"""

class Stack(object):
#LIFO - last in, first out

	def __init__(self):
		#initialize self with empty list
		self.items = []

	def isEmpty(self):
		#return true if empty
		return self.items == []

	def push(self,item):
		#push item onto end of stack
		self.items.append(item)

	def pop(self):
		#pop off last item and return
		return self.items.pop()

	def peek(self):
		#return last item put in
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


#test out created Stack object
myStack = Stack()
print("\nStack object created.")
print("Stack empty? (T/F): " + str(myStack.isEmpty()) + "\n")

#push items to stack
print("Pushing items to stack...\n")
myStack.push(1)
myStack.push('hello')
myStack.push(False)

#check methods are working
print("Stack empty? (T/F): " + str(myStack.isEmpty()))
print("Size of Stack: " + str(myStack.size()) + "\n")

#pop items from stack
print("Popping items from stack...\n")
myStack.pop()
myStack.pop()
myStack.pop()

#check pop is working
print("Stack empty? (T/F): " + str(myStack.isEmpty()))
print("Size of Stack: " + str(myStack.size()) + "\n")

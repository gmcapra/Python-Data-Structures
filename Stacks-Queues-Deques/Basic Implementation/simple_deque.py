"""
-------------------------------------------------------------------------------
Stacks, Queues, and Deques - Implementation of a Deque
-------------------------------------------------------------------------------
Gianluca Capraro - July, 2019
-------------------------------------------------------------------------------
The purpose of this script is to serve as a reference for understanding the
properties of Deques and to demonstrate how a deque can be implemented 
using Python.
-------------------------------------------------------------------------------
"""

class Deque(object):
#LIFO & FIFO - operates like a hybrid Stack/Queue, can remove from front or end
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self,item):
		self.items.append(item)

	def addRear(self,item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)


#create and test Deque object
myDeque = Deque()
print("\nDeque object created.")
print("Deque empty? (T/F): " + str(myDeque.isEmpty()) + "\n")

#add some items to front and rear
print("Pushing items to Deque...\n")
myDeque.addFront('hey')
myDeque.addRear('world')

#check methods are working
print("Deque empty? (T/F): " + str(myDeque.isEmpty()))
print("Size of Deque: " + str(myDeque.size()))
#remove both and check order makes sense
#remove items from deque front and rear
print("Removing items from Deque...")
print("Removed items:")
print(myDeque.removeFront() + ' ' + myDeque.removeRear() + '\n')

#check methods are working
print("Deque empty? (T/F): " + str(myDeque.isEmpty()))



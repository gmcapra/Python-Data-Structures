"""
------------------------------------------------------------------------------
Stacks, Queues, and Deques - Implementation of a Queue
------------------------------------------------------------------------------
Gianluca Capraro - July, 2019
------------------------------------------------------------------------------
The purpose of this script is to serve as a reference for understanding the
properties of Queues and to demonstrate how a queue can be implemented 
using Python.
------------------------------------------------------------------------------
"""

class Queue(object):
#FIFO - First In, First Out

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

#create and test Queue object
myQueue = Queue()
print("\nQueue object created.")
print("Queue empty? (T/F): " + str(myQueue.isEmpty()) + "\n")

#queue some items
print("Pushing items to Queue...\n")
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

#check methods are working
print("Queue empty? (T/F): " + str(myQueue.isEmpty()))
print("Size of Queue: " + str(myQueue.size()) + "\n")

#dequeue all items
print("Dequeuing items from Queue...\n")
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()

#check dequeue is working
print("Queue empty? (T/F): " + str(myQueue.isEmpty()))
print("Size of Queue: " + str(myQueue.size()) + "\n")

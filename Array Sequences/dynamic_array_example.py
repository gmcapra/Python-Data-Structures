"""
--------------------------------------------------------------------------------
Dynamic Array Exercise Project
--------------------------------------------------------------------------------
Gianluca Capraro
Created: July 2019
--------------------------------------------------------------------------------
The purpose of this project is to demonstrate how to create and implement a 
Dynamic Array class using the built-in ctypes library.
--------------------------------------------------------------------------------
"""
import ctypes

class DynamicArray(object):

	def __init__(self):
		#count of elements (default 0)
		self.n = 0
		#how much it can hold (default 1, we will use dynamic style to get larger capacities)
		self.capacity = 1
		#initialize A as array of capacity 1
		self.A = self.make_array(self.capacity)

	def __len__(self):
		#return num elements in array
		return self.n

	def __getitem__(self,k):

		if not 0 <= k < self.n:
			#check if index is within range
			return IndexError('K index out of bounds!')
		
		#if it is in range, return the array value at index k
		return self.A[k]

	def append(self,element):
		#add element to end of array
		#check if capacity is full
		if self.n == self.capacity:
			self._resize(2*self.capacity) # multiply by 2 if capacity isnt enough
		#otherwise
		self.A[self.n] = element
		self.n += 1

	def _resize(self,new_capacity):
		#private method to resize internal array to a new capacity
		B = self.make_array(new_capacity)
		for k in range(self.n):
			B[k] = self.A[k]
		self.A = B
		self.capacity = new_capacity

	def make_array(self,new_capacity):
		#return new array with new capacity
		return(new_capacity*ctypes.py_object)()


"""
--------------------------------------------------------------------------------
Test the Dynamic Array Object
--------------------------------------------------------------------------------
"""
arr = DynamicArray()
print("\nDynamic Array Object (Arr) Successfully Created.\n")
arr.append(2)
print("Append Function Verified.\n")
arr._resize(50)
print("Resize Function Verified.\n")














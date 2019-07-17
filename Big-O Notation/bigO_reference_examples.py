"""
--------------------------------------------------------------------------------
Big-O Notation - Python Analysis and Reference Project
--------------------------------------------------------------------------------
Gianluca Capraro
Created: July 2019
--------------------------------------------------------------------------------
The purpose of this script is to go through different iterations of the 
various Big-O functions and examine them using Python. This script is also
meant to be used as a reference when working with Big O related concepts.

A great overall reference link for Big O:
https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation/487278#487278
--------------------------------------------------------------------------------
"""
print("\nGoing through examples of Big-O...\n")

"""
--------------------------------------------------------------------------------
Visualizing the different Big-O Functions with Matplotlib
--------------------------------------------------------------------------------
"""
print("Showing Relative Runtime Visualization for Different Big-O Functions...")
from math import log
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Define runtime comparisons to be made
n = np.linspace(1,10,1000)
leg_labels = ['Constant','Logarithmic','Linear','Log-Linear','Quadratic','Cubic','Exponential']
bigO = [np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,n**3,2**n]

#Setup the plot
plt.figure(figsize=(14,10))
plt.ylim(0,100)

for i in range(len(bigO)):
    plt.plot(n,bigO[i],label=leg_labels[i])

#Define plot labels
plt.title('Runtime for Various Big-O Functions')
plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------
O(1) - Constant
--------------------------------------------------------------------------------
"""
print("\nO(1): Constant Example\nValue returned:")

def func_constant(values):
	"""
	Prints first item from given list
	"""
	print(values[0])

#will always only print one value - constant Big O
val_list = [1,2,3,4,5,6]
func_constant(val_list)
print('\n')


"""
--------------------------------------------------------------------------------
O(n) - Linear
--------------------------------------------------------------------------------
"""
print("\nO(n): Linear Example\nValues returned:")

def func_linear(val_list):
	"""
	Prints all values in val list
	"""
	for value in val_list:
		print(value)

func_linear(val_list)
print('\n')


"""
--------------------------------------------------------------------------------
O(n^2) - Quadratic
--------------------------------------------------------------------------------
"""
print("\nO(n^2): Quadratic Example\nValues returned:")

def func_quadratic(val_list):
	"""
	For n items in the list, go through n operations
	Hence, n^2 or quadratic
	"""
	for val_1 in val_list:
		for val_2 in val_list:
			print(val_1,val_2)

val_list = [1,2,3]
func_quadratic(val_list)
print('\n')



"""
--------------------------------------------------------------------------------
Calculating Scale of Big O
--------------------------------------------------------------------------------
- Discuss how insignificant terms will drop out of Big O notation
- We only care about most significant terms in Big O
- As input grows larger only the fastest growing terms are of interest
- Similar to taking limits towards infinity in Calculus
--------------------------------------------------------------------------------
"""
print("Examples of Big O Scale and Comparisons\n")

"""
--------------------------------------------------------------------------------
Compare Print 1 and Print 2
--------------------------------------------------------------------------------
"""
print("Big O - Linear - O(n) Example:")
def print_1(val_list):
	"""
	O(n) - Linear, do an action n times for size of list
	"""
	for value in val_list:
		print(value)

print_1(val_list)
print('\n')


print("Big O - Linear - O(2*n), or also O(n) Example:")
def print_2(val_list):
	"""
	O(2*n) - If O is going to infinity, constant can be dropped
	Therefore, this is also O(n) after dropping insignificant terms
	"""
	for value in val_list:
		print(value)

	for value in val_list:
			print(value)

print_2(val_list)
print('\n')


"""
--------------------------------------------------------------------------------
Evaluate Comp Function
--------------------------------------------------------------------------------
"""

print("O(1 + n/2 + 10), or also O(n) Example:")
def comp(val_list):
	"""
	This function consists of parts O(1), O(n/2), and O(10)
	Going to infinity however, the 1 and 10 constants would
	fall off as insignificant and this can be boiled down to
	a Linear O(n) function.
	"""

	#O(1) - Constant
	print(val_list[0])

	#O(n/2) - Linear - Same as O(n)
	mid = (len(val_list)//2)
	for value in val_list[:mid]:
		print(value)

	#O(10) - Constant
	for x in range(10):
		print('Hello There!')

val_list = [1,2,3,4,5,6,7,8,9,10]
comp(val_list)
print('\n')


"""
--------------------------------------------------------------------------------
Big O - Worst Case vs. Best Case Scenarios for Time Complexity
--------------------------------------------------------------------------------
"""

#consider following matching function
def find_match(a_list, match):
	"""
	Given list and a word to find, return true if the word
	is in the list, false if the word is not.
	"""
	for item in a_list:
		if item == match:
			return True
	return False

#define function to print to terminal
def is_match(yes):
	if yes == True:
		return "Item Found."
	else:
		return "Item Not Found."

"""
Test matching function to find 1 (it is the first item in val_list)
Best case scenario, because only need to search at index 0
this is like O(1) or constant.
"""
print("Best Case Scenario for find_match function - O(1):")
matchFound = find_match(val_list,1)
print("Searching for first item in list...")
print(is_match(matchFound))
print("\n")

"""
Test matching function to find 11 (it is not in the list)
Worst case scenario, had to search through every single
element (or n elements). This is the same as O(n).
"""
print("Worst Case Scenario for find_match function - O(n):")
matchFound = find_match(val_list,11)
print("Searching for item not in list...")
print(is_match(matchFound))
print("\n")


"""
--------------------------------------------------------------------------------
Big O - Space Complexity
--------------------------------------------------------------------------------
"""

def create_a_list(n):
	"""
	Example of O(n) in terms of Space Complexity
	Will need to take up n items in terms of memory storage.
	"""
	new_list = []
	for item in range(n):
		new_list.append('New')
	return new_list

print("Example of Space Complexity - O(n)")
print("Returning list of 'New' for input 5...")
print(create_a_list(5))
print('\n')

def printer(n):
	"""
	Example of time and space complexity being different in same
	funciton. Even though time complexity must go through 10 loops,
	the function only stores 'Hello There!' once.
	"""
	for item in range(n): # Time complexity is O(n)
		print('Hello There!') # Space complexity is O(1)

print("Example of Time and Space Complexity for a Function")
print("Printing same message 10 times...")
print(printer(10))
print('\n')

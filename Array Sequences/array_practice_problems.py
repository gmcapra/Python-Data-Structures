"""
--------------------------------------------------------------------------------
Array Practice Problems
--------------------------------------------------------------------------------
Gianluca Capraro
Created: July 2019
--------------------------------------------------------------------------------
The purpose of this script is to show solutions to various practice problems
related to arrays in Python. 

All test code is provided by the Udemy Course to check solutions to problems: 
Python for Data Structures, Algorithms, and Interviews by Jose Portilla
--------------------------------------------------------------------------------
"""

#make necessary imports here
from nose.tools import assert_equal

#Initial Print to Terminal
print('\nRunning Through Problems and Testing Solution Attemps...')

"""
--------------------------------------------------------------------------------
Check if two Strings are Anagrams
--------------------------------------------------------------------------------
Given two strings, check to see if they are anagrams.
Example: Clint Eastwood -> Old West Action
--------------------------------------------------------------------------------
"""
#test code that must be passed
class AnagramTest(object):
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL ANAGRAM TEST CASES PASSED')

#One example solution
#If both strings, when sorted and cleaned, are equal, then they are anagrams.
#Another solution is to check frequency of characters in both strings.
def anagram(s1,s2):
	s1 = s1.replace(' ','').lower()
	s2 = s2.replace(' ','').lower()
	return sorted(s1) == sorted(s2)

#Run tests
t = AnagramTest()
print("\nTesting Anagram Check Problem Solution...")
t.test(anagram)

"""
--------------------------------------------------------------------------------
Array Pair Sum Problem
--------------------------------------------------------------------------------
Given an integer array, output all the unique pairs that sum to a specific
value k.
Example: pair_sum([1,3,2,2], 4) returns 2 pairs -> (1,3) and (2,2)
--------------------------------------------------------------------------------
"""
#test code to pass
class TestPair(object):
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL PAIR SUM TEST CASES PASSED')

#solution
def pair_sum(arr,k):
	if len(arr) < 2:
		return
	#use set for tracking
	seen = set()
	output = set()
	for num in arr:
		target = k-num
		if target not in seen:
			seen.add(num)
		else:
			output.add(((min(num,target)), max(num,target)))
	
	#print the pairs identified
	#print('\n'.join(map(str,list(output))))

	#use following code for test class check
	return len(output)
       
#check a simple command
#output should be (3,10) and (4,9)
#pair_sum([4,3,9,10,11],13) 

#Run tests
t = TestPair()
print("\nTesting Array Pair Sum Problem Solution...")
t.test(pair_sum)


"""
--------------------------------------------------------------------------------
Find the Missing Element Problem
--------------------------------------------------------------------------------
Consider an array of non-negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Example: Given finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) -> 5 is missing
--------------------------------------------------------------------------------
"""
#test code to pass
class TestFinder(object):
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL MISSING ELEMENT TEST CASES PASSED')

def find(arr1,arr2):
	#sort both arrays
	arr1.sort()
	arr2.sort()
	#check each pair, if they are not equal, then we know which is missing
	for num1,num2 in zip(arr1,arr2):
		if num1 != num2:
			return num1
	return arr[-1]

#Run test
t = TestFinder()
print("\nTesting Missing Element Problem Solution...")
t.test(find)

"""
--------------------------------------------------------------------------------
Largest Continuous Sum Problem
--------------------------------------------------------------------------------
Given an array of integers (both positive and negative) find the largest 
continuous sum.

Example: Given finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) -> 5 is missing
--------------------------------------------------------------------------------
"""
#test code to pass
class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL LARGEST CONTINUOUS SUM TEST CASES PASSED')
        
def largecontsum(arr):
    if len(arr) == 0:
        return 0
    max_num = sum = arr[0]
    for n in arr[1:]:
        sum = max(sum+n, n)
        max_num = max(sum, max_num)
    return max_num
    pass

#Run tests
print("\nTesting Largest Continuous Sum Problem Solution...")
t = LargeContTest()
t.test(largecontsum)


"""
--------------------------------------------------------------------------------
Sentence Reversal Problem
--------------------------------------------------------------------------------
Given a string of words, reverse all the words. 
Remove all leading and trailing whitespace.

Example: Given "This is the best" -> "best the is This"
--------------------------------------------------------------------------------
"""
#test code to pass
class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL STRING REVERSAL TEST CASES PASSED")

#this method works, however is technically cheating due to using python's methods
def reverse_word_easy(s):
    return " ".join(reversed(s.split()))

#instead, manually split at spaces (should use this method in interview)
def reverse_the_words(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0    
    #While index less than string length
    while i < length:
        #Element is not a space
        if s[i] not in spaces:
            #Index where word starts
            word_start = i
            while i < length and s[i] not in spaces:
                #Index where word ends
                i += 1
            #Append word to the list
            words.append(s[word_start:i])
        #Increment index
        i += 1
    #Join reversed words
    return " ".join(reversed(words))

#Run tests
t = ReversalTest()
print("\nTesting Word Reversal Problem Solution...")
t.test(reverse_the_words)


"""
--------------------------------------------------------------------------------
String Compression Problem
--------------------------------------------------------------------------------
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become:
'A4B4C5D2E4'

Function should be case sensitive ('AAAaaa' -> A3a3)
--------------------------------------------------------------------------------
"""
#test code to pass
class TestCompress(object):
    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL COMPRESSION TEST CASES PASSED')

#Compresses without checking - RunLength Compression Algorithm
def compress(s):
    #Begin Run as empty string
    r = ""
    l = len(s)
    
    #Check for length 0
    if l == 0:
        return ""
    #Check for length 1
    if l == 1:
        return s + "1"
    #Intialize values
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        #Check for same letter and add count if so
        if s[i] == s[i - 1]: 
            cnt += 1
        else:
            #If not, store previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1  
        #Increment index
        i += 1
    
    #Store everything into run
    r = r + s[i - 1] + str(cnt)
    return r

#Run tests
t = TestCompress()
print("\nTesting String Compression Problem Solution...")
t.test(compress)


"""
--------------------------------------------------------------------------------
Unique Characters in a String Problem
--------------------------------------------------------------------------------
Given a string, determine if it is comprised of all unique characters.

Example: 'abcde'  -> True
		 'aabcde' -> False
--------------------------------------------------------------------------------
"""
#test code to pass
class TestUnique(object):
    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL UNIQUE CHARACTER TEST CASES PASSED')

#easy method, shouldnt be used in formal question setting
def all_unique_easy(s):
    return len(set(s)) == len(s)

#more formal method
def all_unique_characters(s):
    chars = set()
    for let in s:
        #check if in set
        if let in chars:
            return False
        else:
            #add to set
            chars.add(let)
    return True
        
#Run tests
t = TestUnique()
print("\nTesting Unique Characters Problem Solution...")
t.test(all_unique_characters)
print('\n')

# author: Melanie Burns
# date: June 14, 2022
# email: burns.me@northeasturn.edu
# StudenID: 002923383
# Base code given in assignement 3, but everything else is my own

## Note: I was not able to complete problem 2. Despite the debugging. I'm not sure where my bug is'

import pytest
import random

# Given in assignement
def quicksort(A):
	if len(A) < 2:
		return A
	i, j = threePartition(A)
	return quicksort(A[:i]) + A[i:j+1] + quicksort(A[j+1:])
	
def threePartition(A):
	n = len(A)
	pivot = A[0] #choose first element as a pivot
	print(pivot)
	print(A)
	i, j = 0, 0
	
	# My Code
	# i should be the first index of the second partition
	# j should be the last index of the second ppartitoin (which means they can be equal)
	for mark in range(1, len(A)):
		if A[mark] < pivot:
			A[i+1], A[mark] = A[mark], A[i+1]
			i+=1
			j+=1
		elif A[mark] == pivot:
			A[j+1], A[mark] = A[mark], A[j+1]
			j+=1
		
				
	A[0], A[i] = A[i], A[0]	
	return i, j
	
def waterjug(Reds, Blues):
	return waterjug_helper(list(enumerate(Reds)), list(enumerate(Blues)))
	
def waterjug_helper(R, B):
	# assume len(r) == len(b), assume that they have the same sets of distinct 
	if len(R) == 0: return []
	if len(R) == 1: return [(R[0][0], B[0][0])]
	pivot = partition(R, B)
	return waterjug_helper(R[:pivot], B[:pivot]) + \
				 [(R[pivot][0], B[pivot][0])] + \
				 waterjug_helper(R[pivot+1:], B[pivot+1:])
				 
def partition(R, B):
	# My Code
	# Partition int 2 partitions for both r and b return the index of the pivot (it will be the same pivot for both). That pivot should have the same amount of water at the end
	# use random.randrange() for a random number
	
	# pretty sure this si going to be the same as a randomized quick sort
	pivot = random.randrange(min(len(R), len(B)))
	
	i = jug_partition(R, pivot)
	jug_partition(B, pivot)

	return i
	
# This is the basically the in class code
def jug_partition(A, pivot):
	A[0], A[pivot] = A[pivot], A[0]

	i = 0
	for j in range(1, len(A)):
		if A[j] < A[0]: 
			A[i+1], A[j] = A[j], A[i+1]
			i += 1
            
	A[0], A[i] = A[i], A[0]
	return i # returning the index of the pivot
	
def median(X, Y):
	# My Code
	# return the median of all elements of arrays X and Y where len(x)==len(y) and both are sorted. 
	# should run in O(logn) time which means this needs to be binary searched 

	n = len(X) # this works because the two arrays are assuemd to be the same size

	if n != len(Y):
		raise IndexError("arrays must be same size")
		
	if n == 0:
		return -1 # there was none found
	elif n == 1:
		return (X[0] + Y[0])/2
	elif n == 2:
		return (max(X[0], Y[0]) + min(X[1], Y[1]))/2 # similar to below we want the highests min and lowest high to get the median
	
	med_i = n//2 
	x_median, y_median = X[med_i], Y[med_i]
	
	if x_median == y_median:
		return x_median # they are in agreement so we are good! 
	elif x_median < y_median:
		# This should mean the median will be somewhere between the last half of x and the first half of y
		return median(X[med_i+1:], Y[:med_i-1])
	elif x_median > y_median:
		# Similarly this would mean the opposite, that the median is in the first half of x and the last half of y, (bigger than y-med and smaller than x-med)
		return median(X[:med_i-1], Y[med_i+1:])
	
## All tests are my code ## 
@pytest.mark.parametrize("target,expected", [
	([1,2,4,1,2,4,3], [1,1,2,2,3,4,4]), # given in hw
	([1], [1]),
	([2, 1], [1, 2]),
	([3, 2, 2, 1], [1,2,2, 3]),
	([1, 3, 2], [1,2,3]),
	])
def test_quicksort(target, expected):
	assert quicksort(target) == expected
	
@pytest.mark.parametrize("r,b,expected", [
	(
		[10, 20, 30, 40, 80, 70, 60, 100, 90, 50], 
		[40, 20, 30, 10, 100, 90, 80, 60, 50, 70], 
		set([(0, 3), (1, 1), (2, 2), (3, 0), (9, 8), (6, 7), (5, 9), (4, 6),(8, 5), (7, 4)])
	), #given
	(
		[1,3,4],	
		[1,4,3],
		set([(0,0), (1,2), (2,1)])  
	)
	])
def test_waterjug(r, b, expected):
	assert set(waterjug(r,b)) == expected

@pytest.mark.parametrize("x,y,expected", [
	([1,2], [2,4], 2), 
	([1,2], [3,4], 2.5),
	([1, 2, 4, 5], [3, 4, 7, 8], 4)
	])
def test_median(x, y, expected):
	assert median(x,y) == expected
	

if __name__ == '__main__':
	pytest.main()	

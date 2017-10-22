
"""
You're in a hotel and you forgot what room number you were in
but remember that the sum of its divisors is greater than the number,
yet there is no subset of those divisors that add up to the number itself.
There are 100 rooms in the Hotel, what's your room number?
"""

import math as mt 
from itertools import *



def finds_divisors(n):
	div = []
	for i in range(1,int(float(n)/2)+1):
		if n%i == 0:
			div.append(i)
	return div

def sumSubsets(num,vet,tam):
	total = int(mt.pow(2,tam))

	for i in range(1,total):
		summ = 0
		bit = i

		for j in range(0,tam):
			if (bit & 1) ==1:
				summ += vet[j]
			bit = bit >> 1
		if summ == num:
			return True
	return False


def findRoomnr(nr):
	for i in range(1,nr+1):
		vet = finds_divisors(i)

		test = sumSubsets(i, vet, len(vet))
		
		if sum(vet)> i and test == False:
			return i
			

print findRoomnr(100)
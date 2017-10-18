
"""
You're in a hotel and you forgot what room number you were in
but remember that the sum of its divisors is greater than the number,
yet there is no subset of those divisors that add up to the number itself.
There are 100 rooms in the Hotel, what's your room number?
"""


from math import sqrt
import random
def divisors(n):
	divisors = []
	for i in range(2, n/2+1 ):
		if n%i == 0:
			divisors.append(i)
	return divisors

def subset(lst):
	for start in range(len(lst)-1):
		for end in range(start+1,len(lst)-1):
			yield lst[start:end+1]

def all_possible(lst):
	suml = []
	psums = []
	for l in range(20000):
		for i in range(1,len(lst)+1):
			for k in range(1,i+1):
				rc = random.choice(lst)
				if rc not in suml:
					suml.append(rc)
		if sum(suml) not in psums:
			psums.append(sum(suml))
	return psums
def get_room_number(rooms):
	for roomnr in range(1,rooms + 1):
		div = divisors(roomnr)
		psums = all_possible(div)
		if sum(div) <= roomnr:
			continue
		elif roomnr not in psums:
			print roomnr
		"""
		Found = False
		for s in subset(div):
			if sum(s) == div:
				Found = True
				break
		if not Found:
			return roomnr
		"""
get_room_number(100)

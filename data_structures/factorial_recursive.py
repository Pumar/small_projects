def recursive_factorial(n):
	if n == 0:
		return 1
	elif n<0 or type(n)!=int:
		print ('Non applicable')
		sys.exit()
	return n*recursive_factorial(n-1)
import sys
print (recursive_factorial(5))
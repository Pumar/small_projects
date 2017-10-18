
"""
You have 50 white balls and 50 black balls, you are to place all of them inside 2 bowls in whatever configuration
you prefer. After having done so, the balls inside each bowl will be randomly mixed. What is the optimal 
configuration of white and black balls so that you have a maximum likelihood of choosing a white ball from a
random bowl?

"""
p = 0
for x in range(1,51):
	for y in range(1,51):
		if x == 50 and y == 50:
			continue
		tp = float(0.5*(x/float((x+y))+ (50-x)/float((100-x-y))))
		if (p < tp):
			p = tp
			vals = (x,y)

print p,vals

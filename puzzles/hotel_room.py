
def subset_sum(l,n):
	for e in l:
		






d = {}

for n in range(4,101):
	d[n] = [0]
	for i in range(2,n):
		if n%i == 0:
			d[n] += [i]

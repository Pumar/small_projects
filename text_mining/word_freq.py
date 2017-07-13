import string
import matplotlib.pyplot as plt 
d = {}

def invert_dict(d):
	inverse = {}
	for key, val in d.items():
		inverse.setdefault(val, []).append(key)
	return (inverse)


with open('bartleby.txt','r') as fl:
	for line in fl.readlines():
		words = line.strip(string.whitespace).strip('-').lower().split(' ')
		for word in words:
			word = word.strip(string.punctuation)
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1
del d['']

#HistData = list(sorted(invert_dict(d)))
print invert_dict(d)
import string
import random

def do_markov_analysis(book_title):

	with open(book_title) as fl:
		for line in fl.readlines():
			ordered_word_list = line.strip(string.whitespace).split(' ')
			#ordered_word_list[0].strip(string.punctuation)

			for i in range(len(ordered_word_list)-1):
				#ordered_word_list[i+1].strip(string.punctuation)
				if (not ordered_word_list[i].isalpha() and not (string.printable in (ordered_word_list[i] and ordered_word_list[i+1]))):
					continue
				if ordered_word_list[i] not in d:
					d[ordered_word_list[i]] = [ordered_word_list[i+1]]
				else:
					d[ordered_word_list[i]] += [ordered_word_list[i+1]]
				"""
				elif ordered_word_list[i+1] not in d[ordered_word_list[i]].keys():
					d[ordered_word_list[i]][ordered_word_list[i+1]] = 1 # might be problematic

				else:
					d[ordered_word_list[i]][ordered_word_list[i+1]]+=1
				"""

#text file names of the books
bts = []
with open('book_list.txt') as bl:
	for line in bl.readlines():
		bts.append(line.strip(string.whitespace))


d = {}
for j in bts:
	bt = 'books/' + j
	do_markov_analysis(bt)



text = []

r = 'The'
for _ in range(20):
	if r not in d.keys():
		r = random.choice(d.keys())
	r = random.choice(d[r])
	text.append(r)
#print d['beg']
print 'The '+(' '.join(text))


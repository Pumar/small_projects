"""
There are 100 people sat on a circular table.
If you ask every second person to leave,
who will be the last one left?
"""



### List solution

"""
table = [i for i in range(1,101)]
print table
while len(table) > 1:
	ntable = []
	for e in range(len(table)):
		if e%2 != 0:
			ntable.append(table[e])
	
	table = ntable
	print table
#print table
"""

### Data structure solution

class Element(object):
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def skip_next(self, head):
    	element = self.head
    	if element.next.next:
    		element.next = element.next.next
    	else:
    		return -1
    def circularize(self,head):
    	n_element = self.head
    	while n_element.next:
    		n_element = n_element.next
    	n_element.next = self.head

e1 = Element(1)
ll = LinkedList(e1)
for i in range(2,101):
	ll.append(Element(i))
ll.circularize(ll.head)
a = 0
while a!=-1:
	a = ll.skip_next(ll.head)

print ll.head.value



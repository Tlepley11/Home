'''
 This program returns a list that only contains the elements 
 that are common between the lists, without duplicates. 
 '''
from random import randint
a = []
b = []
c = []
for i in range(10):
	a.append(randint(0,10))
	b.append(randint(0,10))
for i in b:
	if i in a and i not in c:
		c.append(i)
print(c)

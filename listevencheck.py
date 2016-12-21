'''
This program takes a list (a) and makes a new list that has only 
the even elements of the list in it.
This exercise is meant to help illustrate list comprehension.
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 ==0]
print(b)

#A program that prints all integers in a list less than a value input by the user
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = input("Please enter a number: ")
b = []
for i in a: 
		if i < x: print(i); b.append(i)
print(b)

#This program checks if a number is even or odd and checks if it is divisible by another number.
num = input("Please enter an number: ")
div = input("Please enter a number to divide by: ")
if num % 2 == 0  and num % 4 == 0:
	print(str(num) + "  is an even number and is divisible by 4.")
else:
	if num % 2 == 0:
		print(str(num) + " is an even number.")
	else:
		print(str(num) + " is an odd number.")
if num  % div == 0:
	print(str(num) + " is divisible by " + str(div) + ".")
else:
	print(str(num) + " is not divisible by " + str(div) + ".")
print("\nHave a nice day!")

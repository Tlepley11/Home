#Ask the user for a string and print out whether this string is a palindrome or not.
a = raw_input("Please enter a word: ").lower()
if a == a[::-1]:
	print("Palindrome.")
else:
	print("Not a palindrome.")

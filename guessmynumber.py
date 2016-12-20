def main():
#"Guess My Number" game.
#The computer will randomly generate a number for the user to guess.
	from random import randint
	guessesTaken = 0
	guess = 0
	User = raw_input("What's your name? ")
	print ("Hi " + User + "!")
	print("Let's play a guessing game. I'll choose a number and you try to guess it.")
	print ("I am thinking of a number between X and Y where Y can't be over 100.")
	range_low = abs(input("What should the value of X be? "))
	while range_low > 90:
		print("X must be greater than or equal to 0 and less than or equal to 99.")
		range_low = abs(input("What should the value of X be? "))
	range_high = abs(input("What should the value of Y be? "))
	while range_low >= range_high or range_high > 100:
		print("Y must be greater than " + str(range_low) + " and less than or equal to 100.")
		range_high = abs(input("What should the value of Y be? "))
	guesses = (range_high-range_low)/5
	numwords = ['', 'one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine',\
				'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',\
				'eighteen', 'nineteen','twenty']
	magic_number = randint(range_low,range_high)
	print("Alright, you have " + str(numwords[guesses]) + " guesse(s)!")
	try:
		while guessesTaken < guesses:
			guess = int(raw_input("Please take a guess: ".replace(',','')))
			guessesTaken = guessesTaken + 1
			if range_low > guess or guess > range_high:
				print("Number outside of %s to %s, bozo. Try again." % (range_low, range_high))
			elif guess < magic_number:
				print("Too low.")
			elif guess > magic_number:
				print("Too high.")
			elif guess == magic_number:
				break
	except:
		print("Error: Invalid integer entered.")
		exit()
	if guess == magic_number:
		print("\nYup, that's the number.")
	else:
		print("\nSorry, " + User + ", the Magic Number is " + str(magic_number) + ".")
	if guess == magic_number and guessesTaken == 1:
		print("It only took " + str(numwords[guessesTaken]) + " guess to find the number!")
	elif guess == magic_number and guessesTaken > 1:
		print("It took " + str(numwords[guessesTaken]) + " guesses to find the number!")

main()

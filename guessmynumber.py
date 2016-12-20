def main():
#"Guess My Number" game.
#The computer will randomly generate a number for the user to guess.
	from random import randint
	guessesTaken = 0
	guess = 0
	User = raw_input("What is your name? ")
	print ("Hi " + User + "!")
	print("Let's play a guessing game. I'll choose a number and you try to guess it.")
	print ("I am thinking of a number between X and Y where Y can't be over 500.")
	range_low = abs(input("What should the value of X be? "))
	if 0 > range_low > 500:
		print("X must be greater than or equal to 0 and less than 500.")
		range_low = abs(input("What should the value of X be? "))
	range_high = abs(input("What should the value of Y be? "))
	if range_low >= range_high or range_high > 500:
		print("Y must be greater than " + str(range_low) + " and less than 500.")
		range_high = abs(input("What should the value of Y be? "))
	guesses = range_high/10
	magic_number = randint(range_low,range_high)
	print("Alright, you have " + str(guesses) + " guesses!")
	try:
		while guessesTaken < guesses:
			guess = int(input("Please take a guess: "))
			guessesTaken = guessesTaken + 1
			if range_low > guess or guess > range_high:
				print("Number outside of %s to %s, bozo. Try again." % (range_low, range_high))
			elif guess < magic_number:
				print("Too low. Try again.")
			elif guess > magic_number:
				print("Too high. Try again.")
			elif guess == magic_number:
				break
	except:
		print("Error: Invalid integer entered.")
		exit()
	if guess == magic_number:
		print()
		print("You guessed correct, great job!")
		print("It took " + str(guessesTaken) + " guesses to find the magic number!")
	else:
		print()
		print("Sorry, " + User + ", the Magic Number is " + str(magic_number) + ".")

main()

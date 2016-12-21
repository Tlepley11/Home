#rock-paper-scissors game for two players
#player names function
def playernames():
	global player_1
	global player_2
	player_1 = raw_input("Player 1 name: ")
	player_2 = raw_input("Player 2 name: ")
	menu()

#game menu
def menu():
	print("Welcome to the game!\n")
	print("Player 1: " + player_1)
	print("Player 2: " + player_2)
	choice = raw_input("Please choose an option: \n"
						"1: Start a new game\n"
						"2: Choose different Player Names\n"
						"3: Quit\n")
	if choice == "1":
		RPS()
	elif choice == "2":
		playernames()
	else:
		end("Quitting...")


#game
def RPS():
	print(player_1 + " it's your turn!")
	pick_1 = raw_input("Player 1, (R)ock, (P)aper, (S)cissors?: ")
	if pick_1



playernames()
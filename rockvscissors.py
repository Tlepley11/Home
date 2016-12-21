#rock-paper-scissors game for two players

#player names function
def playername():
	player_1 = raw_input("Player 1 name: ")
	player_2 = raw_input("\nPlayer 2 name: ")
	menu()

def menu():
	choice = raw_input("Please choose an option: \n"
						"1: Start a new game\n"
						"2: Choose different Player Names\n"
						"3: Quit\n")
	if choice == 1:
		new_game()
	elif choice == 2:
		playername()
	else:
		end("Quitting...")
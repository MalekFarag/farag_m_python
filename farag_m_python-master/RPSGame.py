from random import randint 

c = ["Rock", "Paper", "Scissors"]

computer = c[randint(0,2)]

c_lives = 3
p_lives = 3

player = False

while player == False:

	player = input("Rock, Paper, Scissors?\n")
	if player == computer:
		print("It's a Tie")
		print("Lives:", p_lives, "\nOpponent's lives:", c_lives,"\n")

	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "covers", player)
			p_lives -=1
			print("Lives:", p_lives, "\nOpponent's lives:", c_lives,"\n")

	elif player  == "Paper":
		if computer == "Scissors": 
			print("You lose!", computer, "cuts", player)
			p_lives -=1
			print("Lives:", p_lives, "\nOpponent's lives:", c_lives,"\n")

	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "crushes", player)
			p_lives -=1
			print("Lives:", p_lives, "\nOpponent's lives:", c_lives,"\n")
		else:
			print("You win!")
			c_lives -=1
			print("Lives:", p_lives, "\nOpponent's lives:", c_lives,"\n")

	else: 
		print("That's not a usable weapon. Try again!")

	if c_lives == 0:
		print("You win!\nYou are triumphant! Good work comrad.\n \nNew Game.")
		p_lives = 3
		c_lives = 3

	elif p_lives == 0:
		print("You lose!\nYou're out of lives. Oof. You are dead.\n \nNew Game.")
		p_lives = 3
		c_lives = 3
	
	player = False
	computer = c[randint(0,2)]
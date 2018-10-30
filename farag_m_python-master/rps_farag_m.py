from random import randint 

c = ["Rock", "Paper", "Scissors"]

computer = c[randint(0,2)]

player = False

while player == False:

	player = input("Rock, Paper, Scissors?\n")
	if player == computer:
		print("It's a Tie")

	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "covers", player)

	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player)

	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "crushes", player)
		else:
			print("You win", player,"beats", computer)
	else: 
		print("That's not a usable weapon. Try again!")

	player = False
	computer = c[randint(0,2)]

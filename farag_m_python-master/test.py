from random import randint 

choices = ["Rock", "Paper", "Scissors"]

computer = choices[randint(0,2)]

player = False

while player == False:

	player = input("Rock, Paper, Scissors?")
	if player == computer:
		print("It's a Tie")

	elif player == "Rock":
		print("w")

		player = False
			

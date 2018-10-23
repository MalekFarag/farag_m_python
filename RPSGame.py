# type hash to make notes

from random import randint

choices = ["Rock", "Paper", "Scissors"]
	#to make chocies
player = False

computer_choice = choices[randint(0,2)]
						#"randint to choose at random



while player is False:
	print("Choose your weapon")
	player = input("Rock, Paper, or Scissors?\n")	

	print(player, "\n")

	if player == computer_choice:
		print("Tie")

	elif player == "Rock":
		if computer_choice == "Paper":
			print("FAT L (paper covers rock)")
		else: print("EZ W! Good smash!")

	elif player == "Paper":
		if computer_choice == "Scissors":
			print("FAT L (scissors cut paper")
		else: print("EZ W! Paper covers computer_choice")

	elif player == "Scissors":
		if computer_choice == "Rock":
			print("GET SMASHED FAM! FAT L.")
		else: print("W! You cut computer_choice")

		print("computer chooses:", computer_choice) 
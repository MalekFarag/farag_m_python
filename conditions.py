print("Rules that govern the state of water")

current_temp= False
while current_temp is False:
		current_temp = input("enter a tempature:\n")
		print(current_temp)

		if (int(current_temp) < 0) or (int(current_temp) == 0):
			print("water is now frozen fam.")
			current_temp=False


		elif (int(current_temp) <100):
			print("water is literally water dumbass")
			current_temp=False

		elif (int(current_temp) >100) or (int(current_temp) ==100):
			print("ay fam... your water is now in the sky... float on through brother <3")
			current_temp=False


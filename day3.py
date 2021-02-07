#Define the username and password(Without using dict)
# username = "arinc"
# password = "123456"

#Define the username and password(With using dict)
user_info = {"username": "arinc", "password": "123456"}

#Give user 3 chances to enter correct informations.
chance = 3
while(chance > 0):
	#Ask username:
	username_input = input("Please enter your username: ")

	#Ask password:
	password_input = input("Please enter your password: ")

	#Check the inputs match with username and password(Without using dict)
	# if username_input == username and password_input == password:
	# 	print(f"Login succesfully. Welcome {username}!")
	# 	break

	#Check the inputs match with username and password(With using dict)
	if username_input == user_info['username'] and password_input == user_info['password']:
		#Message without using dict
		#print(f"Login succesfully. Welcome {username}!")
		#Message with using dict
		print(f"Login succesfully. Welcome {user_info['username']}!")
		break

	#Decrement chances if user enter wrong informations
	chance -= 1

	if chance == 0:
		print("Sorry, you ruined all of your chances!!!")
		break

	#notify the user if he/she enters wrong, and display how many chance they have more.
	print(f"Incorrect username or password. You {chance} more chance(s).")
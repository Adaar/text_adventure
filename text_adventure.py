start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)
game_over = int(1)

def start():

	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()

	if user_input == "left":
		print("You decide to go left and...You trip on a vine, landing face first into a hedge. You cannot pull your head out and slowly starve to death.")
		print("Game Over")
		game_over = False

	elif user_input == "right":
		print("You choose to go right and ...You encounter a U-turn leading to a stairway.")
		print("Type 'up' to do up the stairs and 'down' to go down them.")
		user_input = input()

	if user_input == "up":
		print("Going up the stairs...a pressure plate clicks and a spiked log swings down, impaling you. Hope you had good life insurance. :] ")
	elif user_input == "down":
		print("You make your way into a damp, cicular room. In the center of the ivory room, there stands a marble statue of Aphrodite.")
		print("Her left hand extends to the western hallway whilst her right hand burls a fist toward the eastern hallway.")
		print("Choose your path. East or west?")
		user_input = input()

	if user_input == "east":
		print("Making your way down the hallway, you see a chest. Your greed takes over and you dash toward it, you monster.")
		print("The chest was a Mimic and eats you alive.")
		print("Game Over")
		game_over = False

	elif user_input == "west":
		print("Taking heed in the advice of the goddess you walk down the western path. You wander into a brightly lit room, there are men huddled by a fire.")
		print("Do you speak to them or attempt to sneak past? Enter 'speak' or 'sneak'.")

		campgrounds()

if game_over == True:

	print('''Upon standing, you freeze for a moment in quiet contemplation.
	Who does that sign think it is? How dare it try to control me!?
	Then again...you have no idea where you re right now and you mom always said to trust your gut.
	You wanna touch the wall?
	Type 'yes' if you wanna and 'no' if you don't.''')
	user_input = input()

	if user_input == "yes":
		print("You touch the wall, your hand pressing against the slightly prickly vines.")
		print("Before long you feel a gentle caress against your inner thigh.")
		print("Looking down, the leafy appendage has already slunk back into the wall.")
		print("You feel ...uncomfortable.")

		start()

	elif user_input == "no":
		print("Your gut is telling you that whatever the wall is, touching it will not end well.")
		print("So you don't.")

		start()

def campgrounds():
	if user_input == "sneak":
		print("Stealthy route eh? Alright.")
		print("Whats the plan then?")
		print("You can:")
		print("A - Try and do that roll around them")
	elif user_input == "speak":
		#TODO

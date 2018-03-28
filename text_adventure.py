import time

start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)
time.sleep(2)
game_over = int(1)
global score
score = 0

def sadlook():
	print("He gives you a saddened look, crossing his arms across his chest.")
	time.sleep(2)
	print("He then continues to explain his merry little gang's sitation.")
	time.sleep(2)
	print("'You've got a long time ahead, most of us have been here for days, weeks even.' he mutters.")
	time.sleep(2)
	print("Feel like joining their merry gang?")
	print("Yes or no?")
	user_input = input()

	if user_input == "yes" or user_input == "YES" or user_input == "Yes":
		time.sleep(2)
		print("You decide to join them.")
		time.sleep(2)
		print("Over time a few more people stumble uopn your group and they join aswell.")
		time.sleep(2)
		print("Together, you all go an a massive adventure in this mysterious maze.")
		time.sleep(2)
		print("It goes swell.")
		time.sleep(2)
		print("The End?")
		global score
		score += 5
		print ("Your score is %d ." % score)
		game_over = False

	elif user_input == "no" or user_input == "NO" or user_input == "No":
		time.sleep(2)
		print("You politely tell them that you'll be fine on your own.")
		time.sleep(2)
		print("You continue traversing this maze, alone.")
		time.sleep(2)
		print("There is rarely any piece and quiet however, there is always something creeping in the dark.")

		if touched_hedge == True:
			time.sleep(2)
			print("At least the ivy is there for you.")
			time.sleep(2)
			print("That is,")
			time.sleep(1)
			print("If you choose to touch it again.")
			global score
			score += 3
			print("The End?")
			print ("Your score is %d ." % score)
			game_over = False
		else:
			time.sleep(2)
			print("Who knows how long you survive and if you do, will you make it out this maze?")
			time.sleep(2)
			print("Does it even matter?")
			time.sleep(2)
			print("The End?")
			print ("Your score is %d ." % score)
			game_over = False



def dude():
	print("He gives you a quaint hello, nodding with a greeting.")
	time.sleep(2)
	print("'Another lost soul are you?' he says.")
	time.sleep(2)
	print("'We're all in the same boat!' he continued, extending his arm in the showing the rest of the group.")
	time.sleep(2)
	print("He asks you how long you've been wandering the maze.")
	time.sleep(2)
	print("You wanna tell him the truth?")
	time.sleep(2)
	print("Yay or nay?")
	user_input = input()

	if user_input == 'yay' or user_input == 'YAY' or user_input == "Yay" or user_input == 'yes' or user_input == 'Yes' or user_input ==  'YES':
		print("You tell him that you've only recently woken up and made over here not too long ago.")
		time.sleep(2)
		sadlook()

	elif user_input == 'nay' or user_input == "Nay" or user_input == 'NAY' or user_input == 'no' or user_input == 'NO' or user_input == "No":
		sadlook()


def speak():
	print("They glare at you.")
	time.sleep(2)
	print("I'd say you have about 1.5 seconds before they stand and do something.")
	time.sleep(2)
	print("You wanna say something or just let whatever happen?")
	time.sleep(2)
	print("So... 'silent' or 'nah'?")
	user_input = input()

	if user_input == 'silent':
		print("You just kinda stay still, looking back at them.")
		time.sleep(2)
		print("One of the men slowly rises and makes their way toward you.")
		time.sleep(2)
		print("Ya'know, you could try and run, but that might be a bad idea so I don't know.")
		time.sleep(2)
		print("You feel like bolting?")
		time.sleep(2)
		print("Up to you, yes or no?")
		user_input = input()

		if user_input == "yes" or user_input == "Yes" or user_input == 'YES':
			print("Alright! LETS RUN!")
			time.sleep(2)
			print("Wait.")
			time.sleep(2)
			print("Nevermind...seems like you're immobilized from fear.")
			time.sleep(2)
			print("Oh well.")
			score - 1

			dude()

		elif user_input == 'no' or  user_input == 'No' or user_input == "NO":
			score = score + 1
			dude()

	elif user_input == 'nah':
		print("You open your mouth too speak but before you can get a word out,")
		time.sleep(2)
		print("The man smacks his hand onto your shoulder with a grin.")
		time.sleep(2)
		global score
		score = score + 1

		dude()

def sneak():
	print("They notice and turn to face you.")

	speak()

def campgrounds():
	user_input = input()
	if user_input == "sneak":
		print("Stealthy route eh? Alright.")
		print("Whats the plan then?")
		time.sleep(1)
		print("You can:")
		time.sleep(1)
		print("A - Try and do that roll they do in movies around them.")
		time.sleep(2)
		print("B - Crouch and make your way past on your toes, trying not to make a sound.")
		time.sleep(2)
		print("C - Stick to the shadows and hope you aren't seen.")
		user_input = input()

		if user_input == "A" or user_input == "a":
			print("You fail miserably to roll and end up with your face on the ground and your butt in the air.")
			time.sleep(2)
			print("In short, you look stupid.")
			global score
			score = score - 1

			sneak()
		elif user_input == "B" or user_input == "b":
			print("You do your best, creeping along on your tippy toes but contrary from popular belief that actually makes far more sound than just walking on the balls of your feet.")
			global score
			score = score - 1

			sneak()
		elif user_input == "C" or user_input == "c":
			print("You feel like a ninja slipping in and out of darkness that you start to come up with one-liners to use and get distracted.")
			time.sleep(2)
			print("Its doesn't take very long as you step out into broad daylight.")
			global score
			score = score + 1

			sneak()

	elif user_input == "speak":
		speak()

def start():

	print("Type 'left' to go left or 'right' to go right.")
	user_input = input()

	if user_input == "left":
		print("You decide to go left and...You trip on a vine, landing face first into a hedge. You cannot pull your head out and slowly starve to death.")
		time.sleep(2)
		print("Game Over")
		global score
		score = score - 1
		print ("Your score is %d ." % score)
		game_over = False

	elif user_input == "right":
		print("You choose to go right and...")
		time.sleep(2)
		global score
		score = score+ 1
		print("You encounter a U-turn leading to a stairway.")
		time.sleep(2)
		print("Type 'up' to do up the stairs and 'down' to go down them.")
		user_input = input()

	if user_input == "up":
		print("Going up the stairs...a pressure plate clicks and a spiked log swings down, impaling you. Hope you had good life insurance. :] ")
		global score
		score = score - 1
		print ("Your score is %d ." % score)
		game_over = False

	elif user_input == "down":
		print("You make your way into a damp, circular room. In the center of the ivory room, there stands a marble statue of Aphrodite.")
		global score
		score = score + 1
		time.sleep(2)
		print("Her left hand extends to the western hallway whilst her right hand burls a fist toward the eastern hallway.")
		time.sleep(2)
		print("Choose your path. East or west?")
		user_input = input()

	if user_input == "east":
		print("Making your way down the hallway, you see a chest.")
		time.sleep(2)
		print("Your greed takes over and you dash toward it, you monster.")
		time.sleep(2)
		print("The chest was a Mimic and eats you alive.")
		time.sleep(2)
		global score
		score = score - 5
		print("Game Over")
		print ("Your score is %d." % score)
		game_over = False

	elif user_input == "west":
		print("Taking heed in the advice of the goddess you walk down the western path. You wander into a brightly lit room, there are men huddled by a fire.")
		global score
		score += 5
		time.sleep(2)
		print("Do you speak to them or attempt to sneak past? Enter 'speak' or 'sneak'.")

		campgrounds()

if game_over == True:

	print("Upon standing, you freeze for a moment in quiet contemplation.")
	time.sleep(2)
	print("Who does that sign think it is?")
	time.sleep(2)
	print("How dare it try to control me!?")
	time.sleep(2)
	print("Then again...you have no idea where you re right now and you mom always said to trust your gut.")
	time.sleep(2)
	print("You wanna touch the wall?")
	time.sleep(2)
	print("Type 'yes' if you wanna and 'no' if you don't.")
	user_input = input()

	if user_input == "yes":
		print("You touch the wall, your hand pressing against the slightly prickly vines.")
		time.sleep(2)
		print("Before long you feel a gentle caress against your inner thigh.")
		time.sleep(2)
		print("Looking down, the leafy appendage has already slunk back into the wall.")
		time.sleep(2)
		print("You feel...")
		time.sleep(2)
		print(".......uncomfortable.")
		time.sleep(2)
		score = score + 1

		start()

	elif user_input == "no":
		print("Your gut is telling you that whatever the wall is, touching it will not end well.")
		time.sleep(2)
		print("So you don't.")
		score = score + 1

		start()

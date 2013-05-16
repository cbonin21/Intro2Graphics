"""
Source: chooseYourOwnAdventure.py
Author: Craig Bonin
Last Modified By: Craig Bonin
Last Modified: 5/13/2013
Program Description: A simple text game with a series of choices that affects the outcome of the game.
Revision: 0.4

***************************************************
Revision History
***************************************************
0.1
- Simple Dragon.py Game
- Two choices
***************************************************
0.2
- Added Option to choose Foe
- Added Random Treasure Function
- Added Random Path Function
***************************************************
0.3
- Added Continuation of Story
- Added Enemy or Not Function
- Added endStory Function
***************************************************
0.4
- Added Player Array
- Added setPlayer function
- Added getPlayer function
- Changed code to use Player Array
- Adjusted Story

**************************************************
"""
#Imports of methods used.
import random
import time

#Function to display the choice option for which cave to choose form
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will' +  getPlayer(0) + ' go into? (1 or 2)')
		cave = raw_input()
	return cave

#Function that returns that random selects and returns the treasure that the foe droped
def treasureReward():
	number = random.randint(1,5)
	if number == 1:
		treasure = "Sword"
	elif number == 2:
		treasure = "Golden Chalice"
	elif number == 3:
		treasure = "Diamond Encrusted Tiara"
	elif number == 4:
		treasure = "Shield"
	elif number == 5:
		treasure = "Armor"
	return treasure

#Introduction to the game, allows for user to pick their foe.
def displayIntro():
	print("Welcome to Craig's")
	time.sleep(2)
	print("Choose your own Adventure Game!!!")
	time.sleep(2)
	print("Please enter in the foe you'd like to face...")
	time.sleep(2)
	foe = raw_input()
	print("Please enter in your name...")
	time.sleep(2)
	name = raw_input()
	print("Please enter difficulty level: 1-3")
	time.sleep(2)
	difficulty = raw_input()
	while difficulty > 3 or difficulty < 0 :
		print("Please enter difficulty level between 1-3")
		difficulty = raw_input()
	setPlayer(2, int(difficulty))
	setPlayer(1, foe)
	setPlayer(0, name)

#Intro function which sets the story, and describes the world and the foe.
def displayStoryIntro(foe):
	print(getPlayer(0) + " awakes not knowing exactly where they are is...")
	time.sleep(2)
	print("Suddenly a " + getPlayer(1) + " passes by in the distance...")
	time.sleep(2)
	print(getPlayer(0) + " watches as it enters into one of the two caves that lies ahead...")
	time.sleep(2)
	print(getPlayer(0) + " follows the " + getPlayer(1) + " to the caves...")
	time.sleep(2)

#Randomly creates a value and checks the users input against it.
def checkCave(chosenCave, foe):
	print(getPlayer(0) + ' approachs the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large ' + getPlayer(1) +' jumps out in front of ' + getPlayer(0) + '! He opens his jaws and...')
	print(" ")
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print ('Gives '+ getPlayer(0) + ' his treasure!')
		time.sleep(2)
		print (getPlayer(0) + ' continue down the cave..')
		time.sleep(2)
		print('Unsure of what the treasure is.')
		print(" ")
		setPlayer(3, treasureReward())
		setPlayer(6, 1)
	else:
		print('The ' + getPlayer(1) + ' moves to gobble '+ getPlayer(0) +' down!')
		time.sleep(2)
		print (getPlayer(0) + ' narrowly avoid being gobbled down by the ' + getPlayer(1) )
		time.sleep(2)
		print (getPlayer(0) + ' run down the cave thankful for their life...')
		print(" ")
		setPlayer(6, 2)

#Continuation of the story
def continueStory(treasure, location):
	if location == 1:
		
	else:
		
	

#Randomly decides on a path type and returns it. 
def randomPathType(number):
	if number == 1:
		path = "well traveled "
	if number == 2:
		path = "dirt "
	if number == 3:
		path = "stoney "
	if number == 4:
		path = "dark forest "
	return path

#Continues the story and determines whether or not the user runs into a foe and drops their treasure or finds a new one
def enemyOrNot(treasure, pathChoice, foe):
	number = random.randint(1,11)
	if (int(pathChoice) > int(number)):
		print("A " + foe + " jumps out from behind a bush...")
		time.sleep(2)
		print("You are frightened and drop everything you were holding!")
		if treasure != "None":
			print("You drop the " + treasure + " you found!")
			time.sleep(2)
			treasure = 'none'
			print("Oh no!")
		print("You manage to escape and continue down the path.")
	else:
		print("You continue down the path without a hitch...")
		time.sleep(2)
		print("When suddenly you trip over something...")
		time.sleep(2)
		tempTreasure = treasureReward()
		print("It's a " + tempTreasure )
		if treasure != 'none':
			print("Do you drop " + treasure + " for " + tempTreasure + "?")
			input = raw_input()
			if input == "y" or input == 'yes':
				print("You drop the " + treasure + " and pickup the " + tempTreasure)
				treasure = tempTreasure
			else:
				print("You leave the " + tempTreasure)
		else:
			print("You pickup the " + tempTreasure)
			treasure = tempTreasure
	return treasure

#Ends the story and determines whether or not the player survives
def endStory(treasure, foe):
	print("Your legs begin to tire from your long journey!")
	time.sleep(2)
	print("The path twists and continues over hills until you come to a fork...")
	time.sleep(2)
	print("Which path do you choose? 1 or 2")
	input = raw_input()
	if int(input) == random.randint(1,2):
		print("You choose to go down the path numbered " + input + "...")
		time.sleep(2)
		print("Before you lies a large castle, you enter it...")
		time.sleep(2)
		print("As you approach the throne a princess stands.")
		time.sleep(2)
		if treasure == 'none':
			print("You have nothing to offer the princess!")
			time.sleep(2)
			print("You are thrown in jail to rot!")
			alive = False
		elif treasure == 'Shield' or treasure == 'Sword' or treasure == 'Armor':
			print("You offer the " + treasure + " to the princess...")
			time.sleep(2)
			print("She is disgusted by your offer...")
			time.sleep(2)
			print("You are thrown in jail to rot!")
			alive = False
		else:
			print("You offer the " + treasure + " to the princess!")
			time.sleep(2)
			print("She loves the gift!")
			time.sleep(2)
			print("You are rewarded with a place to liveout your life!")
			time.sleep(2)
			alive = True
	else:
		print("You choose to go down the path numbered " + input + "...")
		time.sleep(2)
		print("You stumble upon a huge " + foe + "...")
		time.sleep(2)
		if treasure == 'none':
			print("You have nothing to offer the huge " + foe + "...")
			time.sleep(2)
			print("It crushes you and eats you.")
			alive = False
		elif treasure == 'Sword':
			print("You pull the Sword from your bag!")
			time.sleep(2)
			print("You use the sword to slay the huge " + foe)
			time.sleep(2)
			print("And decide to live out your days in it's home")
			alive = True
		elif treasure == 'Armor' or treasure == 'Shield':
			print("You pull the " + treasure + " from your bag!")
			time.sleep(2)
			print("The huge " + foe + " begins to attack!")
			time.sleep(2)
			print("You use the " + treasure + "to deflect the blows while countering!")
			time.sleep(2)
			print("You defeat the " + foe + " and live out your days in it's home")
			time.sleep(2)
			alive = true
		else:
			print("You offer the huge " + foe + " the " + treasure + "...")
			time.sleep(2)
			print("It doesn't look to impressed...")
			time.sleep(2)
			print("It crushes you and eats you")
			alive = false
	return alive
	
	
#Main function which makes calls to all of the other functions
def main():
	
	player = ['name', 'foe', 'life', 'none', False, True, '1']
	
	#Checks to see if user wants to play again.
	while getPlayer(5):
		displayIntro()
		displayStoryIntro(getPlayer())
		caveNumber = chooseCave()
		checkCave(caveNumber, getPlayer(1))
		continueStory(treasure, getPlayer(6))
		
		treasure = enemyOrNot(getPlayer(3), userChoice, getPlayer(1))
		print(" ")
		alive = endStory(getPlayer(3), getPlayer(1))
		
		#Displays final message as to whether or not the player survived
		if getPlayer(2) > 0:
			print ""
			print("Congradulations you have completed the game alive!")
		else :
			print ""
			print("You have failed and died during your journey...")
			time.sleep(2)
			print("Best of luck next time.")
		#Prompts player if they want to play again or not.
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()

if __name__ == "__main__": main()
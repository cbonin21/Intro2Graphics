"""
Source: chooseYourOwnAdventure.py
Author: Craig Bonin
Last Modified By: Craig Bonin
Last Modified: 5/13/2013
Program Description: A simple text game with a series of choices that affects the outcome of the game.
Revision: 0.1

"""
#Imports of methods used.
import random
import time

#Introduction to the game, allows for user to pick their foe.
def displayIntro():
	print("Welcome to Craig's")
	print("Choose your own Adventure Game!!!")
	print("Please enter in the foe you'd like to face...")
	foe = raw_input()
	return foe

#Intro function which sets the story, and describes the world and the foe.
def displayStoryIntro(foe):
	print('You are on a planet full of ' + foe + 's. In front of you,')
	print('you see two caves. In one cave, the ' + foe + ' is friendly')
	print('and will share his treasure with you. The other ' + foe + '')
	print('is greedy and hungry, and will eat you on sight.')
	
#Function to display the choice option for which cave to choose form
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will you go into? (1 or 2)')
		cave = raw_input()
	return cave

#Randomly creates a value and checks the users input against it.
def checkCave(chosenCave, foe):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large ' + foe +' jumps out in front of you! He opens his jaws and...')
	print(" ")
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print ('Gives you his treasure!')
		time.sleep(2)
		print ('You continue down the cave..')
		time.sleep(2)
		print('Unsure of what the treasure is.')
		print(" ")
		return True
	else:
		print('The ' + foe + ' moves to gobble you down!')
		time.sleep(3)
		print ('You narrowly avoid being gobbled down by the ' + foe )
		time.sleep(1)
		print ('You run down the cave thankful for your life...')
		print(" ")
		return False
	
#Function that returns that random selects and returns the treasure that the foe droped
def treasureReward():
	number = random.randint(1,5)
	if number == 1:
		treasure = "Sword"
	elif number == 2:
		treasure = "Golden Chalice"
	elif number == 3:
		treasure = "Tiara"
	elif number == 4:
		treasure = "Shield"
	elif number == 5:
		treasure = "Armor"
	return treasure

#Continuation of the story
def continueStory(treasure):
	print("The cave opens up the sun shines bright...")
	time.sleep(2)
	pathType = randomPathType(random.randint(1,4))
	print("Before you lies a "+ pathType + "path...")
	if treasure != "none":
		print("You finally get the chance to see the treasure...")
		time.sleep(2)
		print("You discover it's a " + treasure)
	print("You continue down the " + pathType + " path...")
	time.sleep(2)
	print("It then branches out into 10 directions!!")
	print("Which " + pathType + "path do you choose?")
	pathChoice = raw_input()
	print (" ")
	time.sleep(2)
	print("You decide to go down the " + pathType + " path numbered " + pathChoice)
	return pathChoice

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

def endStory(treasure, foe):
	print("Your legs begin to tire from your long journey!")
	print("The path twists and continues over hills until you come to a fork...")
	print("Which path do you choose? 1 or 2")
	input = raw_input()
	if int(input) == random.randint(1,2):
		print("You choose to go down the path numbered " + input + "...")
		print("Before you lies a large castle, you enter it...")
		time.sleep(2)
		print("As you approach the throne a princess stands.")
		if treasure == 'none':
			print("You have nothing to offer the princess!")
			print("You are thrown in jail to rot!")
			alive = False
		elif treasure == 'Shield' or treasure == 'Sword' or treasure == 'Armor':
			print("You offer the " + treasure + " to the princess...")
			time.sleep(2)
			print("She is disgusted by your offer...")
			print("You are thrown in jail to rot!")
			alive = False
		else:
			print("You offer the " + treasure + " to the princess!")
			print("She loves the gift!")
			print("You are rewarded with a place to liveout your life!")
			alive = True
	else:
		print("You choose to go down the path numbered " + input + "...")
		print("You stumble upon a huge " + foe + "...")
		time.sleep(2)
		if treasure == 'none':
			print("You have nothing to offer the huge " + foe + "...")
			print("It crushes you and eats you.")
			alive = False
		elif treasure == 'Sword':
			print("You pull the Sword from your bag!")
			print("You use the sword to slay the huge " + foe)
			print("And decide to live out your days in it's home")
			alive = True
		elif treasure == 'Armor' or treasure == 'Shield':
			print("You pull the " + treasure + " from your bag!")
			print("The huge " + foe + " begins to attack!")
			print("You use the " + treasure + "to deflect the blows while countering!")
			print("You defeat the " + foe + " and live out your days in it's home")
			alive = true
		else:
			print("You offer the huge " + foe + " the " + treasure + "...")
			time.sleep(2)
			print("It doesn't look to impressed...")
			print("It crushes you and eats you")
			alive = false
	return alive
	
	
#Main function which makes calls to all of the other functions
def main():
	
	#Variables used throughout program
	foe = ""
	alive = True
	receivedTreasure = False
	treasure = "none"
	counter = 0
	playAgain = 'yes'
	
	#Checks to see if user wants to play again.
	while playAgain == 'yes' or playAgain == 'y':
		foe = displayIntro()
		displayStoryIntro(foe)
		caveNumber = chooseCave()
		receivedTreasure = checkCave(caveNumber, foe)
		
		#Checks to see if player should receive a treasure
		if receivedTreasure:
			treasure = treasureReward()
			
		#Story continued
		userChoice = continueStory(treasure)
		treasure = enemyOrNot(treasure, userChoice, foe)
		print(" ")
		alive = endStory(treasure, foe)
		
		if alive == True:
			print("Congradulations you have completed the game alive!")
		else :
			print("You have failed and died during your journey...")
			time.sleep(2)
			print("Best of luck next time.")
		
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
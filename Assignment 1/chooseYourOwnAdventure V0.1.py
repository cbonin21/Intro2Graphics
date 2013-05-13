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
	print ('You are on a planet full of ' + foe + 's. In front of you,')
	print ('you see two caves. In one cave, the ' + foe + ' is friendly')
	print ('and will share his treasure with you. The other ' + foe + '')
	print ('is greedy and hungry, and will eat you on sight.')
	
#Function to display the choice option for which cave to choose form
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will you go into? (1 or 2)')
		cave = raw_input()
	return cave

#Randomly creates a value and checks the users input against it.
def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print ('Gives you his treasure!')
		return true
	else:
		print ('Gobbles you down in one bite!')
		return false
	
#Function that returns that random selects and returns the treasure that the foe droped
def treasureReward(number):
	if num == 1:
		treasure = "Sword"
	if num == 2:
		treasure = "Golden Chalice"
	if num == 3:
		treasure = "Tiara"
	if num == 4:
		treasure = "Shield"
	if num == 5:
		treasure = "Armor"
	return treasure

#Randomly decides on a path type and returns it. 
def randomPath(number):
	if num == 1:
		path = "well traveled "
	if num == 2:
		path = "dirt "
	if num == 3:
		path = "stoney "
	if num == 4:
		path = "dark forest "
	return path
		
#Main function which makes calls to all of the other functions
def main():
	
	foe = ""
	alive = true
	treasure = ""
	counter = 0
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		foe = displayIntro()
		displayStoryIntro(foe)
		caveNumber = chooseCave()
		alive = checkCave(caveNumber)
		while alive == true:
			treasure = treasureReward(random.randint(1,5))
			print("You received a treasure, but it's to dark to tell what it is")
			print("The cave opens up to a...")
			
			
				
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()

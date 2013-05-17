"""
Source: chooseYourOwnAdventure.py
Author: Craig Bonin
Last Modified By: Craig Bonin
Last Modified: 5/17/2013
Program Description: A simple text game with a series of choices that affects the outcome of the game.
Revision: 0.5

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
0.5
- Moved Functions around
- Removed & Renamed
- Developed Story
- Removed Bugs
- Added decisions
- Added functions is_Number, DisplayStory1, DisplayStory2, DisplayStory3
- Added life functionality.

"""
#Imports of methods used.
import random
import time

#Number Checker for error checking.
def is_Number(num):
    try:
        num = int(num)
        return True
    except TypeError:
        return False

#Randomly decides on a path type and returns it. 
def randomPathType():
    number = random.randint(1, 5)
    if number == 1:
        path = " well traveled path "
    if number == 2:
        path = " dirt path "
    if number == 3:
        path = " stoney path"
    if number == 4:
        path = " dark forest path"
    if number == 5:
        path = " brick path"
    return path

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

#Introduction to the game, allows for user to pick their foe, name, difficulty level
def displayIntro():
    #User Input
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
    difficulty = ""
    #Error Checking
    while difficulty != '1' and difficulty != '2' and difficulty != '3':
        print("Please enter difficulty level between 1-3 (3 = Easy) (1 = Hard)")
        time.sleep(2)
        difficulty = raw_input()
        difficulty = str(difficulty)
    #Conversion
    difficulty = int(difficulty)
    player = [name, foe, difficulty, 'None', False, 0]
    return player

#First continuation of the story
def displayStory1(name, foe, life, treasure, cheat, location):
    #Starting story
    print(name + " awakes not knowing exactly where they are is...")
    time.sleep(2)
    print("Suddenly a " + foe + " passes by in the distance...")
    time.sleep(2)
    print(name + " watches as it enters into one of the two caves that lies ahead...")
    time.sleep(2)
    print(name + " follows the " + foe + " to the caves...")
    time.sleep(2)
    cave = ''
    
    #User Prompt
    while cave != '1' and cave != '2' and cave != 'comp2022':
        print ('Which cave will ' +  name + ' go into? (1 or 2)')
        cave = raw_input()
        cave = str(cave)
        
    #Determining friendly cave
    print(name + ' approachs the cave...')
    time.sleep(2)
    print('It is very dark and spooky...')
    time.sleep(2)
    friendlyCave = random.randint(1, 2)
    
    
    #Check cave and friendly cave
    if cave == str(friendlyCave):
        print (' As '+ name + ' enters the cave they see a treasure that lies ahead...')
        time.sleep(2)
        print (name + ' continues towards the treasure carefully and picks it up...')
        time.sleep(2)
        print(name + ' is unsure of what the treasure is but picks it up anyways.')
        treasure = treasureReward()
        location = 1
        print(" ")
    
    elif cave == 'comp2022':
        print("You cheater!!!....")
        print("          .")
        print("         ..")
        print("        ...")
        print("       ....")
        print("      .....")
        print("     ......")
        print("    .......")
        print("   ........")
        print("  .........")
        print("   ........")
        print("    .......")
        print("     ......")
        print("      .....")   
        print("       ....")
        print("        ...")
        print("         ..")
        print("          .")
        time.sleep(5)
        print("That's ok though we like cheaters")
        cheat = True;
        name = 'Cheater!'
    else:
        print('A ' + foe + ' inside of the cave moves to gobble '+ name +' down!')
        time.sleep(2)
        print (name + ' narrowly avoid being gobbled down by the ' + foe )
        time.sleep(2)
        print (name + ' run down the cave thankful for their life only escaping partially injured...')
        time.sleep(2)
        print("Lost 1 life!")
        life = int(life)
        life -= 1
        treasure = 'none'
        
        if( life == 0):
            print"You have died!"
        location = 2
        print(" ")
    player = [name, foe, life, treasure, cheat, location]
    return player

def displayStory2(name, foe, life, treasure,cheat, location):
    
    if int(location) == 1:
        print(name + " continues on through the cave...")
        print("Suddenly a large " + foe + " attacks...")
        print(name + " runs...")
        print("The " + foe + " gives chase...")
        print("The cave splits into two directions!")
        direction = ""
        while direction != 'left' and direction != 'right':
            print("Which way will " + name + " go? left or right")
            direction = raw_input()
            direction = str(direction)
        if direction == 'left':
            path = randomPathType()
            print("The cave opens up to a " + path + "...")
            print(name + " runs down it and escapes...")
            print(name + " checks their treasure...")
            print(".")
            print("..")
            print("...")
            print("It's a " + treasure + "!!!")
            location = 1
        else:
            print(name + " travels further into the dark cave...")
            print(name + " unsure of when it will ends hoping they will see daylight again!")
            location = 2
    else:
        print(name + " continues after narrowly escaping the " + foe + "...")
        print(name + " continues and finds the cave ends after a short while...")
        print("On exiting " + name + "sees the road opens up to many different directions...")
        userChoice = 11
        
        while userChoice > 10 or userChoice < 1:
            print("Which way will " + name + " go? 1-10")
            userChoice = raw_input()
            userChoiceNum = is_Number(userChoice)
            if userChoiceNum:
                userChoice= int(userChoice)
            
        number = random.randint(1,10)
        print(name + " takes the path numbered " + str(userChoice))
        
        if userChoice >= number:
            print("Up ahead " + name +" sees some smoke in the distance...")
            location = 3
        else:
            print("Up ahead " + name +" sees a large forest!")
            location = 4
    player  = [name, foe, life, treasure, False, location]
    return player

def displayStory3(name, foe, life, treasure,cheat, location):
    
    if(location == 1):
        
    elif(location == 2):
        
    elif(location == 3):
    
    else:
        
            
        
def main():
    #Array/List used throughout game. Contains Character Name, Foe Name, Life, Treasure, Cheats Enabled, Location 
    playAgain = True
    
    while playAgain:
        player = ['name', 'foe', 'life', 'treasure', False, 0]
        player = displayIntro()
        player = displayStory1(player[0], player[1], player[2], player[3], player[4], player[5])
        #Checking cheatCode
        if player[4]:
            player[3] = 'Tiara'
        else:
            if player[2] == 0:
                print("Sorry try again!")
                print("Thanks!!")
            else:
                player = displayStory2(player[0], player[1], player[2], player[3], player[4], player[5])
        
        if player[2] != '0':
            print("")
            player = displayStory3(player[0], player[1], player[2], player[3], player[4], player[5])
            
        
        
        
if __name__ == "__main__": main()
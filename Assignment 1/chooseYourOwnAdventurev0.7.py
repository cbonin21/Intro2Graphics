"""
Source: chooseYourOwnAdventure.py
Author: Craig Bonin
Last Modified By: Craig Bonin
Last Modified: 5/21/2013
Program Description: A simple text game with a series of choices that affects the outcome of the game.
Revision: 0.6

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
**************************************************
0.6
- Added time.sleep()'s
- Finished story
- Tested
**************************************************
0.7
- Caught a bug
- Added Decision node comments


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

"""
Start of Story.

Decision node one, player chooses cave one or two random cave is chosen as right one. 
Player either finds treasure or is harmed by monster.
Player can type Cheat code.

"""
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
        
    #Checking for cheatcode
    elif cave == 'comp2022':
        print("You cheater!!!....")
        
        dots = "."
        counter = 0
        
        while counter <= 9 :
            print(dots)
            dots += "."
            counter += 1
            time.sleep(1)
        
        counter = 1
        
        while counter <= 8 :
            print(dots[counter:])
            counter += 1
            time.sleep(1)
        
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
        
        #Checking for Death
        if( life == 0):
            print"You have died!"
        location = 2
        print(" ")
    player = [name, foe, life, treasure, cheat, location]
    return player

"""
Story continued

Decision Node 2:
If player is at location 1 they get attacked and then have to choose left or right.

If player is at location 2 (didn't find treasure) the cave opens up to a pathway that splits multiple directions. 

"""
def displayStory2(name, foe, life, treasure,cheat, location):
    
    #For location 1
    if int(location) == 1:
        print(name + " continues on through the cave...")
        time.sleep(2)
        print("Suddenly a large " + foe + " attacks...")
        time.sleep(2)
        print(name + " runs...")
        time.sleep(2)
        print("The " + foe + " gives chase...")
        time.sleep(2)
        print("The cave splits into two directions!")
        time.sleep(2)
        direction = ""
        while direction != 'left' and direction != 'right':
            print("Which way will " + name + " go? left or right")
            time.sleep(2)
            direction = raw_input()
            direction = str(direction)
        if direction == 'left':
            path = randomPathType()
            print("The cave opens up to a " + path + "...")
            time.sleep(2)
            print(name + " runs down it and escapes...")
            time.sleep(2)
            print(name + " checks their treasure...")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("It's a " + treasure + "!!!")
            time.sleep(2)
            location = 1
        else:
            print(name + " travels further into the dark cave...")
            time.sleep(2)
            print(name + " unsure of when it will ends hoping they will see daylight again!")
            time.sleep(2)
            location = 2
    #For location 2
    else:
        print(name + " continues after narrowly escaping the " + foe + "...")
        time.sleep(2)
        print(name + " continues and finds the cave ends after a short while...")
        time.sleep(2)
        print("On exiting " + name + "sees the road opens up to many different directions...")
        time.sleep(2)
        userChoice = 11
        
        while userChoice > 10 or userChoice < 1:
            print("Which way will " + name + " go? 1-10")
            time.sleep(2)
            userChoice = raw_input()
            userChoiceNum = is_Number(userChoice)
            if userChoiceNum:
                userChoice= int(userChoice)
            
        number = random.randint(1,10)
        print(name + " takes the path numbered " + str(userChoice))
        time.sleep(2)
                
        if userChoice >= number:
            print("Up ahead " + name +" sees some smoke in the distance...")
            time.sleep(2)
            location = 3
        else:
            print("Up ahead " + name +" sees a large forest!")
            time.sleep(2)
            location = 4
    player  = [name, foe, life, treasure, False, location]
    return player

"""
Ends story

If at location 1 a large castle is approached and user has to choose what to say to guard.

If at location 2 the player is still stuck in the cave and has to choose left or right again.

If at location 3 the player encounters bandits and has to decide what to do.

If at location 4 the player is in a forest and encounters a tiger, has to choose what to do.

All of the locations except for location 1 with the right input lead to the player losing.

"""
def displayStory3(name, foe, life, treasure,cheat, location):
    
    #Different scenarios based upon locations.
    if(location == 1):
        print ("Up ahead " + name + " spots a large castle.")
        time.sleep(2)
        print ("As they approach it they begin to realize how big it truly is.")
        time.sleep(2)
        print ('"HALT! WHO GOES THERE" a guard yells at ' + name)
        time.sleep(2)
        userInput = ""
        
        while userInput != 'a traveler' and userInput!= 'a enemy' :
            print ("How will you repsond? 'a traveler' or 'a enemy'" )
            time.sleep(2)
            userInput = str(raw_input())
        
        if userInput == 'a traveler':
            print("The guard opens the door and invites " + name + "in...")
            time.sleep(2)
            print("Before " + name + " stands a princess...")
            time.sleep(2)
            print(name + " offers the " + treasure + " that they found")
            time.sleep(2)
            print("The princess is happy!")
            time.sleep(2)
            print("You Won!")
            time.sleep(2)
        else:
            print("The guard slays " + name)
            time.sleep(2)
            print("You Lost! Better luck next time!")
            time.sleep(2)
            
    elif(location == 2):
        print(name + " continues hopelessly through the tunnels")
        time.sleep(2)
        print(name + " comes across another fork in the road")
        time.sleep(2)
        userInput = ""
        while userInput != 'left' and userInput != 'right':
            print("Which way will " + name + " go? left or right?")
            userInput = str(raw_input())
            
        if userInput == 'left':
            print(name + " goes left and feels the ground giveout below...")
            time.sleep(2)
            print(name + " fell into spikes")
            time.sleep(2)
        else:
            print(name + " goes right when suddenly blackness is everywhere...")
            time.sleep(2)
            print("A " + foe + " gobbled " + name + " up!")
            time.sleep(2)
            
        print("You lost! Better luck next time!")
            
    elif(location == 3):
        
        print(name + " continues forward and sees it's a group of bandits!")
        time.sleep(2)
        userInput = ""
        
        while userInput != 'run' and userInput != 'run at':
            print("What will " + name + " do? 'run' or 'run at'")
            time.sleep(2)
            userInput = raw_input()
            
        if userInput == 'run at':
            print(name + " runs at the group of bandits.")
            time.sleep(2)
            print("The bandits quickly overpower " + name)
            time.sleep(2)
            print("A group of " + foe +  " bandits keep " + name + " as their prisoner...")
            time.sleep(2)
        else:
            print(name + " attempts to run from the bandits.")
            time.sleep(2)
            print("The group of " + foe + " bandits catch and kill " + name)
            time.sleep(2)
            
        print("You lost! Better luck next time!")
        time.sleep(2)
    else:
        print(name + " enters the dark forest...")
        time.sleep(2)
        print(name + " hears a deep growl from off to the right..")
        time.sleep(2)
        userInput = ""
        
        while userInput != 'run left' and userInput != 'run at' :
            print("What will " + name + " do? 'run left' or 'run at' the sound")
            time.sleep(2)
            userInput = raw_input()
        
        if userInput == 'run left':
            print(name + " starts to run left away from the sound but...")
            time.sleep(2)
            print(name + " falls into a bushel of poisonous plants and dies!")
            time.sleep(2)
        else:
            print(name + " runs at the noise...")
            time.sleep(2)
            print(name + " is attacked by a strange tiger like animal and killed!")
            time.sleep(2)
        
        print("You lost! Better luck next time!")
    time.sleep(2)
    
def main():
    #Array/List used throughout game. Contains Character Name, Foe Name, Life, Treasure, Cheats Enabled, Location 
    playAgain = True
    
    #Checks to see if playAgain is true then starts the game. Displaying Intro
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
                
        #Checks to see if the player is alove and starts the end of the story.
        if player[2] != '0':
            print("")
            displayStory3(player[0], player[1], player[2], player[3], player[4], player[5])
            print("Thanks!")
        userChoice = ""
        
        #Prompts user for answer.
        while userChoice != 'n' and userChoice != 'y':
            print("Play again? y or n")
            userChoice = raw_input()
            
        #Checks user's answer.
        userChoice = str(userChoice)
        if userChoice == 'n':
            playAgain = False
        
if __name__ == "__main__": main()
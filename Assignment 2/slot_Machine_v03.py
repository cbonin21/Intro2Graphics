"""
Source File Name: slotMachine.py
Author's Name: Craig Bonin
Last Modified: 6/1/2013
Last Modified By: Craig Bonin
*************************************
Program Description-
This program simulates a slot machine. It provides the user with a gui to interact with the slot machine

*****************************************
Version History
*****************************************
v0.1
- Created GUI
- Added Basic Functionality
*****************************************
v0.2
- Checked to see if user had lost!
- Added quit button
- Commented more code
*****************************************
v0.3
- Added Ambient, spin, jackpot sounds

"""
import pygame, random, sys

def Spin(bet, credits, jackpot):
    
    #Variables used throughout Loop
    counter = 3
    amountWon = 0
    reel = ""
    message = ""
    
    #Looping through randomly selecting images and applying them to reels.
    while counter != 0:
        # Spin Reel 3 times and determine what will be in eacah reel.
        number = random.randint(1, 64)
        if number >= 1 and number <=26:   # 40.10% Chance
            reel = "blank.png"
            result = 0
        if number >= 27 and number <=36:  # 16.15% Chance
            reel = "bar.png"
            result = 1
        if number >= 37 and number <=45:  # 13.54% Chance
            reel = "bar2.png"
            result = 2
        if number >= 46 and number <=53:  # 11.98% Chance
            reel = "bar3.png"
            result = 3
        if number >= 54 and number <=58:  # 7.29%  Chance
            reel = "grapes.png"
            result = 4
        if number >= 59 and number <=61:  # 5.73%  Chance
            reel = "cherries.png"
            result = 5
        if number >= 62 and number <=63:  # 3.65%  Chance
            reel = "seven.png"
            result = 6  
        if number == 64:                  # 1.56%  Chance
            reel = "jackpot.png"
            result = 7
        
        #Loading reels with Images
        if counter == 1:
            reel1 = pygame.image.load(reel)
            reel1 = reel1.convert()
            result1 = result
        elif counter == 2:
            reel2 = pygame.image.load(reel)
            reel2 = reel2.convert()
            result2 = result
        else:
            reel3 = pygame.image.load(reel)
            reel3 = reel3.convert()
            result3 = result
        #Updating counter
        counter = counter - 1
        
    #Updating Jackpot
    jackpot = jackpot + round((bet * 0.10),0)
        
    #Checking results
    if result1 == 1 and result2 == 1 and result3 == 1:
        amountWon = bet + round((bet * 0.10),0)
        credits = credits + amountWon
    elif result1 == 2 and result2 == 2 and result3 == 2:
        amountWon = bet + round((bet * 0.15),0)
        credits = credits + amountWon
    elif result1 == 3 and result2 == 3 and result3 == 3:
        amountWon = bet + round((bet * 0.20),0)
        credits = credits + amountWon
    elif result1 == 4 and result2 == 4 and result3 == 4:
        amountWon = bet + round((bet * 0.30),0)
        credits = credits + amountWon
    elif result1 == 5 and result2 == 5 and result3 == 5:
        amountWon = bet + round((bet * 0.40),0)
        credits = credits + amountWon
    elif result1 == 6 and result2 == 6 and result3 == 6:
        amountWon = bet + round((bet * 0.75),0)
        credits = credits + amountWon
    elif result1 == 7 and result2 == 7 and result3 == 7:
        amountWon = bet + jackpot
        credits = credits + amountWon
        message = "YOU WON THE JACKPOT!!!! WOOOT WOOT"
        jackpotSound = pygame.mixer.Sound("jackpot.wav")
    else:
        credits = credits - bet
    #Returning Results
    return reel1, reel2, reel3, amountWon, jackpot, credits, message
        
def main():
    
    #Variables used throughout
    credits = 1000
    bet = 0
    amountWon = 0
    jackpot = 1000
    message = "Welcome to Craig's Slot Machine"
    
    #Setting up Pygame
    pygame.init()
    pygame.mixer.init()
    
    #Setting up graphics
    screen = pygame.display.set_mode((400, 500))
    pygame.display.set_caption("Craig's Slot Machine")
    background = pygame.image.load("Slot_Machine_Base.png")
    background = background.convert()
    reel1 = pygame.image.load("jackpot.png")
    reel1 = reel1.convert()
    reel2 = pygame.image.load("jackpot.png")
    reel2 = reel2.convert()
    reel3 = pygame.image.load("jackpot.png")
    reel3 = reel3.convert()
    
    #Sounds
    sound = pygame.mixer.Sound("casinoSound.wav")
    sound.play(-1, 0, 0)
    
    spinSound = pygame.mixer.Sound("spin.wav")
    
    
    #Labels used throughout GUI
    myfont = pygame.font.SysFont("Arial", 15)
    labelCredits = myfont.render(str(credits), 1, (0, 0, 0))
    labelBet = myfont.render(str(bet), 1, (0,0,0))
    labelAmountWon = myfont.render(str(amountWon), 1, (0,0,0))
    labelJackpot = myfont.render(str(jackpot), 1, (0,0,0))
    labelMessage = myfont.render(message, 1, (0,0,0))
    
    #Setting frame rate and gameloop
    keepGoing = True
    fps = pygame.time.Clock()
    
    while keepGoing:
        fps.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            #Checking Mouse button and location.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                print location[0]
                print location[1]
                #If mouse location is on bet 25
                if (location[0] >= 19 and location[0] <= 119) and (location[1] >= 277 and location[1] <= 328):
                    if credits < 25:
                        message = "Cannot bet more then credits"
                        bet = 0
                    else:  
                        bet = 25
                        message = ""
                    labelMessage = myfont.render(message, 1, (0,0,0))
                    labelBet = myfont.render(str(bet), 1, (0,0,0))
                #If mouse location is on bet 50    
                elif (location[0] >= 136 and location[0] <= 236) and (location[1] >= 277 and location[1] <= 328):
                    if credits < 50:
                        message = "Cannot bet more then credits"
                        bet = 0
                    else:    
                        bet = 50
                        message = ""
                    labelMessage = myfont.render(message, 1, (0,0,0))
                    labelBet = myfont.render(str(bet), 1, (0,0,0))
                #If mouse location is on bet 100
                elif (location[0] >= 259 and location[0] <= 358) and (location[1] >= 277 and location[1] <= 328):
                    if credits < 100:
                        message = "Cannot bet more then credits"
                        bet = 0
                    else:
                        bet = 100
                        message = ""
                    labelMessage = myfont.render(message, 1, (0,0,0))
                    labelBet = myfont.render(str(bet), 1, (0,0,0))
                #If mouse location is on Spin  
                elif (location[0] >= 47 and location[0] <= 314) and (location[1] >= 356 and location[1] <= 436):
                    #Spin occurs updates all of the labels and checks bet and credits.
                    if bet != 0 and credits != 0 and credits >= bet:
                        message = ""
                        spinSound.play()
                        reel1, reel2, reel3, amountWon, jackpot, credits, message = Spin(bet, credits, jackpot)
                        labelAmountWon = myfont.render(str(amountWon), 1, (0,0,0))
                        labelJackpot = myfont.render(str(int(jackpot)), 1, (0,0,0))
                        labelCredits = myfont.render(str(credits), 1, (0, 0, 0))
                        
                    else:
                        message = "Please pick a suitable bet amount"
                    labelMessage = myfont.render(message, 1, (0,0,0))
                #If mouse location is on Reset
                elif (location[0] >= 285 and location[0] <= 386) and (location[1] >= 460 and location[1] <= 486):
                    credits = 1000
                    bet = 0
                    amountWon = 0
                    jackpot = 1000
                    message = "Game Reset"
                    labelAmountWon = myfont.render(str(amountWon), 1, (0,0,0))
                    labelJackpot = myfont.render(str(jackpot), 1, (0,0,0))
                    labelCredits = myfont.render(str(credits), 1, (0, 0, 0))
                    labelBet = myfont.render(str(bet), 1, (0,0,0))
                    labelMessage = myfont.render(message, 1, (0,0,0))
                    reel1 = pygame.image.load("jackpot.png")
                    reel1 = reel1.convert()
                    reel2 = pygame.image.load("jackpot.png")
                    reel2 = reel2.convert()
                    reel3 = pygame.image.load("jackpot.png")
                    reel3 = reel3.convert()
                #If mouse clicks quit
                elif (location[0] >= 21 and location[0] <= 123) and (location[1] >= 457 and location[1] <= 482):
                    keepGoing = False
        #Checking to make sure that user has credits.
        if credits <= 0:
            bet =0
            message = "You have lost! Press Reset to play again!"
            labelMessage = myfont.render(message, 1, (0,0,0))
        #Updating screen objects.           
        screen.blit(background, (0,0))
        screen.blit(labelCredits, (100, 211))
        screen.blit(labelBet, (282,210))
        screen.blit(labelAmountWon, (199,47))
        screen.blit(labelJackpot, (142,12))
        screen.blit(labelMessage, (21,246))
        screen.blit(reel1, (40,78))
        screen.blit(reel2, (151,78))
        screen.blit(reel3, (261,78))
        
        pygame.display.update()
        
if __name__ == "__main__": main()
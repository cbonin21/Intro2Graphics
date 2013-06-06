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
-Started Assignment

"""

#Import and initialize pygame
import pygame

def main():
    pygame.init()
    
    #Setting up Graphics
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Craig's Slot Machine")
    background = pygame.surface(screen.getsize())
    background = background.convert()
    betFont = pygame.font.SysFont("arial", 12)
    
    
    #Variables used throughout game
    clock = pygame.time.Clock()
    keepGoing = True
    userMoney = 1000
    userBet = 10
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = false
            
            screen.blit(background, (0,0))
            pygame.display.flip()
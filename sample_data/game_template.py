#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""
# 0. Import libraries
import pygame 
import sys

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 3. Launch a game window
window = pygame.display.set_mode((600, 400))


# 4. Set up the main game loop
while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 5. Draw
    window.fill(blue)

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
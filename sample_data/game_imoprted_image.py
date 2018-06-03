#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""
# 0. Import libraries
import pygame 
import sys
import random

x = 0
y = 1

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.1 Position and velocity variables 
monster_pos =[200, 200]                   
saucer_pos = [200, 25]
    
saucer_vel = [0,0]
monster_vel = [random.randrange(2,4), random.randrange(1,3)]
if random.randrange(0,2) == 0:
    monster_vel[x] *= -1
if random.randrange(0,2) == 0:
    monster_vel[y] *= -1
 

# 3. Launch a game window
window = pygame.display.set_mode((800, 600))

background = pygame.image.load("../img/space.jpg").convert()
#player = pygame.image.load("../img/rabbit.png")
saucer = pygame.image.load("../img/saucer.png")
#spaceship = pygame.image.load("../img/spaceship.png")
#spaceship.set_colorkey(white)

#shuttle = pygame.image.load("../img/shuttle.png")
#shuttle.set_colorkey(white)

monster = pygame.image.load("../img/monster.gif")
monster.set_colorkey(white)



# 4. Set up the main game loop
while True:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
    # 4.1 Calculations : Reverse direction of travel if edge is reached
    if monster_pos[x] > (800-120) or monster_pos[x] < -120:
        monster_vel[x] *= -1
    if monster_pos[y] > (600-90) or monster_pos[y] < -90:
        monster_vel[y] *= -1
        
    # 4.2 Calculations : Update position
    monster_pos[x] += monster_vel[x]
    monster_pos[y] += monster_vel[y]
    saucer_pos[x] += saucer_vel[x]
    saucer_pos[y] += saucer_vel[y]
    
    
    
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 5. Draw
    #window.fill(blue)
    window.blit(background, [0, 0])
    window.blit(saucer, saucer_pos)
#    window.blit(spaceship, (300, 300))
#    window.blit(shuttle, [200, 200])
    window.blit(monster, monster_pos)

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
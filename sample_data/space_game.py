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
import math

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
    
saucer_vel = [0, 0]
monster_vel = [random.randrange(2,4), random.randrange(1,3)]
if random.randrange(0,2) == 0:
    monster_vel[x] *= -1
if random.randrange(0,2) == 0:
    monster_vel[y] *= -1
    
# 2.2 List to store shots 
shots = []
 

# 3. Launch a game window
window = pygame.display.set_mode((800, 600))

background = pygame.image.load("../img/space.jpg").convert()
#player = pygame.image.load("../img/rabbit.png")
saucer = pygame.image.load("../img/saucer.png")
fire = pygame.image.load("../img/fire.png")
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
        
    # 4.1 Event loop
    # 4.1.1 : Key press 
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP] & pressed[pygame.K_DOWN]: 
            saucer_vel[y] = 0
    elif pressed[pygame.K_UP]: 
            saucer_vel[y] = -8
    elif pressed[pygame.K_DOWN]: 
            saucer_vel[y] = 8
    else: 
            saucer_vel[y] = 0
            
    if pressed[pygame.K_LEFT] & pressed[pygame.K_RIGHT]: 
            saucer_vel[x] = 0
    elif pressed[pygame.K_LEFT]: 
            saucer_vel[x] = -8
    elif pressed[pygame.K_RIGHT]: 
            saucer_vel[x] = 8
    else: 
            saucer_vel[x] = 0
            
    # 4.1.2 : Mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # 4.1.3 : Mouse click
    if event.type==pygame.MOUSEBUTTONDOWN:
        mouse_click = True
    else:
        mouse_click = False

        
    # 4.2 Calculations  
    # 4.2.1 Reverse direction of travel if edge is reached
    if monster_pos[x] > (800-120) or monster_pos[x] < -120:
        monster_vel[x] *= -1
    if monster_pos[y] > (600-90) or monster_pos[y] < -90:
        monster_vel[y] *= -1
        
    # 4.2.2 Update position
    monster_pos[x] += monster_vel[x]
    monster_pos[y] += monster_vel[y]
    saucer_pos[x] += saucer_vel[x]
    saucer_pos[y] += saucer_vel[y]
    
    # 4.2.3 Angle between mouse and saucer
#    angle = math.atan2((mouse_pos[x]-(saucer_pos[x]+80)),
#                       -(mouse_pos[y]-(saucer_pos[y]+39)))
    angle = math.atan2(-(mouse_pos[y]-(saucer_pos[y]+39)),
                        (mouse_pos[x]-(saucer_pos[x]+80)))
    #angle = math.degrees(angle)-90
    angle -= math.pi/2

    
    # 4.2.4 Rotate the saucer
    saucer_r = pygame.transform.rotate(saucer, math.degrees(angle))
    
    # 4.2.5 Fire a shot
    if mouse_click:
        
        # if the mouse is clicked, a shot is added to the list of shots
        shot_pos = [saucer_pos[x]+80, saucer_pos[y]+39]
        shots.append([angle, shot_pos])
        
        # iterate over all shots, giving each one a number
        for n, shot in enumerate(shots):
            speed = 10
            shot_vel = [math.cos(shot[0])*speed, 
                        math.sin(shot[0])*speed]
            shot[1][x] += shot_vel[x]
            shot[1][y] += shot_vel[y]
            
            # if the fireball leaves the screen, remove it from the list of shots
            if (shot[1][x] > 800 + 94 or 
                shot[1][x] < -94 or 
                shot[1][y] > 600 + 94 or 
                shot[1][y] < -94):
                shots.pop(n)
                
                
            
    
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 5. Draw
    #window.fill(blue)
    window.blit(background, [0, 0])
    #window.blit(saucer, saucer_pos)
    window.blit(saucer_r, saucer_pos)
#    window.blit(spaceship, (300, 300))
#    window.blit(shuttle, [200, 200])
    window.blit(monster, monster_pos)

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
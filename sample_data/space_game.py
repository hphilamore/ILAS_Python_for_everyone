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

monster = True

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
 
window = pygame.display.set_mode((800, 600))


background = pygame.image.load("../img/space.jpg").convert()
b_size = pygame.Rect(background.get_rect()).size


saucer = pygame.image.load("../img/saucer.png")
s_size = pygame.Rect(saucer.get_rect()).size

fire = pygame.image.load("../img/fire.png")
f_size = pygame.Rect(fire.get_rect()).size

monster = pygame.image.load("../img/monster.gif")
m_size = pygame.Rect(monster.get_rect()).size
monster.set_colorkey(white)


# 3. Launch a game window




# 4. Set up the main game loop
while True:
    #print("space_center", rectangle.size)
    #print("space_center", rectangle.width)
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
#    if monster_pos[x] > (b_size[x] - m_size[x]) or monster_pos[x] < 0:
#        monster_vel[x] *= -1
#    if monster_pos[y] > (b_size[y]-m_size[y]) or monster_pos[y] < 0:
#        monster_vel[y] *= -1
        
    if monster_pos[x] > (b_size[x] - m_size[x]) or monster_pos[x] < m_size[x]:
        monster_vel[x] *= -1
    if monster_pos[y] > (b_size[y]-m_size[y]) or monster_pos[y] < m_size[y]:
        monster_vel[y] *= -1
        
    # 4.2.2 Update position
    monster_pos[x] += monster_vel[x]
    monster_pos[y] += monster_vel[y]
    saucer_pos[x] += saucer_vel[x]
    saucer_pos[y] += saucer_vel[y]
    
    # 4.2.3 Angle between mouse and saucer
    angle = math.atan2(-(mouse_pos[y] - (saucer_pos[y] + s_size[y]/2)),
                        (mouse_pos[x] - (saucer_pos[x] + s_size[x]/2)))
    #angle = math.degrees(angle)-90
    #angle #-= math.pi/2

    
    # 4.2.4 Rotate the saucer
    saucer_r = pygame.transform.rotate(saucer, math.degrees(angle) - 90)

    
    # 4.2.5 Fire a shot
    if mouse_click:
        
        # if the mouse is clicked, a shot is added to the list of shots
        shot_pos = [saucer_pos[x] + s_size[x]/2 - f_size[x]/2, 
                    saucer_pos[y] + s_size[y]/2 - f_size[y]/2]
        
        shots.append([angle, shot_pos])

    # 4.2.5 Fire a shot   
    # iterate over all shots, giving each one a number
    for n, shot in enumerate(shots):
        speed = 10
        shot_vel = [math.cos(shot[0]) *speed, 
                    -math.sin(shot[0])*speed] # remember y direction is negative
        
        # Update fireball position
        shot[1][x] += shot_vel[x]
        shot[1][y] += shot_vel[y]
        
        # If the fireball leaves the screen, remove it from the list of shots
        shot_len = max(f_size[x],f_size[y])
        if (shot[1][x] > b_size[x] + shot_len or 
            shot[1][x] < - shot_len or 
            shot[1][y] > b_size[y] + shot_len or 
            shot[1][y] < - shot_len):
            shots.pop(n)
        
        # Monster hit, turn off monster
        if ((monster_pos[x]  <  shot[1][x]  <  monster_pos[x] + m_size[x])
            and 
            (monster_pos[y]  <  shot[1][y]  <  monster_pos[y] + m_size[y])):
            monster = False
        
        
    # 5. Draw
    #window.fill(blue)
    window.blit(background, [0, 0])
    window.blit(saucer_r, saucer_pos)
    
    if monster:
        window.blit(monster, monster_pos)
        
    for shot in shots:
        shot_r = pygame.transform.rotate(fire, math.degrees(shot[0]) - 90)
        window.blit(shot_r, shot[1])
        

    
    font = pygame.font.SysFont('helveticaneuedeskinterface', 40)   # font from list above  
    space_green = (0,250,154)
    text = font.render("Space Game!", True, space_green)
    window.blit(text, (250, 550))
        
        
        

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
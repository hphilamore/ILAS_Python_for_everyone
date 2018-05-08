#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""

import pygame 
import sys

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
win_width = 600
win_height = 400

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# circle variables
#x_pos = 100
#y_pos = 50
circ_vel = [5, 1]
circ_pos = [100, 50] 
radius = 20  

# rectangle variables
rect_vel = [2, 3]
rect_pos = [30, 30]  
width = 60
height = 80


position = [circ_pos, rect_pos]
velocity = [circ_vel, rect_vel]  
horizontal = [[radius, radius], [width, 0]]
vertical = [[radius, radius], [height, 0]]

# 3. Launch a game window
window = pygame.display.set_mode((win_width, win_height))

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
    # 
    
    # 5.1 Draw Shapes
    pygame.draw.circle(window, black, (circ_pos[0], circ_pos[1]), radius)
    #pygame.draw.rect(window, white, pygame.Rect(30, 300, 60, 80))
    pygame.draw.rect(window, white, pygame.Rect(rect_pos[0], rect_pos[1], width, height))

#
#    # 5.2 Reverse direction of travel if edge is reached
#    if circ_pos[0] > (win_width-radius) or circ_pos[0] < radius:
#        circ_vel[0] *= -1
#    if circ_pos[1] > (win_height-radius) or circ_pos[1] < radius:
#        circ_vel[1] *= -1
#        
#    if rect_pos[0] > (600-width) or rect_pos[0] < 0:
#        rect_vel[0] *= -1
#    if rect_pos[1] > (400-height) or rect_pos[1] < 0:
#        rect_vel[1] *= -1
#  
#    
#    # 5.3 Update circle position
##    x_pos += 1
##    y_pos += 1
#    circ_pos[0] += circ_vel[0]  
#    circ_pos[1] += circ_vel[1] 
#    
#    rect_pos[0] += rect_vel[0]  
#    rect_pos[1] += rect_vel[1] 
    
    for vel, pos, vert, horiz in zip(velocity, position, vertical, horizontal):
    
        # 5.2 Reverse direction of travel if edge is reached
        # 5.2.1 Environmental collision
        if pos[0] > (600-horiz[0]) or pos[0] < vert[1]:
            vel[0] *= -1
        if pos[1] > (400-vert[0]) or pos[1] < horiz[1]:
            vel[1] *= -1
            
            
        # 5.3 Update shape position
        pos[0] += vel[0]  
        pos[1] += vel[1] 
    
    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
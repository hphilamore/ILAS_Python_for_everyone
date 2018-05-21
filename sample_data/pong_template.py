#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""

import pygame 
import sys
import random

# 1. Initailise the pygame library
pygame.init()

# 2. Variables
x = 0
y = 1

# 2.1 colours 
black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# 2.2 window
win_width = 600
win_height = 400

# 2.3 ball
radius = 20 
ball_pos = [win_width//2, win_height//2] 
ball_vel = [random.randrange(2,4), random.randrange(1,3)]
if random.randrange(0,2) == 0:
    ball_vel[x] *= -1
if random.randrange(0,2) == 0:
    ball_vel[y] *= -1
       
# 2.4 paddles
pad_width = 30
pad_height = 120
pad1_vel = [0,0]
pad2_vel = [0,0]
pad1_pos = [0,                       win_height//2 - pad_height//2]
pad2_pos = [win_width - pad_width,   win_height//2 - pad_height//2] 


# 3. Launch a game window
window = pygame.display.set_mode((600, 400))


# 4. Set up the main game loop
while True:
    
    # 5. Event processing
    event = pygame.event.poll()
    
    # 5.1 Check if the user has quit the game
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
    
    # 6. Calculations

    # 6.1.3 Reverse direction of travel if edge is reached
    if ball_pos[x] > (win_width-radius) or ball_pos[x] < radius:
        ball_vel[x] *= -1
    if ball_pos[y] > (win_height-radius) or ball_pos[y] < radius:
        ball_vel[y] *= -1

        
    # 6.3 Update ball position
    ball_pos[x] += ball_vel[x]
    ball_pos[y] += ball_vel[y]
    

    # 7. Draw everything
    # 7.1 Draw Window
    window.fill(blue)
    
    
    # 7.2 Draw ball and paddles
    pygame.draw.circle(window, red, (int(ball_pos[x]), int(ball_pos[y])), radius)
    pygame.draw.rect(window, white, pygame.Rect(int(pad1_pos[x]), int(pad1_pos[y]), pad_width, pad_height))
    pygame.draw.rect(window, white, pygame.Rect(int(pad2_pos[x]), int(pad2_pos[y]), pad_width, pad_height))
    

    # 8. Update display
    pygame.display.update()
    
    
    # 9. Frame rate
    clock = pygame.time.Clock().tick(60)

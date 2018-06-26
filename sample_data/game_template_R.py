#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 09:02:36 2018

@author: hemma
"""
# 0. Import libraries
import pygame 
import sys
from test_funcs import *

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

background = pygame.image.load("../img/space.jpg")
b_size = pygame.Rect(background.get_rect()).size
saucer = pygame.image.load("../img/saucer.png")
s_size = pygame.Rect(saucer.get_rect()).size
monster = pygame.image.load("../img/saucer.png")
m_size = pygame.Rect(monster.get_rect()).size
fire = pygame.image.load("../img/saucer.png")
f_size = pygame.Rect(fire.get_rect()).size
objects = [pygame.image.load("../img/saucer.png"), pygame.image.load("../img/saucer.png")]
pos = [[0, 0], [50, 50]]


for i in range(len(objects)):
    objects[i] = pygame.transform.scale(objects[i], (120, 120))

obj_size = []
for o in objects:
    obj_size.append(pygame.Rect(o.get_rect()).size)
     
print(obj_size)




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
    window.blit(background, [0, 0])
        
    for o, p in zip(objects, pos):
        window.blit(o, p)

    # 6. Update display
    pygame.display.update()
    
    # 7. Frame rate
    clock = pygame.time.Clock().tick(60)
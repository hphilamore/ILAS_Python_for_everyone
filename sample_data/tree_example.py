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

#def tree():
#    "Draws a tree"
#    pygame.draw.rect(window, black, [160, 300, 30, 45])
#    pygame.draw.polygon(window, green, [[250, 300], [175, 150], [100, 300]])
#    pygame.draw.polygon(window, green, [[240, 250], [175, 130], [110, 250]])
    
def tree(x, y):
    "Draws a tree"
    pygame.draw.rect(window, black, [160+x, 300+y, 30, 45])
    pygame.draw.polygon(window, green, [[250+x, 300+y], [175+x, 150+y], [100+x, 300+y]])
    pygame.draw.polygon(window, green, [[240+x, 250+y], [175+x, 130+y], [110+x, 250+y]])


def draw_trees(trees):
    "Draws trees"
    
    for t in trees:
        
        x = t[0]
        y = t[1]
        
        pygame.draw.rect(window, black, [160+x, 300+y, 30, 45])
        pygame.draw.polygon(window, green, [[250+x, 300+y], [175+x, 150+y], [100+x, 300+y]])
        pygame.draw.polygon(window, green, [[240+x, 250+y], [175+x, 130+y], [110+x, 250+y]])


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
    
    # 5. Process events
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:        
        pygame.quit()
        sys.exit()  
        
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#        print("User pressed a mouse button")
        
    # 6. Draw
    window.fill(white)
#    pygame.draw.rect(window, black, [160, 300, 30, 45])
#    pygame.draw.polygon(window, green, [[250, 300], [175, 150], [100, 300]])
#    pygame.draw.polygon(window, green, [[240, 250], [175, 130], [110, 250]])

#    tree()
    
#    tree(0, 0)
#    tree(100, -100)
    
    trees = [[0, 0], [200, -150], [350, -150]]
    
#    for t in trees:
#        tree(t[0], t[1])
        
        
    draw_trees(trees)

    # 7. Update display
    pygame.display.update()
    
    # 8. Frame rate
    clock = pygame.time.Clock().tick(60)
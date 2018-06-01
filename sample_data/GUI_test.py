#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 00:43:34 2018

@author: hemma
"""
import tkinter as tk
from tkinter import *
import pygame
import os
import platform

black = (0,0,0)
white = (255, 255, 255)
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
def draw():
    pygame.draw.circle(screen, (0,0,0), (250,250), 125)
    pygame.display.update()
#    button1 = Button(buttonwin, text = 'Draw',  command=draw)
#    button1.pack(side=LEFT)
    #btn_end = Button(buttonwin, text='Close', command=exit)
    btn_tog = Button(buttonwin, text = 'Switch' , command=tog )
    #btn_end.pack(padx=150, pady=20)
    btn_tog.pack(padx = 150 , pady = 20 )
    print('hello')
    root.update()
    
def tog() :
    if root.cget( 'bg' ) == 'yellow' :
        root.configure( bg = 'gray' )
    else :
        root.configure( bg = 'yellow' )
    
root = tk.Tk()
root.title('Button Example')

embed = tk.Frame(root, width = 500, height = 500) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left

buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))
draw()
pygame.display.init()
pygame.display.update()


    
while True:
    draw()
    pygame.display.update()
    root.update() 
    clock = pygame.time.Clock().tick(1)
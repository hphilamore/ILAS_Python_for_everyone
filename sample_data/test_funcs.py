#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:22:01 2018

@author: hemma

"""

import pygame


def draw_circ(surf):
    
    pygame.draw.circle(surf, 
                       (255, 0, 0), 
                       (100, 100), 
                       40)
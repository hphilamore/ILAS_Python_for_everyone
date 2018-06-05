#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:50:31 2018

@author: hemma
"""
file = open("my_file.txt", "w" )


print( "File Name:",  file.name )

print( "Open Mode:",  file.mode )

print( "Readable:",  file.readable())

print( "Writable:",  file.writable())
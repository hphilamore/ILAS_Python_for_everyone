#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:31:33 2018

@author: hemma
"""
import numpy as np
a = np.loadtxt('sample_data/sample_data_seminar10.dat')

a = int(a[0][0])

a = 1 / a

print(a)
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:20:09 2017

@author: gyks
"""
import random

x0 = 50
y0 = 50

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    

x1 = 50
y1 = 50

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
distance = ((x1-x0)**2 + (y1-y0)**2)**0.5
print(x0,y0,x1,y1)
print(distance)
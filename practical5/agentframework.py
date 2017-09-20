# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:54:47 2017

@author: gyks
"""
import random

class Agent():
    
    def __init__(self):
        self.x = random.randint(0,100);
        self.y = random.randint(0,100)
        
    def move(self):
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99

        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99
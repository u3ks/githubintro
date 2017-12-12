# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:54:47 2017

A class file that holds the Agent class.

@author: gyks
"""
import random
import math

class Agent():
    
    def __init__(self, environment, agents, c, s):

        # initialize the agent at a random location
        self.x = random.randint(0,100);
        self.y = random.randint(0,100)
        self.store = 0

        # save the rest of the agent parameters
        self.environment = environment
        self.agents = agents
        self.color = c
        self.shape = s
        
    def move(self):
        
        # move the agent by to a random x and y location
        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99

        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99
            

    def eat(self):
        # if there is enough food in the enviroment each it
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
		

    def distance_with(self, other):
        # return the eucledian distance to the other agent
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    

    def share_with_neighbours(self, neighbourhood):
        # share half of the the food with any agent in the neighbourhood
        for agent in self.agents:
            if self.distance_with(agent) <= neighbourhood:
                shared_store = (self.store + agent.store) / 2
                self.store, agent.store = shared_store, shared_store
        
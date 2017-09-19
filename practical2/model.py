# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:20:09 2017

@author: gyks
"""
import random
import operator
import matplotlib.pyplot

# add first agent to random location
agents = []
agents.append([random.randint(0,100), random.randint(0,100)])

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# add second agent at random location 
agents.append([random.randint(0,100), random.randint(0,100)])

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
distance = ((agents[0][0]-agents[1][0])**2 + 
    (agents[0][1]-agents[1][1])**2)**0.5
    
print(agents[0],agents[1])
print(distance)
print(max(agents, key=operator.itemgetter(1)))


matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.scatter(agents[0][0],agents[0][1])
matplotlib.pyplot.scatter(agents[1][0],agents[1][1], color='red')
matplotlib.pyplot.show()
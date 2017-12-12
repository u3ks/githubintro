# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:54:47 2017

The script that reads in the environment and runs the model.

@author: gyks
"""
#import everything required
import matplotlib.pyplot
import agentframework
import csv
import random
from itertools import cycle

# setup the model parameters
num_of_agents = 10
num_of_iterations = 200
MIN_X ,MIN_Y = 0, 0
MAX_X, MAX_Y = 100, 100
neighbourhood = 10
DATAFILE = 'in.txt'
# cycle through the colors and shapes to create a unique combination
# of color and shape for up to 42 agents
cycol = cycle('bgrcmk')
cyshape = cycle('oD|ps2*')

environment = []
agents = []

# read in the data
with open(DATAFILE) as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		env_row = []
		for item in row:
			env_row.append(float(item))
		environment.append(env_row)
		
c = next(cycol)
s = next(cyshape)

# create each agent
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, c, s))
    c = next(cycol)
    if c == 'k':
        s = next(cyshape)

# plot initial frame
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.imshow(environment)

# simulate the agent based model
for n in range(num_of_iterations):
    # shuffle the agents and perform their actions
    random.shuffle(agents)
    for agent in agents:
	    agent.move()
	    agent.eat()
	    agent.share_with_neighbours(neighbourhood)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.imshow(environment)
	
    # plot the agents on the frame
    for a in agents:
        matplotlib.pyplot.plot(a.x, a.y, a.shape, markersize=a.store/100, color=a.color)
    # draw the frame
    matplotlib.pyplot.draw()
    matplotlib.pyplot.pause(0.001)
    # clear the frame
    matplotlib.pyplot.clf()

matplotlib.pyplot.imshow(environment)
for a in agents:
    matplotlib.pyplot.plot(a.x, a.y, a.shape, markersize=a.store/100, color=a.color)
matplotlib.pyplot.show()
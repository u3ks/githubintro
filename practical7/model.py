# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:20:09 2017

@author: gyks
"""
import matplotlib.pyplot
import agentframework
import csv
import copy
import random

num_of_agents = 10
num_of_iterations = 2
MIN_X ,MIN_Y = 0, 0
MAX_X, MAX_Y = 100, 100
neighbourhood = 20
DATAFILE = 'in.txt'

environment = []

with open(DATAFILE) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        env_row = []
        for item in row:
            env_row.append(float(item))
        environment.append(env_row)

old_env = copy.deepcopy(environment)
        
# add agents to random location
agents = []

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

for n in range(num_of_iterations):
    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share_with_neighbours(neighbourhood)


matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


for agent in agents:
    print(agent.store)

assert old_env != environment
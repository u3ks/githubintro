# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:20:09 2017

@author: gyks
"""
import matplotlib.pyplot
import math
import pprint
import agentframework
import csv

num_of_agents = 10
num_of_iterations = 2
MIN_X ,MIN_Y = 0, 0
MAX_X, MAX_Y = 100, 100
DATAFILE = 'in.txt'

def distance(agent1, agent2):
    return math.sqrt((agent1.x - agent2.x)**2 + (agent1.y - agent2.y)**2)
    

environment = []

with open(DATAFILE) as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        env_row = []
        for item in row:
            env_row.append(float(item))
        environment.append(env_row)
        
#pprint.pprint(environment)
#        
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

# add agents to random location
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

for agent in agents:
    for n in range(num_of_iterations):
        agent.move()
        agent.eat()


matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#for agent in agents:
#    assert (0 <= agent.x <= 99) and (0 <= agent.y <= 99)
#    
#agent_distances = [[0 for i in range(len(agents))] for i in range(len(agents))]
#
#for i, agent1 in enumerate(agents):
#    for j in range(i + 1, len(agents)):
#        dist = distance(agent1, agents[j])
#        agent_distances[i][j] = dist
#        agent_distances[j][i] = dist
#
#pprint.pprint(agent_distances)
#
#matplotlib.pyplot.xlim(MIN_X, MAX_X)
#matplotlib.pyplot.ylim(MIN_Y, MAX_Y)
#agents.sort(key=lambda agnt: agnt.y, reverse=True)
#
##plot the northern_most_point red
#matplotlib.pyplot.scatter(agents[0].x,agents[0].y, color='red')
#
##plot the other points in blue
#for agent in agents[1:]:
#    matplotlib.pyplot.scatter(agent.x,agent.y, color='blue')
#
#matplotlib.pyplot.show()
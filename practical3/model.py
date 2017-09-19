# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:20:09 2017

@author: gyks
"""
import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 2
MIN_X ,MIN_Y = 0, 0
MAX_X, MAX_Y = 100, 100

# add agents to random location
agents = []
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])


for i in range(len(agents)):
    for n in range(num_of_iterations):
        for c in range(len(agents[i])):
            if random.random() < 0.5:
                agents[i][c] = (agents[i][c] + 1) % 100
            else:
                agents[i][c] = (agents[i][c] - 1) % 100


print(max(agents, key=operator.itemgetter(1)))

for agent in agents:
    assert (0 <= agent[0] <= 100) and (0 <= agent[1] <= 100)

matplotlib.pyplot.xlim(MIN_X, MAX_X)
matplotlib.pyplot.ylim(MIN_Y, MAX_Y)
agents.sort(key=operator.itemgetter(1), reverse=True)

#plot the northern_most_point red
matplotlib.pyplot.scatter(agents[0][0],agents[0][1], color='red')

#plot the other points in blue
for i in range(1, len(agents)):
    matplotlib.pyplot.scatter(agents[i][0],agents[i][1], color='blue')

matplotlib.pyplot.show()
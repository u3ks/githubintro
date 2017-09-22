import matplotlib.pyplot
import agentframework
import csv
import random
from itertools import cycle

matplotlib.pyplot.ion()
num_of_agents = 10
num_of_iterations = 400
MIN_X ,MIN_Y = 0, 0
MAX_X, MAX_Y = 100, 100
neighbourhood = 20
DATAFILE = 'in.txt'
cycol = cycle('bgrcmk')
cyshape = cycle('oD|ps2*')


environment = []
agents = []

with open(DATAFILE) as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for row in data:
		env_row = []
		for item in row:
			env_row.append(float(item))
		environment.append(env_row)
		
c = next(cycol)
s = next(cyshape)

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, c, s))
    c = next(cycol)
    if c == 'k':
        s = next(cyshape)

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.imshow(environment)

for n in range(num_of_iterations):
    random.shuffle(agents)
    for agent in agents:
	    agent.move()
	    agent.eat()
	    agent.share_with_neighbours(neighbourhood)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.imshow(environment)
	
    for a in agents:
        matplotlib.pyplot.plot(a.x, a.y, a.shape, markersize=a.store/100, color=a.color)
    matplotlib.pyplot.draw()
    matplotlib.pyplot.pause(0.001)
    matplotlib.pyplot.clf()
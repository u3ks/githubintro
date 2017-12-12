"""
Example that captures how the mapper works on more complicated datasets.
"""

import matplotlib.pyplot as plt
import sys
import numpy as np
import networkx as nx
from base_mapper import mapper, leftmost_filter
from slic import build_pairwise_distance_heap, slic

# read in the data
smooth_circle = np.load('data/smoothcircle.npy')

# show what the original dataset looks like
plt.scatter(smooth_circle[::, 0], smooth_circle[::, 1])
plt.show()

# calculate the topological shape of the data
G = mapper(smooth_circle, build_pairwise_distance_heap,
                  leftmost_filter, slic, 5, 0.2)

# # save the resulting image to the examples folder
nx.draw(G, with_labels=True)
plt.savefig('fig1.png')
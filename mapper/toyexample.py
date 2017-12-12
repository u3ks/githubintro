"""
Example that shows what the mapper captures, when ran on a toy dataset.

"""
import matplotlib.pyplot as plt
import sys
import numpy as np
import networkx as nx
from base_mapper import mapper, filter_data
from slic import build_pairwise_distance_heap, slic

toy_data = np.array([[ 2.26641764,  4.71195453],
       [ 4.85456134,  4.15984003],
       [-0.77747422,  6.15894165],
       [ 3.34855548, -6.63030249],
       [ 5.5413445 ,  5.36414154],
       [ 8.50234728, -3.38120701],
       [-0.79011924,  6.23190392],
       [ 6.46312364, -7.20641922],
       [-9.44442878,  6.06682957],
       [ 3.4522224 ,  4.88034308]])

fig, ax = plt.subplots()
ax.scatter(toy_data[::, 0], toy_data[::, 1])

for i in range(len(toy_data)):
    ax.annotate(i, (toy_data[i, 0], toy_data[i, 1]))
plt.show()

G = mapper(toy_data, build_pairwise_distance_heap,
                  filter_data, slic, 7, 0.2)

nx.draw(G, with_labels=True)
plt.show()
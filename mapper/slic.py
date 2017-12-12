# implementation of clustering algorithm described in mapper paper
# Single-LInkage Clustering with interval termination

import numpy as np
import heapq


error = 0.09

# check whether two floats are within the same range
def eqs(x, y, err):
    return abs(y-x) <= err


# helper class for the heap function
class Edge:
    
    def __init__(self, point1, point2, distance):
        self.A = point1
        self.B = point2
        self.distance = distance
        
    def __lt__(self,that):
        return self.distance < that.distance
    
    def __eq__(self,that):
        return self.distance == that.distance
    
    def __gt__(self,that):
        return self.distance > that.distance
    
# function that calculates the euclidean distance between two points
def eucledian_distance(x, y):
    return np.sqrt(np.sum(np.power(x-y, 2)))


# helper function for the union find data structure
# it returns the parent of each element
def parent(parents, i):
    
    while parents[i] != i:
        i = parents[i]
        
    return i


# histogram cutoff function that determines the step at which clustering terminates
# it takes as input the length of all edges needed to fully connect the dataset and 
# the number of bins for the histogram.
def get_last_merge(values, num_intervals):
    
    max_edge = max(values)
    min_edge = min(values)
    
    # the distance between all points is practivally the same
    # cluster until the end
    if eqs(max_edge, min_edge, error):
        return len(values) - 1
    
    # otherwise create a histogram and place all values in it
    int_length = (max_edge - min_edge) / num_intervals
    bins = []
    for i in range(num_intervals):
        s = min_edge + (i)*int_length
        bins.append(s)
    bins.append(max_edge + 1)
    placements = np.digitize(values, bins)
    
    # if there is an empty space that is where the clustering terminates
    for i, b in enumerate(placements[:-1]):
        if placements[i + 1] > b + 1:
            break
    else:
        i = len(placements) - 1
            
    return i

# helper function that sorts the datapoints based on the eucledian distance between them
def build_pairwise_distance_heap(data):
    
    h = []
    l = len(data)
    for i in range(l):
        for j in range(i+1, l):
            dist = eucledian_distance(data[i,], data[j,])
            heapq.heappush(h, Edge(i,j,dist))
    return h

# a function that calculates the number of connections needed and their length,
# in order to completely connect the dataset
def get_linkage(data, heap_func):
    
    edges = []
    parents = [x for x in range(len(data))]
    
    # create all possible pairwise distances between points and
    # sort them in increasing order
    h = heap_func(data)
    
    num_clusters = len(parents)

    # using the union find datastructure completely connect the dataset
    while num_clusters > 1:
        dist = heapq.heappop(h)
        x, y = parent(parents, dist.A), parent(parents, dist.B)
        if x != y:
            parents[x] = y
            num_clusters -= 1
            edges.append(dist)
            
    return edges


# a function that finds the number of clusters and to which cluster a point belongs
# based on the number of available connections
def find_clusters(num_data_points, edges):
    
    clusters, parents = [], []
    for x in range(num_data_points):
        parents.append(x)
        clusters.append(x)
        
    for e in edges:
        x, y = parent(parents, e.A), parent(parents, e.B)
        parents[x] = y
    
    for i, c in enumerate(clusters):
        clusters[i] = parent(parents, c)
    
    return clusters

# cluster the dataset using the Single-LInkage Clustering with interval termination
def slic(data, heap_func, num_intervals):
    
    if len(data) == 0:
        return []
    if len(data) == 1:
        return [0]
    
    edges = get_linkage(data, heap_func)
    edge_lengths = [e.distance for e in edges]
    # get the cutoff point
    last_merge = get_last_merge(edge_lengths, num_intervals)
    edges = edges[:last_merge + 1]
    # cluster until that point
    clusters = find_clusters(len(data), edges)
    return clusters
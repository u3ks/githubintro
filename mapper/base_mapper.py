import operator
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from collections import defaultdict

# filter function that returns the first dimension of the dataset
# for example, if the data is x,y coordinate based, this will return the x coordinates
def filter_data(data):
    return data[::, 0]


# filter function that returns the eucledian distance between each element
# and the leftmost element in the dataset
def leftmost_filter(data):
    # first find the leftmost element
    leftmost_index, _ = min(enumerate(data[::, 0]), key=operator.itemgetter(1))
    # calculate the distance from it for each element
    return np.sqrt(np.sum(np.power(data - data[leftmost_index], 2), axis=1))


# split a range into intervals with a percent overlap
# for example if the range is (0,2) and it should be split into 4
# intervals with a 66% overlap, the output would be
# (0,1), (0.333, 1.33), (0.66, 1.66), (1,2)
def create_intervals(filter_range, num_intervals, percent_overlap):
    
    intervals = []
    s,e = filter_range
    j = s
    
    # calculate the length of each interval
    interval_length = abs(e-s) / (num_intervals - (num_intervals - 1) * percent_overlap)
    
    interval_length = interval_length
    # calculate each step
    step = interval_length * (1 - percent_overlap)
    
    # start from the minimal interval value
    # and create interval at each step
    for i in range(num_intervals):
        j = s + (i) * step
        intervals.append([j, j + interval_length])

    # account for rounding errors
    intervals[len(intervals)-1][1] = e
    
    return intervals


# a helper function that records in which intervals a data point lies
def in_range(i, preimages, intervals, filter_vals):
    for j, interval in enumerate(intervals):
        if interval[0] <= filter_vals[i] <= interval[1]:
            preimages[j].append(i)


# split the dataset into subsets based on the filter function
# cluster the points in each intervals
# and return which data points lie in which clusters       
def get_nodesets(data, heap_func, filter_func, clustering, 
           num_intervals, percent_overlap):
    
    filter_vals = filter_func(data)
    fmin = min(filter_vals)
    fmax = max(filter_vals)
    intervals = create_intervals((fmin, fmax), num_intervals, percent_overlap)
    # for each interval create an array that holds the point indecies 
    # that fall within that interval
    preimages = {x:[] for x in range(len(intervals))}
    
    # for each data point, record in which intervals it lies
    for i in range(len(data)):
        in_range(i, preimages, intervals, filter_vals)
    
    nodesets = []
    
    for i, x in enumerate(preimages):
        # cluster the points in each interval
        clusters = clustering(data[preimages[x]], heap_func, num_intervals)
        
        # record which datapoints lie in which clusters
        clusters_dict = defaultdict(set)
        for j, n in enumerate(clusters):
            clusters_dict[str(i)+str(n)].add(preimages[x][j])
        nodesets.append(clusters_dict)
    
    return nodesets

# create a graph from the dataset, based on the specified 
# clustering function, filter function, ranking function,
# number of intervals and their overlap
def mapper(data, heap_func, filter_func, clustering, 
           num_intervals, percent_overlap):
    
    # get the clusters and the points that lie in each cluster
    nodesets = get_nodesets(data, heap_func, filter_func, clustering, 
               num_intervals, percent_overlap)

    G=nx.Graph()

    # for each cluster
    for i, nodeset in enumerate(nodesets):
        for node in nodeset:
            # create a vertex
            G.add_node(node)
            for nodeset2 in nodesets[i+1:]:
                for node2 in nodeset2:
                    # if two clusters share points create an edge
                    if len(nodeset[node].intersection(nodeset2[node2])) > 0:
                        G.add_edge(node, node2)
                        
    return G
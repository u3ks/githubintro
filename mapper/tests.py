"""
Test methods for all the implemented functions.

"""

import numpy as np
from base_mapper import *
from slic import *


def test_parent():
    example1 = [0, 1, 2]
    expected1 = 1
    
    example2 = [0, 0, 2]
    expected2 = 0
    
    assert parent(example1, 1) == expected1
    assert parent(example2, 1) == expected2
    

def test_get_last_merge():
    
    values1 = [1, 2, 5, 6, 6]
    num_intervals1 = 5
    assert get_last_merge(values1, num_intervals1) == 1
    
    values1 = [1, 2, 3, 4, 5]
    num_intervals1 = 4
    assert get_last_merge(values1, num_intervals1) == 4
    
    values2 = [0.074, 1.195, 1.386, 1.576, 3.167, 3.370, 4.334, 8.376, 8.655]
    num_intervals2 = 10
    assert get_last_merge(values2, num_intervals2) == 3
    

def test_build_pairwise_distance_heap():
    
    example = np.array([[ 1.0,  1.0],
                       [2.0,  2.0],
                       [3.0,  3.0]])
    expected = [Edge(0, 1, 1.414214),
                Edge(1, 2, 1.414214),
                Edge(0, 2, 2.828427)]
    i = 0
    h = build_pairwise_distance_heap(example)
    for i in range(len(expected)):
        r = heapq.heappop(h)
        e = expected[i]
        assert e.A == r.A
        assert e.B == r.B
        assert eqs(e.distance, r.distance, error)
        

def test_get_linkage():
    
    example = np.array([[ 1.0,  1.0],
                       [2.0,  2.0],
                       [3.0,  3.0]])
    
    expected = [Edge(0, 1, 1.414214),
                Edge(1, 2, 1.414214)]
    
    returned = get_linkage(example, build_pairwise_distance_heap)
    for i in range(len(expected)):
        r = returned[i]
        e = expected[i]
        assert e.A == r.A
        assert e.B == r.B
        assert eqs(e.distance, r.distance, error)
        
def test_find_clusters():
    
    example = [Edge(0, 1, 1.414214),
                Edge(1, 2, 1.414214)]
    
    expected = [2, 2, 2]
    
    returned = find_clusters(3, example)
    assert expected == returned


def test_create_intervals(expected, returned):
    for x,y in zip(expected, returned):
        assert eqs(x[0], y[0], error)
        assert eqs(x[1], y[1], error)


def test_leftmost_filter():
    example = np.array([[ 2.0,  2.0],
                    [ 1.0,  1.0],
                    [ 3.0,  3.0]])
    expected =  np.array([1.414214, 0, 2.828427])
    returned = leftmost_filter(example)

    for i, ex in enumerate(returned):
        assert eqs(expected[i], ex, error)    

def test_eq():
    assert eqs(eucledian_distance(np.array([1,2,3]), np.array([4,5,6])), 5.1961, error)

if __name__ == '__main__': 
    expected1 = [(0,1), (0.333, 1.33), (0.66, 1.66), (1,2)]
    returned1 = create_intervals((0,2), 4, 2/3)

    expected2 = [(0,1), (0.8, 1.8), (1.6, 2.6), (2.4, 3.4), (3.2, 4.2)]
    returned2 = create_intervals((0,4.2), 5, 0.2)
    test_create_intervals(expected1, returned1)
    test_create_intervals(expected2, returned2)

    test_eq()
    test_leftmost_filter()
    test_parent()
    test_get_last_merge()
    test_build_pairwise_distance_heap()
    test_get_linkage()
    test_find_clusters()
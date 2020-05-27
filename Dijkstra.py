"""
The path with length D [k] = Min {D [i] | vi in V} is the shortest path from v0 (v0, vi). The next shortest path with the next shortest length (v0 to vj) is either directly an arc (v0, vj), the length is the weight on the arc, or (v0, vk, vj), and the length is D [k] (vk, vj) Weights on the arc.
"""
from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
     #directed graph edges, source points, target points
    g = defaultdict(list)  # construct adjacency matrix 
    for l,r,c in edges:
        g[l].append((c,r))
#     {'A': [(7, 'B'), (5, 'D')], 
#      'B': [(8, 'C'), (9, 'D'), (7, 'E')], 
#      'C': [(5, 'E')], 
#      'D': [(15, 'E'), (6, 'F')], 
#      'E': [(8, 'F'), (9, 'G')], 
#      'F': [(11, 'G')]})
    
    q = [(0, f, ())]  # (The shortest distance from the source point to the current point, the current point, the corresponding path)
    seen = set()   # Set S, the set of vertices that have found the shortest path 
    mins = {}  # Source point to each of T The shortest path length of the vertex, auxiliary vector D 
    while q:
        cost, vk, path = heappop(q)  # the shortest distance cost from the source point to the vertex in the current T, the corresponding vertex is vk
        if vk not in seen:  # Make sure that vk is not in 
            seen.add(vk)  # Add vk to S, that is, exit T
            path = (vk, path)  # Record the path from the source point to vk
            if vk == t:  # If vk is the target point, just return directly, that is the shortest distance and the corresponding path 
                return (cost, path)

            # If vk is not the target point, check whether vk can reach other vertices 
            for c, vj in g.get(vk, ()):  # vk is returned when the degree is 0 ()
                if vj not in seen:  # Only need to check all the vertices that vk can reach are vj 
                    prev = mins.get(vj, None)  # D[j], The shortest path from the source point to vj, if it does not exist, return None
                    next_ = cost + c  # D[vk] + (vk, vj) arc length h
                    if prev is None or next_ < prev:  # If the path is v0 -...- vk -vj weight is smaller than path v0-vj 
                        mins[vj] = next_  # update source point to the shortest distance in T
                        heappush(q, (next_, vj, path))  # add heap 
    return float("inf")

# test
edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]

print("=== Dijkstra ===")
print(edges)
print("A -> E:")
print(dijkstra(edges, "A", "E"))
print("F -> G:")
print(dijkstra(edges, "F", "G"))

"""
Result:
=== Dijkstra ===
[('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)]
A -> E:
(14, ('E', ('B', ('A', ()))))
F -> G:
(11, ('G', ('F', ())))
"""

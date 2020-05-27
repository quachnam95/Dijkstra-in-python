from collections import defaultdict 
from heapq import * 

def dijkstra (edges, f, t): 
    #directed graph edges, source points, target points
    g = defaultdict (list) # construct adjacency matrix 
    for l, r, c in edges: 
        g [l] .append ((c, r)) 
# {'A': [(7, 'B'), (5, 'D')], 
# 'B': [(8, 'C'), (9, 'D'), (7, 'E')], 
# 'C': [(5, 'E')], 
# 'D': [(15, 'E') , (6, 'F')], 
# 'E': [(8, 'F'), (9, 'G')], 
# 'F': [(11, 'G')]}) 
    
    q = [(0, f,())] # (The shortest distance from the source point to the current point, the current point, the corresponding path) 
    seen = set () # Set S, the set of vertices that have found the shortest path 
    mins = {} # Source point to each of T The shortest path length of the vertex, auxiliary vector D 
    while q: 
        cost, vk, path = heappop (q) # the shortest distance cost from the source point to the vertex in the current T, the corresponding vertex is v1
        if v1 not in seen: # Make sure that v1 is not in 
            seen.add (v1) # Add v1 to S, that is, exit T 
            path = (v1, path) # Record the path from the source point to v1 
            if v1 == t: # If v1 is the target point, just return directly, that is the shortest distance and the corresponding path 
                return (cost, path) 

            # If vk is not the target point, check whether vk can reach other vertices 
            for c, v2 in g.get (v1, ( )): # v1 is returned when the degree is 0 () 
                if v2 not in seen: # Only need to check all the vertices that vk can reach are v2 
                    prev = mins.get (v2, None) # D [2], The shortest path from the source point to v2, if it does not exist, return None 
                    next_ = cost + c # D [v1] + (v1, v2) arc length 
                    if prev is None or next_ <prev: # If the path is v0 -...- v1 -v2 weight is smaller than path v0-v2 
                        mins [v2] ​​= next_ # update source point to the shortest distance in T
                        heappush (q, (next_, v2, path)) # add heap 

    return float ("inf") 

# test 
edges = [ 
    ("A", "B", 7), 
    ("A", "D", 5) , 
    ("B", "C", 8), 
    ("B", "D", 9), 
    ("B", "E", 7), 
    ("C", "E", 5), 
    ( "D", "E", 15), 
    ("D", "F", 6), 
    ("E", "F", 8), 
    ("E", "G", 9), 
    ("F "," G ", 11) 
] 

print (" === Dijkstra === ") 
print (edges) 
print (" A-> E: ") 
print (dijkstra (edges, "A", "E")) 
print ("F-> G:") 
print (dijkstra (edges, "F", "G"))

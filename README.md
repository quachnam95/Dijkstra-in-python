# Dijkstra-in-python
The shortest path - dijkstra algorithm: a single-source shortest path problem for non-negative weight directed graphs. 
1. Set a set of two vertices T and S, an auxiliary vector D. S is the set of vertices that have found the shortest path. Initially, there is only one vertex in the set S, that is, the source point v0; T is the set of vertices that have not yet found the shortest path; each component of D D [i] represents the current The shortest path length (weight) found from the source point v0 to vi. Initially, if v0 to vi has an arc, D [i] is the weight on the arc, otherwise it is ∞.
2. Traverse through the set T to find the shortest path (v0, ..., vk) with the shortest current length, thus adding vk to the vertex set S. Then check whether the newly added vertex can reach other vertices, and check whether the path length through the vertex to other points is shorter than that from V0 to other points directly. If yes, modify the shortest path length of each vertex in the source point v0 to T. 
3. Repeat 2 until all vertices are added to the set S.

Example: The path with length D [k] = Min {D [i] | vi in V} is the shortest path from v0 (v0, vi). The next shortest path with the next shortest length (v0 to vj) is either directly an arc (v0, vj), the length is the weight on the arc, or (v0, vk, vj), and the length is D [k] (vk, vj) Weights on the arc.

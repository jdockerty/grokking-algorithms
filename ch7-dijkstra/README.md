# Dijkstra

In [chatper 6](../ch6-breadth-first/README.md), we learnt how we could get the *shortest path*, using BFS. This isn't necessarily the fastest path, but the one with the least number of *segments* - a segment is the edge that is bounded by nodes, this creates a valid sub-graph too.

Let us now suppose that we add a travel time to the edges in our fictional graph, we would want the fastest time for a travel route etc. If we use BFS, we will get the path with the fewest segments, but not necessary the fastest path based on the weighted edges.

**Finding the fastest/shortest path in a weighted graph can be solved using Dijkstra's algorithm.**

The algorithm can be followed as such:

* Find the *cheapest* node, the node you can reach in the least amount of time from your starting point.
* Update the costs of the neighbours of this node.
* Repeat until you've done the above steps for every node in the graph.
* Calculate final path.

In the graph below, the weighted edges represent the time in minutes to travel from one node to the next, e.g. X --> A takes 6 minutes.

Using our first step, we take the cheapest distance from the starting position (X). Going to Node B is the cheapest, we're comparing 2 < 6 here - we don't know of the other nodes edges yet, so technically we'd count getting to the finish (Node Y) as infinity.

Next we calculate how long it takes to get to all of Node B's neighbours, following an edge from Node B. This would be going to Node A, it takes 3 minutes, even though the finish node would be 5, we go for the lowest edge. From here, we could update our list to know we can get to Node A in 5 minutes, not 6 as you would first believe by going direct.

Our current updated list would be:

* From the start to Node A - 5 minutes (Start --> B --> A)
* From start to finish, currently we can get there in 7 (Start --> B --> Finish)

We repeat the above steps for each node in the graph.

[step_1](images/step_1.png)

## Terminology and Facts

* When edges have an associated number, typically representing a time or value between the nodes, this is the *weight* of the edge.
* Calculating the shortest path in an *unweighted graph*, use BFS. With a *weighted graph* use Dijkstra.
* Graphs can have a *cycles*, meaning you can start at one node and travel back around to it again without going along the same edge you did to leave.
* An *undirected graph* graph is cyclical, since both nodes are pointing to each other. This means each edge adds another cycle.
* **Dijkstra's algorithm only works with directed acyclic graphs (DAGs)**
* **Dijkstra's algorithm cannot be used on negative weighted graphs either. Use Bellman-Ford instead**

### Implementation

The graph we're using is the one in the picture above.

We can use hash tables again to show the relationship of the nodes and their weights.

Code available in [dijkstra.py](./dijkstra.py)
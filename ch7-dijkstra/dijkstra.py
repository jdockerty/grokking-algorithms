graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {} 
graph["a"]["finish"] = 1 
graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["finish"] = 5 
graph["finish"] = {} # no neighbours at the finish node

# We also need a hash table to store the cost of each node as we go along. We can populate the beginning of our algorithm, since we start on the 'start' node.
infinity = float("inf") # use inf rather than 0, since we compare, shown later
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity

# We also need another hash table for storing the parent nodes
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["finish"] = None

# Keep an array for the nodes we have processed.
processed = []

def find_lowest_cost_node(costs):
   lowest_cost = float("inf")
   lowest_cost_node = None
   for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
        lowest_cost = cost
        lowest_cost_node = node
    
    return lowest_cost_node

node = find_lowest_cost_node(costs) # lowest node we haven't processed
while node is not None: # stop loop once all processed
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys(): # check all neighbours of current node
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost: # if cheaper for new_cost, update it. This is also why we use infinity in our initial unknown path weight
            costs[n] = new_cost
            parents[n] = node 
    processed.append(node) # mark node as processed
    node = find_lowest_cost_node(costs) # find next node to process and continue loop

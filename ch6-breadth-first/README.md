# Breadth First Search (BFS)


- [Breadth First Search (BFS)](#breadth-first-search-bfs)
  - [What is a Graph?](#what-is-a-graph)
  - [Breadth-First Search (BFS)](#breadth-first-search-bfs-1)
  - [Implementing the Graph](#implementing-the-graph)
  - [Implementing the algorithm](#implementing-the-algorithm)
  - [Running Time](#running-time)
- [Recap](#recap)

This chapter introduces a new data structure, a *graph*.

BFS allows you to find the shortest distance between two things, but this distance could mean a lot of things depending on what the graph data structure is representing:

* A checkers AI to calculate the fewest moves to victory
* A spell checker, fewest edits from mispelling to a real word. E.g. `READED` to `READER` is one edit.
* Find the doctor closest to you in your network.


**Graph algorithms are some of the most useful algorithms. If you understand them, you'll be able to apply them a lot.**

## What is a Graph?

A graph models a set of connection, it can be a relationship between the different items such as distance between cities, family relations between people etc.

Each graph is made up of *nodes* and *edges*. A node can be directly connected to other nodes, these are known as *neighbours*. Here Jim and Bob are neighbours, if there was another node behind Bob, this would be Bob's neighbour, but not Jim's.

[nodes and edges](images/nodes_edges.png)

## Breadth-First Search (BFS)

In [chapter 1](../ch1-introduction-to-algorithms/README.md), we looked at binary search. BFS is a different kind of search algorithm, it runs on graphs.

BFS can help us answer two types of questions:

* Is there a path from node A to node B?
* What is the shortest path from node A to node B?


## Implementing the Graph

A graph consists of several nodes, each node is connected to neighbouring nodes. We know a data structure which allows us to represent relationships in data, a [hash table!](../ch5-hash-tables/README.md)

Since we are mapping a key to a value, in the case of a graph we want to map a key (the node) to a value (all of the node's neighbours).

```python
graph = {}
graph["me"] = ["alice", "bob"]
```

A bigger graph would look something like this

```python
graph = {} 
graph[“you”] = [“alice”, “bob”, “claire”] 
graph[“bob”] = [“anuj”, “peggy”] 
graph[“alice”] = [“peggy”] 
graph[“claire”] = [“thom”, “jonny”] 
graph[“anuj”] = [] 
graph[“peggy”] = [] 
graph[“thom”] = [] 
graph[“jonny”] = []
```

Notice here, how Anuj, Peggy, Thom, and Jonny have no neighbours, but they do have other nodes which point to them. This is known as a *directed graph*, since relationships can be one-way - meaning Bob is Anuj's neighbour, but Anuj isn't Bob's. This is represented with pointed arrows to show the direction of relationships.

An *undirected graph* does not have arrows which show the direction of the relationship, and thus the neighbour relationship. In this case, both nodes would be each other neighbour.

## Implementing the algorithm

We will use a queue structure too here, this lets us keep a *queue* of people to check through in our search algorithm.

We have use a double-ended queue, known as a *deque*. We can use a function for this in Python to make the implemtnation simpler.

```python
from collections import deque
search_queue = deque() # create a new queue
search_queue += graph["you"] # adds all of my neighbours to the queue, from earlier this is [alice, bob, claire]

# keep a checklist of those who have been checked to avoid infinite loops/unecessary work if you people share mutual friends, 
# as they would be added to the queue multiple times and checked again otherwise.
searched = [] 

def person_is_seller(name):
    """
    Our silly way to check whether someone is a mango seller in the network, does their name start with the letter 'm'.
    """
    return name[-1] == 'm'

while search_queue: # while the queue is not empty
    person = search_queue.popleft() # grab first person from the queue
    
    if person not in searched:
        if person_is_seller(person): # is the person a mango seller?
            print("{} is a mango seller!".format(person))
            return True
        else:
            search_queue += graph[person] # add all of the persons network to the queue to check later

return False # if we get here, nobody is a mango seller in the whole network
```


## Running Time

If you search the entire network for a mango seller, you follow each edge. This means our running time will be at least O(num edges). We also keep a queue of people to search, adding a person takes constant time, O(1), for every person means it takes O(num people). 

BFS takes O(num people + num edges), this is more commonly written as **O(V + E)**. V = vertices, E = edges

# Recap

* BFS tells us whether there is a path from A to B.
* If there is a path, BFS will show us the shortest path.
* If you have a problem like "find shortest X", try modelling it as a graph and using BFS to solve it.
* Directed graphs have arrows, relationships will follow the direction of the arrow.
* Undirected graphs don't have arrows, implicitly, the relationship goes both ways.
* Queues are First In, First Out (FIFO).
* Stacks are Last In, First Out (LIFO).
* With BFS, you need to check in the order that people were added to the queue, otherwise you won't get the shorted path.
* Make sure we don't check things again with BFS, we can get an infinite loop otherwise.
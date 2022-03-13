# Exercises


**8.1**

    You work for a furniture company, and you have to ship furniture all over the country. You need to pack your truck with boxes. 
    
    All the boxes are of different sizes, and you’re trying to maximize the space you use in each truck. How would you pick boxes to maximize space? 
    
    Come up with a greedy strategy. Will that give you the optimal solution?

We could do this in a similar way to fitting items in a sack, we place the largest box in first, then the next largest box which will fit after that. This won't be the most optimal solution, but would be good enough.

**8.2**

    You’re going to Europe, and you have seven days to see everything you can. You assign a point value to each item (how much you want to see it) and estimate how long it takes. 

    How can you maximize the point total (seeing all the things you really want to see) during your stay? 
    
    Come up with a greedy strategy. Will that give you the optimal solution?

We can go to the highest rated thing first, then the 2nd highest etc. Moving down the sorted list of things/places to visit. Similar to above, this won't be the most optimal solution, but would be pretty good.

**8.3**
*For each of the algorithms, are they greedy or not?*

    Quicksort

No

**8.4**
    Breadth-first search
No <-- incorrect, the answer is **Yes**.

**8.5**

    Dijkstra
Yes

**8.6**

    A postman needs to deliver to 20 homes. He needs to find the shortest route that goes to all 20 homes. Is this an NP-complete problem?


Yes, this is the travelling salesman problem. You need to know the shortest route between all 20 homes, before being able to pick the shortest route that visits all of them.


**8.7**

    Finding the largest clique in a set of people (a clique is a set of people who all know each other). Is this an NP-complete problem?

Yes, you would need to know who everybody knows within the entire set of people, before being able to find the largest clique.

**8.8**

    You’re making a map of the USA, and you need to color adjacent states with different colors. You have to find the minimum number of colors you need so that no two adjacent states are the same color. Is this an NP-complete problem?

Yes
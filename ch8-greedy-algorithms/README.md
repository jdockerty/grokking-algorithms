# Greedy Algorithms

- [Greedy Algorithms](#greedy-algorithms)
  - [Classroom Scheduling Problem](#classroom-scheduling-problem)
  - [Knapsack Problem](#knapsack-problem)
  - [Set-Covering Problem](#set-covering-problem)

These are part of a class of algorithms used to solve problems that have no fast algorithmic solution, known as NP-complete problems.

## Classroom Scheduling Problem

Suppose that you have a classroom and you wish to hold as many classes at possible in it. You get a list of classes that need to take place.

It is not possible to do all classes, since there will be conflicts. E.g. Art may be scheduled at 9:30am, lasting for an hour, where Science is scheduled for 9:45am, scheduled for 2 hours. These would overlap and cannot be conducted in the same room.

How would you schedule which classes to arrange, so you get the biggest set of classes possible?

The problem sounds difficult, but the algorithm for it can be quite simple.

* Pick the class which starts the earliest, this will be the first class.
* The next class will be the one which starts soon after the first one.
* Repeat.

This is the beauty of a greedy algorithm, it is very simple. Each step, you pick an optimal move. In technical terms, you pick the *locally optimal solution at each step.*


## Knapsack Problem

Suppose you are a greedy thief, there are many items in a store which we can steal, but we cannot take everything. We can only take what fits in our knapsack, it can hold 35 lb of items. We are trying to maximise the amount of items we put into the sack.

What is our algorithm? The greedy algorithm is very simple:

* Pick the most expensive thing which will fit.
* Pick the next most expensive thing that will fit.
* Repeat.

However, this won't work exactly we would expect this time. Suppose there are 3 items: 

* Stereo - £3000, 30lb.
* Laptop - £2000, 20lb.
* Guitar - £1500, 15lb.

Using this algorithm, we'd only get the stereo, for £3000 and 5lb remaining. But the optimal solution would be the laptop AND guitar, for £3500 with no wasted space in the sack.

Here, the greedy strategy doesn't give you an optimal solution, but it does get us quite close. This is *good enough*, as we do not care about perfect with greedy algorithms.

**Sometimes, perfect is the enemy of good. At times, all we need is an algorithm to solve the problem "pretty well", not absolutely perfect. Greedy algorithms are simple to write and get us a good solution.**

## Set-Covering Problem

Assume we have a radio show, we want to reach listeners in all 50 states (US-based show), but it costs money to be on each station. We need to minimise the number of stations we are on, whilst getting a high number of listeners.

Each station will cover a region, and there will be overlap. How do we figure out what is the smallest set of stations we can play on, whilst covering all 50 states?

Whilst this sounds quite easy, it's an extremely hard problem. Here is how:

* List every possible subset of stations, known as a *power set*. There are `2^n` possible subsets.
* From this list, pick the set with smallest number of stations that cover all 50 states.

The problem here, is that it takes 2^n time to calculate every possible subset. I.e. O(2^n) time. This is fine when we only have a small set of stations to begin with, 5 or 10 etc. Assume we can calculate 10 subsets per second.

| Stations | Time taken      |
|----------|-----------------|
| 5        | 3.2 seconds     |
| 10       | 102.4 seconds   |
| 32       | 13.6 years      |
| 100      | 4 x 10^23 years |

**There is no algorithm fast enough. Greedy algorithms to the rescue!**

Here is a greedy algorithm which comes close:

* Pick the station which covers the most states that haven't been covered yet. It is OK if the station covers some states that have been covered already.
* Repeat until all states covered.

This is an *approximation algorithm*. When calculating the solution would take too much time, an approximation algorithm will work. An approximation algorithm will be judged by:

* How fast they are
* How close they are to optimal

Greedy algorithms are a good choice since they are simple to come up with, the simplicitly means they are generally fast. In this case, this is `O(2^n)`, `n` is the number of stations.

```python
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # we use a set so we have no duplicates, only distinct items.

stations = {} 
stations[“kone”] = set([“id”, “nv”, “ut”]) 
stations[“ktwo”] = set([“wa”, “id”, “mt”]) 
stations[“kthree”] = set([“or”, “nv”, “ca”]) 
stations[“kfour”] = set([“nv”, “ut”]) 
stations[“kfive”] = set([“ca”, “az”])

final_stations = set() 

while states_needed:

    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
            covered = states_needed & states_for_station # intersection of the set, return items that show up in both.
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)
```
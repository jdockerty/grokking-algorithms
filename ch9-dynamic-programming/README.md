# Dynamic Programming (DP)

- [Dynamic Programming (DP)](#dynamic-programming-dp)
- [Knapsack Problem](#knapsack-problem)
  - [Simple solution](#simple-solution)
  - [Dynamic programming solution](#dynamic-programming-solution)
  - [Longest common substring](#longest-common-substring)

**Dynamic Programming is a way to solve hard problems by breaking them into sub-problems and solving these first.**


# Knapsack Problem

Revisiting the problem from the last chapter. We are a thief with a sack that can hold 4 lb of items.

The items available are:

* Stereo, £3000, 4lb
* Laptop, £2000, 3lb
* Guitar, £1500, 1.5lb

## Simple solution

The simplest way to do this would be to try every combination of items, then using the set of items which gives the most value as our result.
Whilst this works, it is really slow. For 3 items, we have 8 sets. 4 items gives us 16 total sets.

Every item we add, doubles the number of sets. The running time would be `O(2^n)`, very slow.

## Dynamic programming solution

We can start by solving the problem for smaller sacks and building up. E.g. a 4lb sack is like having a 1lb + 3lb sack.

Every DP algorithm starts with a grid, here we'll do items to knapsack weight in pounds (lb).

|        | 1             | 2                      | 3                      | 4                      |
|--------|---------------|------------------------|------------------------|------------------------|
| Guitar | £1500, guitar | £1500, guitar          | £1500, guitar          | £1500, guitar          |
| Stereo | £1500, guitar | £1500, guitar          | £1500, guitar          | £3000, stereo          |
| Laptop | £1500, guitar | £1500 guitar           | £2000, laptop          | £3500, laptop + guitar |
| iPhone | £2000, iPhone | £3500, iPhone + guitar | £3500, guitar + iPhone | £4000, laptop + iPhone | 

*iPhone added after calculations done to Laptop with 4lb knapsack.*

At each row, we go across and put the best item in that can fit. Until we move down, we cannot compare items, e.g. until `Stereo - 4lb`, we do cannot fit anything else in until then - we can't select the laptop because we do not know of it yet, it is our best guess at this time. We can only compare the stereo with the guitar when we get to it, the same goes for the laptop to the rest of the items in the various sack sizes.

If we added another item, say an iPhone, with values of £2000 and 1 lb weight, we wouldn't need to recalculate our entire table. We already have stored the best combinations for each row, we simple add another row for an item.

**Dynamic programming only works when each sub-problem is discrete, i.e. it does not depend on other subproblems.**

## Longest common substring

Coming up with a dynamic programming solution can be quite difficult, some tips are:

* Every DP problem solution involves a grid.
* Values in the cells are usually what you are trying to optimise. E.g. the knapsack problem, value of the goods.
* Each cell has a sub-problem. How can we divide our problem into smaller ones?


**Use the Feynman Algorithm:**
1) Write down the problem.
2) Think real hard.
3) Write down the solution!

*A great quip from the book.*

# Introduction to Algorithms

## Introduction

An algorithm is a set of instructions for completing a task. Every bit of code that you write could be called an algorithm, but there are some far more interesting ones, solving interesting problems quickly.

E.g.
* Binary search for cutting down the time taken to find a value in a sorted list.
* GPS devices use graph algorithms to calculate the shortest route to a destination.
* Dynamic Programming (Ch9) is used to write AI that can play checkers.
* Recommendation systems using K-nearest neighbour algorithms (KNN).
* Some problems aren't solved with a fancy algorithm, instead an approximation is required - these are `NP-complete`.

Algorithms are described in Big-O notation, which is elucidated later on.

## Binary Search

If you are searching for a person in the phone book and their name starts with a `K`, you could start at the beginning and flip through the pages, but this would take an incredibly long time. You're more likely to start in the middle of the book, since you know K is around that area, then search from there. Another example of this is searching for a word beginning with *O* in the dictionary, this is near the middle so you'd start there.

In the case where you have a *search problem*, you can use the *binary search algorithm* to solve the problem in an efficient manner. This requires the input to the binary search to be sorted, if the element you're looking for is in the list, then the search will return the position of it (index), if it is not contained within that list then the search will return `null`.

In the children's number guessing game (*I'm thinking of a number between 1 and 100*), to get this in the fewest possible tries, you can use a binary search by starting at 50 - if they respond saying it is too low, then you have eliminated half of the numbers that you would have to guess (1 to 50). Next you could say 75, if that is too high, then you know that 75 to 100 is not correct, then you cut the list in half again by going down. 63 (halfway between 50 and 75), if this is too high, then you go again to 57. In which case this number was correct.

The incorrect way to do this would be *simple search*, whereby you start at 1 and move up by a single value each time. 1, 2, 3, etc...

A great example of this is looking for a word in the dictionary, this has ~240,000 words. It would take you 18 steps, in the **worst case** to find the word. Compared to 240,000 steps using a simple search, this is assuming that the word was at the very end and you had to traverse the entire dictionary.

For any list of *n*, binary search will take $log{_2}{n}$ steps in the worst case. Compared to a simple search, which take *n*, i.e. the entire list.

#### Running time

When discussing algorithms, you'll typically hear it talked about in its *running time*, this means how efficient it is in respect to time and space.

With a linear/simple search, the maximum number of attempts to find the item depends on the size of the list. If there are 4 billion items, you might need 4 billion lookups/guesses, this is *linear time*.

As opposed to binary search, which with 4 billion items would take at most 32 guesses. This runs in *logarithmic time* (*log time*).

Linear = $O(n)$

Logarithmic = $O(log\ n)$

### Big O Notation

This tells you compare the number of operations an algorithm requires and how fast the algorithm grows.

It establishes the *worst case* run time, e.g. looking through a phone book to find someone's name and their's is the very last name. This means that the algorithm won't ever be slower than the worst case, which makes sense as it is the worst possible outcome, it provides a guarantee.

#### Commong Big O run times

Ordered from fastest to slowest:

* $O(log\ n)$ known as log time, e.g. binary search.
* $O(n)$ known as linear time, e.g. simple/linear search.
* $O(n * log\ n)$ Linearithmic, e.g. quicksort.
* $O(n^2)$ Quadratic, e.g. selection sort.
* $O(n!)$ Factorial, e.g. travelling salesman problem


#### Travelling Salesman Problem

This is an example of an $O(n!)$ algorithm, which many computer scientist think can be improved. Although it's incredibly difficult to do so.

Assuming there are 5 cities which a salesman must travel, whilst travelling the minimum distance total. You would want to find the distance between them, then use the lowest total combination, this is done by looking at all the possible combinations of travel options and using the lowest one. This is $n!$, $5! = 120$.

Once you're dealing with larger numbers, it becomes near impossible to answer. E.g. $100!$. This algorithm is terrible, you would think that a different one should be used; however, this is an unsolved problem in Computer Science and there is no known fast algorithm for completing it - the best we can do is come up with an approximation.


### Recap

* Binary search is a lot faster than simple/linear search, especially as the number of operations grows.
* $O(log\ n)$ is faster than $O(n)$. As above.
* Algorithm speed is not measured in seconds.
* Algorithm times are measured in terms of *growth* of an algorithm.
* Algorithm times are written in Big O notation.

### Exercises

#### 1.1
Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

##### Solution/Working

$log{_2}{128}$ = x

Logarithm definitions state that $log{_a}{x}$ = $N$ means $a^n$ = $x$

$2^n = 128$

$2^7 = 128$

Therefore, 7 steps.
#### 1.2 
Suppose you double the size of the list. What’s the maximum number of steps now?


##### Solution/Working

List size = 256

$2^n = 256$ i.e. what exponent to 2 makes 256?

Doubling the value (x2) is adding another 1 to the power.

$2^8 = 256$

#### 1.3

You have a name, and you want to find the person’s phone number in the phone book.

#### Solution

$O(log\ n)$

#### 1.4

You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

##### Solution

$O(n)$

#### 1.5

You want to read the numbers of every person in the phone book.

##### Solution

$O(n)$

#### 1.6

You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)

##### Solution

$O(n)$

Still linear time, as any small constant cancel out as the inputs grow?
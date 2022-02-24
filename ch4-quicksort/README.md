# Quicksort

When coming across a problem that you cannot solve with an algorithm that you know, a good approach is to use divide-and-conquer. An implementation of this technique is the quicksort algorithm.


## Divide & Conquer

Divide and conquer algorithms are recursive. There are two steps to using this technique in order to solve a problem:

* Figure out the base case (how you'll terminate the recursive calls), this is the simplest case that cannot be reduced any further.
* Divide your problem until it reaches the base case.

Example:

    Given an array of numbers, you have to add them all up and return the total.

    Example array: [2, 4, 6]

This is quite easy to do with a loop, but how would you do it with a recursive function?

First, we figure out the base case for the problem.

Interestingly, we have 2 cases which are our base case.

    Array = [ ], there are no elements so the sum is 0.
    Array = [ 6 ], sum is the item value itself, so 6 in this case.

We need to move towards our base case, which is where we have either 0 or 1 item in our array. Therefore, we must continually reduce the problem size as we go.

From here, we know that we can use an array which only has a single element, since we know the sum of that array is the single value in there. We pass the rest of the list back to the function, with the isolated value removed, this is reducing the size of our problem by one each time, until we get an array with a size of 1 - this meets our base case.

My example code for this is shown in [recursive_ex.py](recursive_ex.py).

**If you're writing a recursive function involving an array, the base case is often when the array is empty or with only a single element remaining. If you get stuck, try it with that.**

Recursion is also very useful if you come into functional programming. A functional language like Haskell doesn't have a concept of a loop, so to sum values within a list, you would need to do it recursively.


## Quicksort

This is a sorting algorithm, it is much faster than selection sort and is used in real life. The C standard library has an implementation called `qsort`.

The quicksort algorithm uses divide and conquer.

Using quicksort to sort an array, what is the simplest array that a sorting algorithm could handle? Since some arrays don't need to be sorted at all, an array of 1 or 0 items would satisfy this. These can be returned as is without any swapping of items.

```python
    def quicksort(arr):
        if len(arr) < 2:
            return arr
```

If an array has 3 elements? We need to break this down until we're at the base case. Quicksort does this by picking an element from the array, this is known as the *pivot*, for now this will be the first item in the array (later on we'll go into picking a good pivot).

Now, we can find elements which are smaller or larger than our pivot value - this is called *partitioning*. We have sub-array of all the numbers which are less than the pivot, the pivot value itself, and sub array of numbers that are greater than the pivot.

The sub-arrays we have aren't sorted, they are only partitioned. If they were sorted though, then sorting the entire array would be quite easy, since if these sub arrays are sorted, we can combine them `<left_array> + <pivot> + <right_array> = <whole_array_sorted>`.

To sort the sub arrays, we do our recursive call.
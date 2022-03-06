# Exercises

    Which of these hash functions are consistent?


**5.1**

    f(x) = 1

This is consistent, whatever our input is, x, the output is 1.

**5.2**

    f(x) = rand()

This is not consistent, our output is going to a random number each time.

**5.3**

    f(x) = next_empty_slot() 
    
    # next_empty_slot returns index of the next empty slot in the hash table

This is not consistent, as the empty slot will differ each time and not return the index of the item.

**5.4**

    f(x) = len(x)

This is consistent, we'll always get the same value back depending on the input we provide. E.g. f("hello") will always be 5 and f("hi") will always be 2.


**5.5**

*See book for exercise question*

D

**5.6**

B

**5.7**

D

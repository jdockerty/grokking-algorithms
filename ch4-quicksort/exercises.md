# Exercises

**4.1**

    Write code for recursive sum.

Code was done in [recursive_ex.py](recursive_ex.py)


**4.2**

    Write code to recursively count the number of items in a list

Code done in [recursive_ex.py](recursive_ex.py)

**4.3**

    Write code to find maximum number in a list

Code done in [recursive_ex.py](recursive_ex.py)

**4.4**

    Remember binary search from chapter 1? 
    
    It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

The base case would be when the array is a single item, since this single item is either your key you are looking for or is not it.



How long to each of these operations take?

**4.5**
    
    Printing the value of each element in an array.

O(n), each element means we have to go through the array once.

**4.6**

    Doubling the value of each element in the array.

O(n) again, the constant from the mathematical operation is removed over time.

**4.7**

    Doubling the value of just the first element.

O(1)


**4.8**

    Creating a multiplication table with all the elements in the array. 
    
    So if your array is [2, 3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 3, then by 7, and so on.

O(n^2)
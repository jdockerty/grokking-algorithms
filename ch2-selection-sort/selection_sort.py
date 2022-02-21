
from cgitb import small


def find_smallest(arr):

    smallest = arr[0] # We assume the lowest value is the first element at the very beginning
    smallest_index = 0 # As above, for the index.

    # Check each element to find which is the smallest value.
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index

def selection_sort(arr):
    newArr = []

    for i in range(len(arr)):

        smallest = find_smallest(arr)
        
        # Using .pop will remove the element at the given index from the list and return its value
        # we insert this returned value into the new array.
        newArr.append(arr.pop(smallest))

    return newArr

print(selection_sort([15, 2, 12, 18, 99, 1, 4, 16]))
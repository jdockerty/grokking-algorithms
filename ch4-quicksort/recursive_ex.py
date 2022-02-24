def r_sum(arr):
    """First attempt at recursive sum"""
    if len(arr) == 0:
        print("No size, return 0")
        return 0
    elif len(arr) == 1:
        print("Single element remains, returning {0}".format(arr[0]))
        return arr[0] 
    else:
        print("Array is {0}".format(arr))
        return arr[0] + r_sum(arr[1:])

print("Recursive sum: ", r_sum([2, 4, 6])) # prints 12


def r_count(arr):
    """Recursively count items in a list"""

    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    else:
        return 1 + r_count(arr[1:]) 
        # Array is length > 1, so we take that element away and recursively call the function again.
        # We do 1 + <func call> because we are saving the state of this function call, which will we know there is at least 1 element to add onto the total count.

print("Recursive count: ", r_count([1, 1, 2, 4, 10, 12, -1])) # prints 7

# This answer was taken from the book, couldn't figure this one out.
def r_max(arr):
    """Recursively find the maximum number in a list"""

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1] # our base case is 2 values in the array to compare against each other
    else:
        sub_max = r_max(arr[1:]) # Each call we reduce the list size
        return arr[0] if arr[0] > sub_max else sub_max # finally we end with the first value being compared against the final value that was returned

print("Recursive max: ", r_max([4, 9, 1, 25, 6, 2]))
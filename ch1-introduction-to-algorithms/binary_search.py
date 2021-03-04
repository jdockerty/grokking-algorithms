

def binary_search(arr, item):

    # Keep track of which part of the list you are in.
    low = 0
    high = len(arr) - 1

    # Loop whilst the element hasn't been narrowed down
    while low <= high:
        
        # Check middle element
        mid = (low + high) // 2
        guess = arr[mid]

        # If found, then return position
        if guess == item:
            return mid

        # Guess is too high, reduce high point to mid - 1
        # E.g. Guess between 1 and 100, if 50 is too high, rule out 50 to 100, leaves 1 to 49.
        if guess > item:
            high = mid - 1
        
        # Guess is too low, move low point to mid + 1
        else:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9)) # 4
print(binary_search(my_list, -5)) # None


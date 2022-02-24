def quicksort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less_than_arr = [i for i in arr[1:] if i <= pivot] # sub array of values less than pivot

        greater_than_arr = [i for i in arr[1:] if i > pivot] # sub array of values greater than pivot

        return quicksort(less_than_arr) + [pivot] + quicksort(greater_than_arr)

print(quicksort([9, 1, 10, 15, 5, 8, 2]))
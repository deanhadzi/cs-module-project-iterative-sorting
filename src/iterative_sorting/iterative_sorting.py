# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    """Selection Sort algorithm."""

    # Start by looping through the whole list.
    # We assume that item at 0th index is always sorted.
    for i in range(len(arr)):
        # Assign the value of the current index as the minimum index.
        minimum_index = i
        # Start looping through the rest of the list (unsorted portion).
        # Unsorted portion begins immediatelly following current index.
        for j in range(i+1, len(arr)):
            # If the value of the unsorted index is smaller than the current smallest index
            # update the smallest index to this new index.
            if arr[j] <= arr[minimum_index]:
                minimum_index = j

        # Swap the current index with the smallest value from the unsorted portion.
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

    return arr


# TO-DO: implement the bubble_sort() function below
def bubble_sort(arr):
    """Bubble Sort algorithm."""
    # Set up initial flags.
    active = True
    swap_counter = 0
    cur_index = 0
    next_index = 1

    # Start the loop.
    while active:
        # Compare the current index with the next index in line.
        if cur_index <= len(arr) - 2:
            # If the current index is larger, swap the items.
            if arr[cur_index] > arr[next_index]:
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
                # Increment each index and bump the swap counter.
                cur_index += 1
                next_index += 1
                swap_counter += 1
            # If no swap was done, continue traversing through the array.
            else:
                cur_index += 1
                next_index += 1
        # If we reached the last item in the array and we have more than 0 swaps,
        # reset the counters to initial values.
        elif cur_index == len(arr) - 1 and swap_counter > 0:
            swap_counter = 0
            cur_index = 0
            next_index = 1
        # Otherwise, if we reach the last item and there was no swaps, kill the loop. 
        else:
            active = False

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


# def counting_sort(arr, maximum=None):
#     # Your code here

#     return arr

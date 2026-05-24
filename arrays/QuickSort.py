## Quick Sort

def partition(array, low, high):
    # 1. pick the very last item as our "benchmark" (the pivot).
    # we want to put everything smaller to its left, and everything bigger to its right:
    pivot = array[high]

    # 2. this market tracks the wall where "smaller items" end.
    # it starts just outside the left edge of our current section becasuse we haven't found any small items yet.
    i = low - 1 

    # 3. Use a scanner (j) to look at every item in this section from left to right
    for j in range(low, high):
        # is the current item smaller than or equal to our benchmark?
        if array[j] <= pivot:
            # Yes! move the "smaller items" wall one step to the right to make room
            i += 1
            # swap the small item we found into this newly created room
            array[i], array[j] = array[j], array[i]
    # 4. The loop is done. Everything left of  wall 'i' is smaller than the benchmark
    # Now, swap the benchmark item from the very end into its perfect final spot (right after the wall)
    array [i+1], array[high] = array[high], array[i+1]
    # 5. return the exact spot where the benchmark now sits so the next step knows where to split.
    return i + 1

def quicksort(array, low = 0, high = None):
    # If this is the very first run, set the high boundary to the last item in the list.
    if high is None:
        high = len(array) - 1

    # Basae case: as long as the section has at least 2 items, keep sorting
    # if low >= high, the section has 1 or 0 items, meaning it is already sorted
    if low < high:
        # 1. organize the current section and find where the benchmark item ended up
        pivot_index = partition(array, low, high)
        # 2. Repeat the exact same process for the left side (everything smaller than the benchmark)
        quicksort(array, low, pivot_index-1)
        #3. Repeat the exact same process for the right side (everything bigger than the benchmark)
        quicksort(array, pivot_index + 1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

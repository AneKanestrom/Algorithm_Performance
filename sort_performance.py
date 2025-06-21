import time
import random   
import matplotlib.pyplot as plt

#Insertion Sort (O(n^2))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1 # Start from the previous element
        while j >= 0 and arr[j]> key: # Compare with the key
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1 # Continue checking previous elements
        arr[j + 1] = key # Place the key in its correct position
    return arr

#Merge Sort (O(n log n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Find the middle point
        Left = arr[:mid] 
        Right = arr[mid:] 

        merge_sort(Left)  # Recursively sort the left half
        merge_sort(Right) # Recursively sort the right half

        i = j = k = 0 # Start indices for Left, Right, and arr

        while i < len(Left) and j < len(Right): 
            if Left[i] < Right[j]: # Check if Left element is smaller
                arr[k] = Left[i] # Place element in left in arr
                i += 1
            else:
                arr[k] = Right[j] # Else place element in right in arr
                j += 1 
            k += 1 

        while i < len(Left): # Check if any elements left in Left
            arr[k] = Left[i] 
            i += 1
            k += 1

        while j < len(Right): # Check if any elements left in Right
            arr[k] = Right[j] 
            j += 1
            k += 1
    return arr

#Quick Sort (O(n log n))
def quick_sort(myList):
    if myList == []:
        return []
    else:
        pivot = myList[-1] # Choose the last element as pivot
        lesser = quick_sort([x for x in myList[1:] if x < pivot])
        greater = quick_sort([x for x in myList[1:] if x >= pivot])
        myList = lesser + [pivot] + greater
        return myList

# Test with different sizes
def test_sorting_algorithms(input_arr,sizes, title):
    insertion_times = []
    merge_times = []
    quick_times = []

    for size in sizes:
        arr = input_arr[:size] if len(input_arr) >= size else None
        arr_copy = arr.copy()  # Create one copy per test
        
        # Measure Insertion Sort
        start = time.perf_counter()
        insertion_sort(arr_copy.copy())  # New copy for each sort
        insertion_times.append(time.perf_counter() - start)
        
        # Measure Merge Sort
        start = time.perf_counter()
        merge_sort(arr_copy.copy())
        merge_times.append(time.perf_counter() - start)
        
        # Measure Quick Sort
        start = time.perf_counter()
        quick_sort(arr_copy.copy())
        quick_times.append(time.perf_counter() - start)

        print(f"Completed tests for size: {size}")

    # Plotting (different sizes)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def alredy_sorted_array(size):
    return list(range(size))

def reverse_sorted_array(size):
    return list(range(size, 0, -1))

def equal_elements_array(size):
    num= random.randint(1, 10)  # Random number between 1 and 10
    return [num for _ in range(size)]

def random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def partially_sorted_array(size):
    arr = list(range(size))
    for i in range(size // 2):
        arr[i] = random.randint(1, 100)  # Randomize the first half
    return arr

def small_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

if __name__ == "__main__":
    sizes = [100, 200, 500, 750, 990]  # Reduced max size

    #case 1: Already sorted array
    test_sorting_algorithms(alredy_sorted_array(990),sizes, "Already Sorted Array")

    #case 2: Reverse sorted array
    test_sorting_algorithms(reverse_sorted_array(990),sizes, "Reverse Sorted Array")

    #case 3: Array with equal elements
    test_sorting_algorithms(equal_elements_array(990),sizes, "Array with Equal Elements")

    #case 4: Random array
    random_sizes = [100, 500, 700, 1000, 1500]  # Reduced max size
    test_sorting_algorithms(random_array(1500),random_sizes, "Random Array")

    #case 5: Partially sorted array
    test_sorting_algorithms(partially_sorted_array(990),sizes, "Partially Sorted Array")

    #case 6: Small random array
    small_sizes = [2, 4, 5, 7, 10]  # Smaller sizes for small random array
    test_sorting_algorithms(small_random_array(10), small_sizes, "Small Random Array")




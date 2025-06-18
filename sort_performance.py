import time
import random   
import matplotlib.pyplot as plt

#Insertion Sort (O(n^2))
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#Merge Sort (O(n log n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

#Quick Sort (O(n log n))
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)   

#Test the sorting algorithms
def test_sorting_algorithms():
    sizes = [100, 500, 1000, 5000, 10000]
    insertion_times = []
    merge_times = []
    quick_times = []

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        # Measure Insertion Sort
        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_times.append(time.time() - start_time)

        # Measure Merge Sort
        start_time = time.time()
        merge_sort(arr.copy())
        merge_times.append(time.time() - start_time)

        # Measure Quick Sort
        start_time = time.time()
        quick_sort(arr.copy())
        quick_times.append(time.time() - start_time)

    # Plotting the results
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

    






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

#Quick Sort In-place (O(n log n))
def quick_sort(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

#Test the sorting algorithms
def test_sorting_algorithms():
    sizes = [100, 500, 1000, 2000, 3000]  # Reduced max size
    insertion_times = []
    merge_times = []
    quick_times = []

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
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

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
    
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    test_sorting_algorithms()
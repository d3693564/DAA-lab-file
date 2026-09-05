
import csv
import random
import time
import tracemalloc
from pathlib import Path

OUT = Path("results")
OUT.mkdir(exist_ok=True)

# ---------------- SORTING ALGORITHMS ----------------

def bubble_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a

def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(a):
    a = a.copy()

    def qs(lo, hi):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        pivot = a[mid]

        i, j = lo, hi

        while i <= j:
            while a[i] < pivot:
                i += 1

            while a[j] > pivot:
                j -= 1

            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        if lo < j:
            qs(lo, j)

        if i < hi:
            qs(i, hi)

    qs(0, len(a) - 1)
    return a

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

def make_input(n, condition):
    if condition == "Sorted":
        return list(range(n))
    if condition == "Reverse-sorted":
        return list(range(n, 0, -1))
    data = list(range(n))
    random.shuffle(data)
    return data

def benchmark_sort(func, data, repeats=3):
    times = []
    memories = []
    for _ in range(repeats):
        tracemalloc.start()
        start = time.perf_counter()
        result = func(data)
        elapsed = (time.perf_counter() - start) * 1000
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        assert result == sorted(data)
        times.append(elapsed)
        memories.append(peak / 1024)
    return sum(times) / len(times), max(memories)

# ---------------- FIBONACCI ----------------

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def benchmark_fibonacci(func, n, repeats=3):
    times = []
    memories = []
    for _ in range(repeats):
        tracemalloc.start()
        start = time.perf_counter()
        result = func(n)
        elapsed = (time.perf_counter() - start) * 1000
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(elapsed)
        memories.append(peak / 1024)
    return sum(times) / len(times), max(memories)

def main():
    # Use modest sizes because Python's O(n^2) and recursive algorithms
    # become very slow for large inputs.
    sizes = [100, 500, 1000, 2000]
    conditions = ["Sorted", "Random", "Reverse-sorted"]

    with open(OUT / "sorting_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Algorithm", "Input_Condition", "Input_Size",
            "Execution_Time_ms", "Memory_Usage_KB"
        ])
        for name, func in sorting_algorithms.items():
            for condition in conditions:
                for n in sizes:
                    data = make_input(n, condition)
                    t, m = benchmark_sort(func, data)
                    writer.writerow([name, condition, n, round(t, 4), round(m, 4)])

    # Keep recursive Fibonacci small enough to finish.
    fib_sizes = [10, 20, 25, 30, 32, 34]

    with open(OUT / "fibonacci_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Algorithm", "Input_n", "Execution_Time_ms", "Memory_Usage_KB"
        ])
        for name, func in [
            ("Fibonacci Iterative", fibonacci_iterative),
            ("Fibonacci Recursive", fibonacci_recursive),
        ]:
            for n in fib_sizes:
                t, m = benchmark_fibonacci(func, n)
                writer.writerow([name, n, round(t, 4), round(m, 4)])

    print("Done. CSV files created in the results/ folder.")

if __name__ == "__main__":
    main()

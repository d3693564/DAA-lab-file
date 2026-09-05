# Task 5: Complexity Analysis

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Fibonacci (Recursive) | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) | O(n) |
| Fibonacci (Iterative) | O(n) | O(n) | O(n) | O(1) |
| Fibonacci (Dynamic Programming) | O(n) | O(n) | O(n) | O(n) |

## Comparison of Theoretical and Experimental Results

The experimental results generally agree with the theoretical time
complexities.

Bubble Sort and Insertion Sort showed higher execution times as the
input size increased, which is consistent with their O(n²) average
and worst-case complexity.

Merge Sort and Quick Sort performed better for larger datasets because
their average time complexity is O(n log n).

Recursive Fibonacci showed a very rapid increase in execution time as
the input size increased. This is consistent with its exponential
O(2ⁿ) time complexity.

Iterative Fibonacci was much faster because it has O(n) time complexity
and O(1) space complexity.

Dynamic Programming Fibonacci also performed efficiently because it
reduces repeated calculations and has O(n) time complexity.

Small differences between theoretical and experimental results can
occur because of hardware, Python interpreter overhead, memory
allocation, and measurement variations.
import random
from sorting import *

l = [random.randint(0,100) for i in  range(16)]
print("Sorting with Merge\n")
print(merge_sort(l))
print("\n\nHeap Sort:\n")
print(heap_sort(l))
print()
print()
print("Quick Sort")
print()
print(quick_sort(l))
print()
print("Bubble Sort")
print(bubble_sort(l))

import random
import time
from copy import copy
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from max_heap import heapsort

list_length = int(1e5)
random_list = [random.randrange(int(5e6)) for x in range(list_length)]
original = copy(random_list)
sorted_list = copy(random_list)
sorted_list.sort()

# measure the time
# before = time.time()
# insertion_sort(random_list)
# after = time.time()
# print random_list
# print("Insertion Sort, size: %d time: %f" % (list_length, after-before))

# Merge Sort
random_list = copy(original)
before = time.time()
merge_sort(random_list)
after = time.time()
#print random_list1
print("Merge Sort, size: %d time: %f" % (list_length, after-before))
print sorted_list == random_list

# Selection Sort
# random_list2 = copy(original)
# before = time.time()
# selection_sort(random_list2)
# after = time.time()
# print random_list2
# print("Selection Sort, size: %d time: %f" % (list_length, after-before))
# print random_list2 == random_list1

# Bubble Sort
# random_list3 = copy(original)
# before = time.time()
# bubble_sort(random_list3)
# after = time.time()
# print random_list3
# print("Bubble Sort, size: %d time: %f" % (list_length, after-before))
# print random_list3 == random_list1

# Quick Sort
random_list4 = copy(original)
before = time.time()
quick_sort(random_list4)
after = time.time()
#print random_list4
print("Quick Sort, size: %d time: %f" % (list_length, after-before))
print random_list4 == sorted_list

# Heap Sort
random_list5 = copy(original)
#unsorted = [5, 13, 2, 25, 7, 17, 20, 8, 4]
#random_list5 = copy(unsorted)
before = time.time()
heapsort(random_list5)
after = time.time()
#print unsorted
#print random_list5
print("Heap Sort, size: %d time: %f" % (list_length, after-before))
print random_list5 == sorted_list
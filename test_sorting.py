import unittest
import random
import time
from copy import copy
# Importing all the test code
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from max_heap import heapsort
from bubble_sort import bubble_sort
from radix_sort import radix_sort


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.list_length = int(1e5)
        random_list = [random.randrange(int(2e5)) for x in range(self.list_length)]
        self.original = copy(random_list)
        self.sorted_list = copy(random_list)
        self.sorted_list.sort()

    def testMerge(self):
        result = copy(self.original)
        before = time.time()
        merge_sort(result)
        after = time.time()
        print("Merge Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Merge Sort Failed")

    def testQuick(self):
        result = copy(self.original)
        before = time.time()
        quick_sort(result)
        after = time.time()
        print("Quick Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Quick Sort Failed")

    def testHeap(self):
        result = copy(self.original)
        before = time.time()
        heapsort(result)
        after = time.time()
        print("Heap Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Heap Sort Failed")

    def testBubble(self):
        result = copy(self.original)
        before = time.time()
        bubble_sort(result)
        after = time.time()
        print("Bubble Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Bubble Sort Failed")

    def testInsertion(self):
        result = copy(self.original)
        before = time.time()
        insertion_sort(result)
        after = time.time()
        print("Insertion Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Insertion Sort Failed")

    def testSelection(self):
        result = copy(self.original)
        before = time.time()
        selection_sort(result)
        after = time.time()
        print("Selection Sort, size: %d time: %f" % (self.list_length, after-before))
        self.assertEqual(self.sorted_list, result, "Selection Sort Failed")

    def testRadix(self):
        result = copy(self.original)
        before = time.time()
        result = radix_sort(result)
        after = time.time()
        print("Radix Sort, size: %d time: %f" % (self.list_length, after-before))
        #print "Original List is: ", self.original
        #print "Result of Radix Sort is: ", result
        self.assertEqual(self.sorted_list, result, "Radix Sort Failed")

if __name__ == '__main__':
    unittest.main()
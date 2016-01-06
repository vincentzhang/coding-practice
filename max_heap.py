def max_heapify(alist, i, heap_size):
    if heap_size == 1:
        return
    l, r = 2 * i, 2 * i + 1
    if l <= heap_size-1 and alist[l] > alist[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size-1 and alist[r] > alist[largest]:
        largest = r
    if largest != i:
        tmp = alist[i]
        alist[i] = alist[largest]
        alist[largest] = tmp
        max_heapify(alist, largest, heap_size)


def build_max_heap(alist):
    # heapify all the non-leaf nodes
    for i in range(len(alist) / 2, 0, -1):
        max_heapify(alist, i - 1, len(alist) - 1)


def heapsort(alist):
    build_max_heap(alist)
    heapsize = len(alist)
    for i in range(len(alist) - 1, 0, -1):
        tmp = alist[i]
        alist[i] = alist[0]
        alist[0] = tmp
        heapsize -= 1
        max_heapify(alist, 0, heapsize)

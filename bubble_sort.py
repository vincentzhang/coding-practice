def bubble_sort(alist):
    swap = True
    n = len(alist)
    while swap:
        swap = False
        # From left to right,
        for i in range(n-1):
            if alist[i] > alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
                swap = True
        # Optimized, notice that the n th iteration puts the n-th largest item to the final place
        n -= 1
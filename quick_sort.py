import random
#g_count = 0

def quick_sort(alist, low=0, high=None):
    global g_count
    # divide and conquer, pick a pivot, move the smaller numbers to the left of the pivot
    # bigger numbers to the right
    if high is None:
        high = len(alist)-1
    if low < high:
        #g_count += 1
        #print 'Depth: ', g_count
        pivot = partition(alist, low, high)
        quick_sort(alist, low, pivot-1)
        quick_sort(alist, pivot+1, high)
    else:
        g_count = 0


def partition(alist, low, high):
    # swap a random item with the rightmost item
    rand_idx = random.randint(low, high)
    tmp = alist[high]
    alist[high] = alist[rand_idx]
    alist[rand_idx] = tmp
    pivot = alist[high]
    i = low
    for j in range(low, high):
        if alist[j] <= pivot:
            # swap alist[j] with alist[i]
            tmp = alist[j]
            alist[j] = alist[i]
            alist[i] = tmp
            i = i + 1
    # swap alist[i] with alist[high]
    tmp = alist[i]
    alist[i] = alist[high]
    alist[high] = tmp
    return i  # pivot index

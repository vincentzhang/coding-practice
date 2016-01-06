import random
from copy import copy

# average: O(n)
# worst: O(n^2)

def random_partition(alist, start, end):
    # swap with a random pivot
    rand_idx = random.randint(start, end )
    tmp = alist[end]
    alist[end] = alist[rand_idx]
    alist[rand_idx] = tmp
    # pick pivot, rearrange the list
    pivot = alist[end]
    k = start
    for i in range(start, end):
        if alist[i] <= pivot:
            tmp = alist[k]
            alist[k] = alist[i]
            alist[i] = tmp
            k += 1
    # swap alist[i] with alist[high]
    tmp = alist[k]
    alist[k] = alist[end]
    alist[end] = tmp
    return k  # pivot index

class Error(Exception):
    def __init__(self, msg):
        self.msg = msg
        print msg

def random_select(alist, p, r, i):
    # pick the ith largest item
    if p == r:
        return alist[p]
    if p > r:
        msg = "Has to be a valid range, p=%d, r=%d" % (p, r)
        raise Error(msg)
    q = random_partition(alist, p, r)
    k = q - p + 1
    if i == k:
        return alist[q]
    elif i < k:
        return random_select(alist, p, q - 1, i)
    else:
        return random_select(alist, q + 1, r, i - k)


if __name__ == "__main__":
    alist = [random.randrange(1e2) for _ in range(10)]
    print "unsorted list is: %s" % alist
    print("sorted list is: %s" % sorted(alist))
    print random_select(alist, 0, 9, 1)

def counting_sort(alist, k):
    # k: number of distinct values
    # return sorted numbers in blist
    # Initialize C and B
    # C is the array of counts
    # B is the sorted list
    clist = [0] * k
    blist = [0] * len(alist)
    # clist[i] contains the number of elements = i
    for i in range(len(alist)):
        clist[alist[i]] += 1
    # clist[i] contains the number of elements <= i
    for i in range(1, k + 1):
        clist[i] += clist[i - 1]
    # traverse alist, update blist
    for i in range(len(alist), 0, -1):
        blist[clist[alist[i]]] = alist[i]
        # update clist so that the distinct number won't be inserted to the same idx
        clist[alist[i]] -= 1
    return clist


def radix_sort(alist):
    import copy
    # dim: dimension of the numbers in alist, i.e., how many digits
    # idx_dim: which digit is being processed
    # k: number of possible values at each digit
    idx_dim = 0
    BASE = 10
    max_len = False

    while not max_len:
        max_len = True
        clist = [0] * BASE
        blist = [0] * len(alist)
        divisor = BASE ** idx_dim
        for i in alist:
            tmp = (i / divisor) % BASE
            # clist[tmp] contains the number of elements = tmp
            clist[tmp] += 1
            if max_len and tmp > 0:
                max_len = False
        if max_len:
            break
        # update clist to be the counts of elements <=i
        for i in range(1, BASE):
            clist[i] += clist[i - 1]
        # traverse alist, update blist
        for i in reversed(alist):
            tmp = (i / divisor) % BASE
            blist[clist[tmp]-1] = i
            # update clist so that the distinct number won't be inserted to the same idx
            clist[tmp] -= 1

        # update alist
        alist = blist
        # print("after digit %d, the alist is: " % idx_dim)
        # print alist
        # print "blist is:"
        # print blist


        idx_dim += 1
    return alist
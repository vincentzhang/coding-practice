import time
from random import randrange


def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

def find_lin(alist):
    min_sofar = alist[0]
    for i in alist:
        min_sofar = i if i < min_sofar else min_sofar
    return min_sofar

if __name__ == "__main__":
#   print(findMin([5,4,2,1,0]))
#    print(findMin([0,4,2,1,5]))
    for list_size in range(1000, 10001, 1000):
        alist = [randrange(100000) for x in range(list_size)]
        start = time.time()
        print(find_lin(alist))
        end = time.time()
        print("size: %d time: %f" % (list_size, end-start))


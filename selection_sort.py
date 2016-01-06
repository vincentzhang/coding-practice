def selection_sort(unsorted):
    for i in range(len(unsorted)):
        k = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[k]:
                k = j
        tmp = unsorted[k]
        unsorted[k] = unsorted[i]
        unsorted[i] = tmp

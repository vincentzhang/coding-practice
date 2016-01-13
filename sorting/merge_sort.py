# space: O(n), not in-place
def merge_sort(unsorted):
    if len(unsorted) > 1:
        # print 'len of unsorted', len(unsorted)
        # Divide until only 1 item left in the list
        idx_mid = int(len(unsorted) / 2)
        left = unsorted[0:idx_mid]
        right = unsorted[idx_mid :]
        merge_sort(left)
        merge_sort(right)
        # Merge left and right
        i = 0
        j = 0
        for k in range(len(unsorted)):
            if j < len(unsorted) or i < len(unsorted):
                if j >= len(right):
                    unsorted[k] = left[i]
                    i += 1
                    #print 'i is: ', i
                elif i >= len(left):
                    unsorted[k] = right[j]
                    j += 1
                    #print 'j is: ', j
                elif left[i] <= right[j]:
                    unsorted[k] = left[i]
                    i += 1
                    #print 'i is: ', i
                elif left[i] > right[j]:
                    unsorted[k] = right[j]
                    j += 1
                    #print 'j is: ', j
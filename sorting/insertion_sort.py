#import matplotlib.pyplot as plt
#import time

def insertion_sort(unsorted):
    # print unsorted
    # f = plt.figure()
    # ax = f.gca()
    # ax.bar(range(len(unsorted)), unsorted)
    # f.show()
    # raw_input('Press Enter to continue')
    for i in range(1, len(unsorted)):
        key = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > key:
            unsorted[j+1] = unsorted[j]
            j -= 1
            # ax.cla()
            # ax.bar(range(len(unsorted)), unsorted)
            # f.canvas.draw()
        unsorted[j+1] = key
        # plotting
    #     ax.cla()
    #     ax.bar(range(len(unsorted)), unsorted)
    #     f.canvas.draw()
    # raw_input('Press Enter to continue')


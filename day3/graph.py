import numpy as np
from matplotlib import pyplot as plt

with plt.xkcd():
    N = 3
    heapTimes = (0.004997, 0.0469744, 0.953484)
    sortTimes = (0.011932, 0.16586, 2.88484)

    width = 0.35
    x = np.arange(N)
    plt.bar(x,heapTimes,width,label='maxHeap')
    plt.bar(x+width,sortTimes,width,label='sorting')

    plt.ylabel('Time elapsed')
    plt.xlabel('Input size')
    plt.title('Sorting VS Maxheap')

    plt.xticks(x + width / 2, ('35,000','350,000','3,500,000'))
    plt.legend(loc='best')

    plt.show()
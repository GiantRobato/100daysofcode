from heapq import heapify, heappush, heappop
import random
import time

def compareMethods(n):
    waitTimes = random.sample(range(10000000),n)
    #sorting method
    t = waitTimes[:]
    start = time.time()
    sorted(t)
    playerTimes = t[:-100]
    elapsed1 = time.time() - start
    print('sorting method took: {}'.format(elapsed1))

    #maxheap method
    t = waitTimes[:]
    t = [-1*x for x in t]    
    start = time.time()
    #trick to make heapify create a max heap instead of a min heap
    heapify(t)
    playerTimes = [-heappop(t) for _ in range(100)]
    elapsed2 = time.time() - start
    print('max heap method took: {}'.format(elapsed2))
    try:
        print('speed increase: {}'.format(elapsed1/elapsed2))
    except:
        print('differce in speed smaller than timer can time')



tests = []
tests.append(3500)
tests.append(35000)
tests.append(350000)
tests.append(3500000) # number of fornite users

for test in tests:
    print('Comparing sizes with {} players'.format(test))
    compareMethods(test)
    print('-'*80)

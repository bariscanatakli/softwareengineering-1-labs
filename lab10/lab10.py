import numpy as np
import time
length = np.random.randint (10,10000)

mainList1 = list()
mainList2= list()

for number in range(length):
    mainList1.append(np.random.randint (0,1000))
    mainList2.append(np.random.randint (0,1000))
from sortingalgorithms import *

def measureTimeMerge(func):
    tic = time.time()
    func(mainList1)
    toc = time.time()
    cpu_cost = toc - tic
    return (cpu_cost*(10**6))
def measureTimeInsertion(func):
    tic = time.time()
    func(mainList2)
    toc = time.time()
    cpu_cost = toc - tic
    return (cpu_cost*(10**6))

print(measureTimeMerge(mergeSort), "mergesort")
print(measureTimeInsertion(insertionSort), "insertionsort")

# print(measureTime(mergeSort(val)))
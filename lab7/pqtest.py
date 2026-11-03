"""
Author: Ilaria Teberneac
File: pqtest.py
Compares the time needed to add items to two priority queues.
"""

from priorityqueue import PriorityQueue as PQ1
from priorityqueue2 import PriorityQueue as PQ2
import time


if __name__ == '__main__':

    pq1 = PQ1()
    pq2 = PQ2()

    print("Testing the linked-list queue with 1000 items")
    start = time.time()

    for number in range(1000):
        pq1.push(number)

    finish = time.time()

    print("Linked-list time:", finish - start, "seconds")
    print()
    print("Testing the heap queue with 1000 items")
    start = time.time()

    for number in range(1000):
        pq2.push(number)

    finish = time.time()

    print("Heap time:", finish - start, "seconds")

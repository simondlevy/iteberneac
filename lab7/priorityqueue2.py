"""
Author: Ilaria Teberneac
File: priorityqueue2.py
This program builds a priority queue using a heap.
It lets you add items and remove the smallest item first.
"""

from heap import Heap


class PriorityQueue:

    def __init__(self):

        self.heap = Heap()

    def push(self, data):

        self.heap.add(data)

    def pop(self):

        if self.isEmpty():
            return None
        return self.heap.pop()

    def isEmpty(self):

        return self.heap.isEmpty()


if __name__ == '__main__':

    pq = PriorityQueue()

    for letter in ['c', 'a', 'd', 'b', 'f', 'e']:
        pq.push(letter)

    print("Expected False:", pq.isEmpty())

    print("Expected a:", pq.pop())
    print("Expected b:", pq.pop())
    print("Expected c:", pq.pop())
    print("Expected d:", pq.pop())
    print("Expected e:", pq.pop())
    print("Expected f:", pq.pop())

    print("Expected True:", pq.isEmpty())


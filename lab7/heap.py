"""
Author: Ilaria Teberneac
File name: heap.py
This program creates a heap that keeps the smallest item at the top.
It lets you add items, remove the smallest item, check for an item,
and display the heap.
"""

class Heap:

    def __init__(self):

        self._heap = list()
        self._size = 0

    def add(self, item):

        self._size += 1
        self._heap.append(item)
        curPos = len(self._heap) - 1

        while curPos > 0:
            parent = (curPos - 1) // 2
            parentItem = self._heap[parent]

            if parentItem <= item:
                break
            else:
                self._heap[curPos] = self._heap[parent]
                self._heap[parent] = item
                curPos = parent

    def __contains__(self, item):

        return item in self._heap

    def __str__(self):

        return str(self._heap)
    
    def isEmpty(self):

        return len(self._heap) == 0

    def pop(self):

        if len(self._heap) == 0:
            raise IndexError("Cannot pop from an empty heap")

        self._size -= 1
        topItem = self._heap[0]
        bottomItem = self._heap.pop(len(self._heap) - 1)

        if len(self._heap) == 0:
            return bottomItem

        self._heap[0] = bottomItem
        lastIndex = len(self._heap) - 1
        curPos = 0

        while True:
            leftChild = 2 * curPos + 1
            rightChild = 2 * curPos + 2

            if leftChild > lastIndex:
                break

            if rightChild > lastIndex:
                maxChild = leftChild
            else:
                leftItem = self._heap[leftChild]
                rightItem = self._heap[rightChild]

                if leftItem < rightItem:
                    maxChild = leftChild
                else:
                    maxChild = rightChild

            maxItem = self._heap[maxChild]

            if bottomItem <= maxItem:
                break
            else:
                self._heap[curPos] = self._heap[maxChild]
                self._heap[maxChild] = bottomItem
                curPos = maxChild

        return topItem


if __name__ == '__main__':

    heap = Heap()

    heap.add(7)
    heap.add(4)
    heap.add(9)
    heap.add(1)

    print("Expected [1, 4, 9, 7]:", heap)
    print("Expected True:", 4 in heap)
    print("Expected False:", 10 in heap)

    print("Expected 1:", heap.pop())
    print("Expected [4, 7, 9]:", heap)

    print("Expected 4:", heap.pop())
    print("Expected 7:", heap.pop())
    print("Expected 9:", heap.pop())

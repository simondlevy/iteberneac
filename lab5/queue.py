"""
Author: Ilaria Teberneac
File Name: queue.py
A queue built on top of LinkedList.
Items are added at the back and removed from the front.
"""

from linkedlist import LinkedList

class Queue:

    def __init__(self):

        self.list = LinkedList()

    def push(self, data):

        self.list.addLast(data)

    def pop(self):

        return self.list.removeFirst()

    def peek(self):

        if self.list.isEmpty():
            return None
        return self.list.head.data

    def isEmpty(self):

        return self.list.isEmpty()

    def __len__(self):

        return len(self.list)

    def __iter__(self):

        return iter(self.list)

if __name__ == '__main__':

    q = Queue()

    q.push(2)
    q.push(3)
    q.push(5)
    q.push(7)

    print("Expected 2:", q.pop())
    print("Expected 3:", q.pop())
    print("Expected 5:", q.pop())
    print("Expected 7:", q.pop())
    print("Expected None:",q.pop())

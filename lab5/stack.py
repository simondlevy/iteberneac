"""
Author: Ilaria Teberneac
File Name: stack.py
A stack built on top of LinkedList.
Supports push and pop, peek, isempty, length, and iteration
"""

from linkedlist import LinkedList

class Stack:

    def __init__(self):

        self.list = LinkedList()

    def push(self, data):

        self.list.addFirst(data) 

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

    s = Stack()

    s.push(2)
    s.push(3)
    s.push(5)
    s.push(7)

    print("Expected 7: ", s.pop())
    print("Expected 5: ", s.pop())
    print("Expected 3: ", s.pop())
    print("Expected 2: ", s.pop())
    print("Expected None: ", s.pop())

  



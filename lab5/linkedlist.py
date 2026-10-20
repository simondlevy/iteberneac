"""
Author: Ilaria Teberneac
File Name: linkedlist.py
This is a singly linked list built from Node objects.
It supports adding at the front or back, removing from the front, length, iteration, and printing.
"""

class Node:

    def __init__(self, data, next = None):

        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):

        self.head = None
        self.size = 0

    def isEmpty(self):

        return self.head == None
    
    def __len__(self):

        return self.size

    def addFirst(self, data):

        self.head = Node(data, self.head)
        self.size+= 1

    def addLast(self, data):

        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = newNode
        self.size += 1

    def removeFirst(self): 

        if self.head == None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def __iter__(self):

        cursor = self.head
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):

        return "[" + ", ".join(map(str, self)) + "]"


if __name__ == '__main__':

    lst = LinkedList()

    lst.addFirst(2)
    lst.addFirst(1)
    lst.addLast(3)
    lst.addLast(4)

    print("Expected [1, 2, 3, 4]: ", (lst))             
    print("Expected 4: ", len(lst))  
    print("Expected 1: ", lst.removeFirst()) 
    print("Expected [ 2, 3, 4]: ",(lst))              
    print("Expected True: ", 3 in lst)          

"""
Author: Ilaria Teberneac
File: priorityqueue.py
Priority queue built on top of LinkedList.
Everything is kept in sorted order, smallest at the front.
Push returns the position where the item was inserted.
"""

from linkedlist import LinkedList, Node

class PriorityQueue:

    def __init__(self):

        self.list = LinkedList()

    def push(self, data):

        position = 1
        if self.list.head == None or data < self.list.head.data:
        
            self.list.head = Node(data, self.list.head)
        else:
            
            trailer = self.list.head
            probe = self.list.head.next
            position = 2                    
            while probe != None and data >= probe.data:
                trailer = probe
                probe = probe.next
                position += 1
                
            trailer.next = Node(data, probe)
        self.list.size += 1
        return position                      

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

    pq = PriorityQueue()

    for letter in ['c', 'a', 'd', 'b', 'f', 'e']:
        pq.push(letter)

    print(("Expected a:"), pq.pop())   
    print(("Expected b:"),pq.pop())   
    print(("Expected c:"),pq.pop())   
    print(("Expected d:"),pq.pop())   
    print(("Expected e:"),pq.pop())   
    print(("Expected f:"),pq.pop())   
    print(("Expected None:"),pq.pop())    

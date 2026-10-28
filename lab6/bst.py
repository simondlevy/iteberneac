"""
Author: Ilaria Teberneac
File name: bst.py
This program makes a Binary Search Tree (BST)
"""

import math

class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def add(self, item) :

        # adds new item to the tree
        
        data = Node(item)
        
        if item < self.data:
            if self.left is None :
                self.left = data
            else:
                self.left.add(item)
        else:
            if self.right is None:
                self.right = data
            else:
                self.right.add(item)

    def __contains__(self, item) :

        # checks if the tree contains a specific item
        
        if item == self.data:
            return True
        elif item < self.data:
            if self.left == None:
                return False
            return self.left.__contains__(item)
        else:
            if self.right is None:
                return False
            return self.right.__contains__(item)

    def height(self):

        # checks how tall the three is from the root to the deepest node

        if self.left is not None:
            left_child = self.left.height() 
        else:
            left_child = 0
         
        if self.right is not None:
            right_child = self.right.height() 
        else:
            right_child = 0

        if left_child > right_child:
            return left_child + 1
        else:
            return right_child + 1
        

    def __len__(self):

        # checks how many nodes are there
        
        if self.left is not None:
            left_node = self.left.__len__()
        else:
            left_node = 0

        if self.right is not None:
            right_node = self.right.__len__()
        else:
            right_node = 0

        total_node = left_node + right_node + 1

        return total_node
    
        
    def __str__(self):

        # displays the tree

        if self.left is not None:
            left_child = self.left.__str__()
        else:
            left_child = "_"
            
        if self.right is not None:
            right_child = self.right.__str__()
        else:
            right_child = "_"

        return f" {self.data} ( {left_child} , {right_child} ) "
                                    
    

class BST:

    def __init__(self):

        self.root = None

    def add(self, item):

        if self.root is None:
            data = Node(item)
            self.root = data
        else:
            self.root.add(item)

    def __contains__(self, item):

        if self.root is None:
            return False
        else:
            return self.root.__contains__(item)

    def height(self):

        if self.root is None:
            return 0
        else:
            return self.root.height()

    def __len__(self): 

        if self.root is None:
            return 0
        else:
            return self.root.__len__()

    def isBalanced(self):

        # checks if the tree is balanced based on the given formula

        return self.height()<=math.ceil(math.log2(self.__len__()))

    def __str__(self):

        if self.root is None:
            return "_"
        else:
            return str(self.root)


if __name__== '__main__':

    test_tree = BST()

    test_tree.add(1)
    test_tree.add(7)
    test_tree.add(3)
    test_tree.add(9)
    test_tree.add(4)

    print("Expected True:", 9 in test_tree)
    print("Expected True:", 1 in test_tree)
    print("Expected True:", 7 in test_tree)
    print("Expected False:", 8 in test_tree)
    print("Expected False:", 2 in test_tree)
    print("Expected False:", 5 in test_tree)
    print()
    print("Expected 4: " , test_tree.height())
    print()
    print("Expected 5: " , len(test_tree))
    print()
    print("Expected False:", test_tree.isBalanced())
    print()
    print(test_tree)

    test_tree = BST()

    test_tree.add("A")
    test_tree.add("C")
    test_tree.add("D")
    test_tree.add("M")
    test_tree.add("P")
    test_tree.add("O")
    test_tree.add("L")
    test_tree.add("K")

    print("\n\n")

    print("Expected True:", "A" in test_tree)
    print("Expected True:", "C" in test_tree)
    print("Expected True:", "K" in test_tree)
    print("Expected False:", "J" in test_tree)
    print("Expected False:", "X" in test_tree)
    print("Expected False:", "Z" in test_tree)
    print()
    print("Expected 6: " , test_tree.height())
    print()
    print("Expected 8: " , len(test_tree))
    print()
    print("Expected False:", test_tree.isBalanced())
    print()
    print(test_tree)


    test_tree = BST()

    test_tree.add(7)
    test_tree.add(4)
    test_tree.add(9)
    test_tree.add(1)
    test_tree.add(5)
    test_tree.add(10)
    test_tree.add(8)


    print("\n\n")

    print("Expected True:", 7 in test_tree)
    print("Expected True:", 8 in test_tree)
    print("Expected False:", 200 in test_tree)
    print("Expected False:", 0 in test_tree)
    print()
    print("Expected 3: " , test_tree.height())
    print()
    print("Expected 7: " , len(test_tree))
    print()
    print("Expected True:", test_tree.isBalanced())
    print()
    print(test_tree)

    

 



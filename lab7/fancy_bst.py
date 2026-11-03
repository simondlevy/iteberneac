"""
Author: Ilaria Teberneac
File Name: fancy_bst.py
This programm adds up to th epreviously created BST class
preorder, inorder and postorder methods.
It also adds a bananced method which would return a balanced version of BST.
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
            if self.left is None:
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
    

    def preorder(self):

        # Returns Parent first then all its Kids
        
        test_list = []
        test_list.append(self.data)
        if self.left is not None:
            test_list +=  self.left.preorder()
        if self.right is not None:
            test_list += self.right.preorder()

        return test_list
            

    def inorder(self):

        # Goes from kid to parent in a paired order 
        
        test_list = []
        
        if self.left is not None:
           test_list += self.left.inorder()
        
        test_list.append(self.data)
        
        if self.right is not None:
           test_list += self.right.inorder()


        return test_list

    def postorder(self):

        # Returns all Kids first then their Parents
        
        test_list = []
        
        if self.left is not None:
           test_list += self.left.postorder()
        if self.right is not None:
           test_list += self.right.postorder()

        test_list.append(self.data)

        return test_list
        

    
                                    
    

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

    def preorder(self):
        
        if self.root is None:
            return []
        else:
            return self.root.preorder()

    def inorder(self):
        
        if self.root is None:
            return []
        else:
            return self.root.inorder()

    def postorder(self):
        
        if self.root is None:
            return []
        else:
            return self.root.postorder()
        

    def balanced(self):

        # Returns a new balanced BST 

        items = self.inorder()
        new_tree = BST()


        def recurse(left, right):

            if left <= right:

                middle = (left + right) //2

                new_tree.add(items[middle])

                recurse(left, middle-1)
                recurse(middle+1, right)

        recurse(0, len(items) - 1)

        return new_tree


if __name__== '__main__':

    bst = BST()

    bst.add(2)
    bst.add(3)
    bst.add(1)

    print("Expected [2, 1, 3] : ", bst.preorder())
    print("Expected [1, 2, 3] : " , bst.inorder())
    print("Expected [1, 3, 2] : " , bst.postorder())
    print()
    print("Expected (2(1(_,_),3(_,_)) : ", bst.balanced())

    print("\n\n")

    bst = BST()

    bst.add(7)
    bst.add(4)
    bst.add(9)
    bst.add(3)
    bst.add(5)
    bst.add(8)
    bst.add(10)


    print("Expected [7, 4, 3, 5, 9, 8, 10] : ", bst.preorder())
    print("Expected [3, 4, 5, 7, 8, 9, 10] : ", bst.inorder())
    print("Expected [3, 5, 4, 8, 10, 9, 7] : ", bst.postorder())
    print()
    print("Expected (7(4(3(_,_),5(_,_)),9(8(_,_),10(_,_))) : ", bst.balanced())

    print("\n\n")

    bst = BST()

    bst.add(7)
    bst.add(6)
    bst.add(5)
    bst.add(4)
    bst.add(3)
    bst.add(2)
    bst.add(1)
    
    print()
    print("Expected (4(2(1(_,_), 3(_,_)),6(5(_,_),7(_,_))) : ", bst.balanced())

    
    

    

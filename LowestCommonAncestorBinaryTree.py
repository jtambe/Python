import sys
#sys.path.append()
import os
os.getcwd()
#from directory/file.py
#import BinarySearchTree
# This algo also applies for binary tree,
# Although int his example I have only imported BST modules from previous work
from BinarySearchTree import *


def LCA(root, x, y):

    if root is None:
        return None

    if root.value == x or root.value == y:
        return root


    left = LCA(root.leftChild, x, y)
    right = LCA(root.rightChild, x, y)

    if left is not None  and right is not None:
        return root

    if left is None and right is None:
        return None

    return left if left is not None else right











bst = Tree()
bst = Tree()
bst.insert(10)
bst.insert(15)
bst.insert(23)
bst.insert(12)
bst.insert(17)
bst.insert(29)
bst.insert(18)
bst.insert(11)
bst.insert(32)
bst.insert(30)
bst.insert(24)
bst.insert(67)

lcaNode = (LCA(bst.root, 11, 32))
print(lcaNode.value)






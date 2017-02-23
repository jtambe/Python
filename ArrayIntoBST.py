# Given an Array, Create a  binary tree with minimum height to store that array

#Algo

# 1. Sort the Array
# 2. Insert middle element in array as the root
# 3. Insert into left subtree, the left subarray
# 4. Insert into right subtree, the right subarray
# 5. recursively repeat until end of array < start of array

import sys
#sys.path.append()
import os
os.getcwd()
#from directory/file.py
#import BinarySearchTree
from BinarySearchTree import *





def AddToTree(a, start, end):
    if len(a) == 0:
        return False

    if end < start:
        return None

    mid = (start+end)//2
    node = Node(a[mid])
    node.leftChild = AddToTree(a, start, mid-1)
    node.rightChild = AddToTree(a, mid +1, end)

    return node


def CreateMinimalBST(a):
    a = sorted(a)
    root = AddToTree(a, 0, len(a)-1)
    root.inorder()

def main():
    a = [5,8,5,9,1,2,7,87,34,27]
    CreateMinimalBST(a)

if __name__ == "__main__":
    main()
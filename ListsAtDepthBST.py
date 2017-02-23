# create lists of vertices at each depth of BST

import os
os.getcwd()
from BinarySearchTree import * # using my BST generation code


def getLinkedLists(root):

    # maintain a level variable for current depth in tree traversal
    level = 0
    # DepthWiseList will hold  lists for each depth
    DepthWiseList = []
    # initially append root to it
    DepthWiseList.append([root])

    while(1):
        # maintain a list for each level
        listForLevel = []

        # find out how many nodes are there at the current level in DepthwiseList
        for i in range( len(DepthWiseList[level]) ):

            #for each node at current level in depthwise list, add left and right children in current level's listforlevel
            node = DepthWiseList[level][i]
            if node.leftChild:
                listForLevel.append(node.leftChild)
            if node.rightChild:
                listForLevel.append(node.rightChild)

        # if there is any node in the current level, add this current level's list in DepthwiseList
        # and proceed further with level++
        if len(listForLevel) > 0:
            DepthWiseList.append(listForLevel)
        else:
            break

        level += 1

    return DepthWiseList



# Here comes the driver program
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

#Above insertions only form right subtree after root as all elements are bigger than root

DepthWiseLists = (getLinkedLists(bst.root))

for eachList in DepthWiseLists:
    print(" ")
    for eachItem in eachList:
        print(eachItem.value, end=" , ")


#output is as follows
'''
10 ,
15 ,
12 , 23 ,
11 , 17 , 29 ,
18 , 24 , 32 ,
30 , 67 ,
'''













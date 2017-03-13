from BinarySearchTree import *


def Invert(current, parent):

    if current is None:
        return None

    if current.leftChild:
        Invert(current.leftChild, current)
        current.leftChild = None

    if current.rightChild:
        Invert(current.rightChild, current)
        current.rightChild = None


    current.leftChild = parent
    return

bst = Tree()
bst.insert(15)
bst.insert(23)
bst.insert(10)
bst.insert(12)
bst.insert(17)
bst.insert(29)
bst.insert(18)
bst.insert(11)
bst.insert(32)
bst.insert(30)
bst.insert(24)
bst.insert(67)

Invert(bst.root, None)
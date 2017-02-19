
# #set operations
# test = set([2,3,9,3,12,65,6,7,1])
# print(sorted(test))
# test.add(65) # adding duplicate
# test.add(12) # adding duplicate
# print(sorted(test))


#Check if given tree Binary Search Tree

Globalmin = NEG_INFINITY = float("-infinity")
Globalmax =INFINITY = float("infinity")


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

# print(Globalmin)
# print(Globalmax)

def IsBST(Node, min, max): #First root node is passed with global min and max
        if Node is None:  # if recursion reaches point with no further Node, return True
            return True

        if Node.data < min or Node.data > max: # if at any point in recursion, given node fails these 2 conditions, return false
            return False

        # recursively call IsBST
        # for left node of every node, min value can be global lowest, but max value cannot be greater than parent or parent-1
        # for right node of every node, max value can be global highest, but max value cannot be greater than parent or parent+1
        return IsBST(Node.left, Globalmin, Node.data-1) and IsBST(Node.right, Node.data+1 , Globalmax )


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if IsBST(root, Globalmin, Globalmax):
    print("It is BST")
else:
    print("It is not BST")


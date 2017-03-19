class Node:
    # constructor

    def __init__(self,val):
        self.value = val
        #self.parent = parent
        self.leftChild = None
        self.rightChild = None
        self.Parent = None

    # recursive insert function
    def insert(self,data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                self.leftChild.Parent = self
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                self.rightChild.Parent = self

    # recursive find function
    def find(self, data):
        if self.value == data:
            return True
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def findParent(self,data):
        if self.value == data:
            print("parent of "+ str(data) + " is : " + str(self.Parent.value))
        elif data < self.value:
            if self.leftChild:
                return self.leftChild.findParent(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.findParent(data)
            else:
                return False

    # recursive traversal function
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    def getHeight(self,child):
        if child is None:
            return -1
        else:
            return (1 + max(child.getHeight(child.leftChild), child.getHeight(child.rightChild)))



class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            self.root.Parent = None
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print('Preorder')
        self.root.preorder()

    def postorder(self):
        print('postorder')
        self.root.postorder()

    def inorder(self):
        print('inorder')
        self.root.inorder()

    def findParent(self,data):
        if self.root:
            if self.root.value == data:
                return "it is root node"
            else:
                return self.root.findParent(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight(self.root)
        else:
            return -1

    def remove(self,data):

        # empty tree
        if self.root is None:
            return False

        # deleting root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.leftChild
            elif self.root.leftChild and self.root.rightChild:

                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.RightChild
                else:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None
            return True


        parent = None
        node = self.root

        # look for data to be removed
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # data not found
        if node is None or node.value != data:
            return False

        # remove node with no children
        elif node.leftChild is None and node.rigthChild is None:
            if data < parent.value:
                parent.leftChild = None
            if data > parent.value:
                parent.rightChild = None
            return True

        # remove node with only left child
        elif node.leftChild and node.rigthChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            if data > parent.value:
                parent.rightChild = node.leftChild
            return True

        # remove node with only right child
        elif node.leftChild is None and node.rigthChild:
            if data < parent.value:
                parent.leftChild = node.rigthChild
            if data > parent.value:
                parent.rightChild = node.rigthChild
            return True

        # remove node has both children
        else:
            delNodeParent = None
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.RightChild
            else:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None
        return True





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

#bst.inorder()

#bst.findParent(12)

#print("Height of tree is : "+ str(bst.getHeight()))

#bst.preorder()
#bst.postorder()

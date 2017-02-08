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
                self.leftChild.Parent = self.value
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                self.rightChild.Parent = self.value


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
            print("parent of "+ str(data) + " is : " + str(self.Parent))
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
            self.root.Parent = -99
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
            return self.root.findParent(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight(self.root)
        else:
            return -1


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

bst.inorder()

bst.findParent(12)

print("Height of tree is : "+ str(bst.getHeight()))
#bst.preorder()
#bst.postorder()

'''
credit : https://www.youtube.com/watch?v=foAoAMEObno
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


def Eval(root):

    if root is None:
        return False

    current = root
    if current.left is None and current.right is None:
        return current.data
    else:
        if current.data == '+':
            return Eval(current.left) + Eval(current.right)
        if current.data == '-':
            return Eval(current.left) - Eval(current.right)
        if current.data == '*':
            return Eval(current.left) * Eval(current.right)
        if current.data == '/':
            return Eval(current.left) / Eval(current.right)





root = Node('+')
root.left = Node('*')
root.right = Node('/')
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(2)

print(Eval(root))
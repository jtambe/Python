def MaxDepth(root):
    if root == None:
        return 0

    return 1 + max(MaxDepth(root.left), MaxDepth(root.right))

def MinDepth(root):
    if root == None:
        return 0

    return min(MinDepth(root.left), MinDepth(root.right))

def IsTreeBalanced(root):
    return (MaxDepth(root) - MinDepth(root) <= 1)

def MaxDepth(root):
    if root == None:
        return 0

    return 1 + max(MaxDepth(root.left), MaxDepth(root.right))

def MinDepth(root):
    if root == None:
        return 0

    return 1 + min(MinDepth(root.left), MinDepth(root.right))


# Tree is balanced if difference between Max depth of tree and Min Depth of tree does not exceed one
def IsTreeBalanced(root):
    return (MaxDepth(root) - MinDepth(root) <= 1)

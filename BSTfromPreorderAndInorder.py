

class Node:

    def __init__(self,val):
        self.value = val
        self.Left= None
        self.Right = None
        self.Parent = None

root = Node(None)

def PreOrderInorderToBST(inorder, preorder, Root):

    # print("inorder" + str(inorder))
    # print("preorder" + str(preorder))
    if Root == None or len(inorder) == 0:
        return
    else:
        print("Root: " + str(Root.value))
        subRootInorderIndex = inorder.index(Root.value)
        leftSubTree = inorder[:subRootInorderIndex]
        rightSubTree = inorder[subRootInorderIndex+1:]

        print("leftSubTree : " + str(leftSubTree))
        print("rightSubTree : " + str(rightSubTree))

        RootPreorderIndex = preorder.index(Root.value)
        count = 0
        while preorder[RootPreorderIndex] not in leftSubTree and count <= len(leftSubTree):
            RootPreorderIndex += 1
            count += 1
        if count < len(leftSubTree):
            leftSubRoot = Node(preorder[RootPreorderIndex])
            # leftSubRoot = Node(leftSubTree[count])
            print("leftSubRoot: " + str(leftSubRoot.value))
        else:
            leftSubRoot = None
            print("leftSubRoot: " + str(leftSubRoot))


        RootPreorderIndex = preorder.index(Root.value)
        count = 0
        while preorder[RootPreorderIndex] not in rightSubTree and count <= len(rightSubTree):
            RootPreorderIndex += 1
            count += 1
        if count < len(rightSubTree):
            rightSubRoot = Node(preorder[RootPreorderIndex])
            print("rightSubRoot: " + str(rightSubRoot.value))
        else:
            rightSubRoot = None
            print("rightSubRoot: " + str(rightSubRoot))

        Root.left = leftSubRoot
        Root.right = rightSubRoot

        PreOrderInorderToBST(leftSubTree, preorder, leftSubRoot)
        PreOrderInorderToBST(rightSubTree, preorder, rightSubRoot)

        return



def main():
    inorder = [10,	11,	12,	15,	17,	18,	23,	24,	29,	30,	32,	67]
    preorder = [15,	10,	12,	11,	23,	17,	18,	29,	24,	32,	30,	67]
    postorder = [11, 12, 10,18,	17,	24,	30,	67,	32,	29,	23,	15]

    # print(preorder[3:])
    # print(preorder[:3])
    global root
    root = Node(preorder[0])
    PreOrderInorderToBST(inorder, preorder, root)


if __name__ == '__main__':
    main()

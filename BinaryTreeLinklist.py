#   Depth first search
#       preorder traversal   root -> left -> right
#       inorder traversal    left -> root -> right
#       postorder traversal  left -> right ->root
#   Breadth first search 
#       levelorder traversal(dfid)

class BinaryTree:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

tree = BinaryTree("A")


# preorder traversal                #                        A
root = BinaryTree("A")              #                      /   \
left = BinaryTree("B")              #                     /     \
right = BinaryTree("C")             #                    B       C  
root.left = left                    #                   /  \    /  \
root.right = right                  #                  D    E  F    G
a1 = BinaryTree("D")                #                 / \
a2 = BinaryTree("E")                #                H   I 
left.left = a1
left.right = a2
b1 =  BinaryTree("F")
b2 = BinaryTree("G")
right.left = b1
right.right = b2
c1 = BinaryTree("H")
c2 = BinaryTree("I")
root.left.left.left = c1
root.left.left.right = c2

#  dfs
def preOrder(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrder(rootNode.left)
    preOrder(rootNode.right)
# print(preOrder(root))

def inOrder(rootNode):
    if rootNode is None:
        return
    inOrder(rootNode.left)
    print(rootNode.data)
    inOrder(rootNode.right)
# print(inOrder(root))

def postOrder(rootNode):
    if rootNode is None:
        return 
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.data)
# print(postOrder(root))


#  bfs dfid = i = 3(till level 3)
from queueLinkList import Queue,Node

def levelorder(rootNode):
    if rootNode is None:
        return
    que = []
    que.append(rootNode)
    while len(que) != 0 :
        currentRoot = que.pop(0)
        print(currentRoot.data)
        if currentRoot.left is not None:
            que.append(currentRoot.left)
        if currentRoot.right is not None:
            que.append(currentRoot.right)
levelorder(root)

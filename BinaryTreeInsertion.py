#display as per level order
from typing import Counter


def DisplayTree(rootNode):
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



class BinaryTree:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
def insert(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = []
        customQueue.append(rootNode)
        while len(customQueue) != 0:
            root = customQueue.pop(0)
            if root.left is not None:
                customQueue.append(root.left)
            else:
                root.left = newNode
                return "Successfully Inserted"
            if root.right is not None:
                customQueue.append(root.right)
            else:
                root.right= newNode
                return "Successfully Inserted"

root = BinaryTree("A")
insert(root,BinaryTree("B"))
insert(root,BinaryTree("C"))
insert(root,BinaryTree("D"))
insert(root,BinaryTree("E"))
insert(root,BinaryTree("F"))
insert(root,BinaryTree("G"))
# DisplayTree(root)

print(root.data)
print(root.left.data,"\t",root.right.data)
print(root.left.left.data,root.left.right.data,end="")
print("\t",root.right.left.data,root.right.right.data)
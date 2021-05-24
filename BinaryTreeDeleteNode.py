from typing import Counter


class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# level order display
def display(root):
    if root is None:
        return
    que=[]
    que.append(root)
    while len(que)!=0:
        current = que.pop(0)
        print(current.data)
        if current.left !=None:
            que.append(current.left)
        if current.right != None:
            que.append(current.right)

def insert(root,newNode):
    if not root:
        root  = newNode
    else:
        que = []
        que.append(root)
        while len(que)!= 0 :
            current = que.pop(0)
            if current.left is not None:
                que.append(current.left)
            else:
                current.left = newNode
                return 0
            if current.right is not None:
                que.append(current.right)
            else:
                current.right = newNode
                return 0
root = BinaryTree("A")
insert(root,BinaryTree("B"))
insert(root,BinaryTree("C"))
insert(root,BinaryTree("D"))
insert(root,BinaryTree("E"))
insert(root,BinaryTree("F"))
insert(root,BinaryTree("G"))
insert(root,BinaryTree("H"))
insert(root,BinaryTree("I"))
display(root)


def finddeepNode(root):
    que = []
    que.append(root)
    while len(que)!=0:
        current = que.pop(0)
        if current.left != None:
            que.append(current.left)
        if current.right != None:
            que.append(current.right)
    return current.data
print("Deep node :",finddeepNode(root))
deepvalue = finddeepNode(root)


               
#                        A
#                     /    \
#                    B      C
#                   / \    / \
#                  D   E  F   G
#                 / \
#                H   I 

def delDeepNode(root,deepvalue):
    que = []
    que.append(root)
    while len(que)!=0:
        current = que.pop(0)
        if current.left !=None:
            if current.left.data == deepvalue:
                current.left = None
            else:
                que.append(current.left)
        if current.right != None:
            if current.right.data == deepvalue:
                current.right = None
            else:
                que.append(current.right)
delDeepNode(root,deepvalue)
display(root)


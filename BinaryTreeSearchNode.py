class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = BinaryTree("A")
left = BinaryTree("B")
right = BinaryTree("C")
root.left = left
root.right = right
a1 = BinaryTree("D")
a2 = BinaryTree("E")
left.left = a1
left.right = a2
b1 = BinaryTree("F")
b2 = BinaryTree("G")
right.left=b1
right.right = b2

def Search(rootNode,num):
    if rootNode is None:
        return
    que = []
    que.append(rootNode)
    while len(que)!=0:
        current = que.pop(0)
        print(current.data)
        if current.data == num:
            return f"data {num} is present"
        if current.left != None:
            que.append(current.left)
        if current.right != None:
            que.append(current.right)
    return f"Data {num} not found"
    
num = input("Enter data to search :")
print(Search(root,num))
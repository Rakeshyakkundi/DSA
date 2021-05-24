class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def display(root):
    if root is None:
        return
    display(root.left)
    print(root.data)
    display(root.right)
    


def insert(root,newValue):
    if root is None:
        root = BinarySearchTree(newValue)
    elif newValue <=root.data:
        if root.left is None:
            root.left = BinarySearchTree(newValue)
        else:
            insert(root.left,newValue)
    else:
        if root.right is None:
            root.right = BinarySearchTree(newValue)
        else:
            insert(root.right,newValue)
    return 0

root = BinarySearchTree(70)
insert(root,50)
insert(root,90)
insert(root,30)
insert(root,60)
insert(root,80)
insert(root,100)
insert(root,20)
insert(root,40)
display(root)


def search(root,data):
    if root.data == data:
        print(f"found {data}")
    elif data<root.data:
        if root.left.data == data:
            print(f"found {data} in left")
        else:
            search(root.left,data)
    else:
        if root.right.data == data:
            print(f"found {data} in right")
        else:
            search(root.right,data)
search(root,100)

data = 100
def deleteNode(root,data):
    if data<root.data:
        if root.left.data == data:
            root.left = None
        else:
            deleteNode(root.left,data)
    else:
        if root.right.data == data:
            root.right = None
        else:
            deleteNode(root.right,data)
deleteNode(root,data)
display(root)
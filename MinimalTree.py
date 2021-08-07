arr = [1,2,3,4,5,6,7,8,9]
ln = len(arr)
# print(arr[int(ln/2)])

class BinaryTree:
    def __init__(self,data=None):
        self.data =data
        self.left = None
        self.right = None
    

def insert(root,newData):
    if root.data == None:
        root.data = newData
    else:
        if root.data>newData:
            if root.left is None:
                a = BinaryTree(newData)
                root.left = a
            elif root.right is None:
                a = BinaryTree(newData)
                root.right = a
            else:
                insert(root.left,newData)
        if root.data<newData:
            if root.right is None:
                a = BinaryTree(newData)
                root.right = a
            elif root.left is None:
                a = BinaryTree(newData)
                root.left = a
            else:
                insert(root.right,newData)
    return 0

def display(root):
    if root is None:
        return
    display(root.left)
    print(root.data)
    display(root.right)

root = BinaryTree()

# while True:
#     if len(arr)==0:
#         break
#     num = arr

insert(root,arr[int(ln/2)])
arr.remove(5)
for i in arr:
    insert(root,i)

# display(root)
print(root.data)
print(root.left.data,root.right.data)
print(root.left.left.data,root.left.right.data,root.right.left.data,root.right.right.data)
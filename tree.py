#  1.complete binary tree : except last leaf all are full
#  2.Full binary tree : all have max child in tree
#  Depth first order : 1.in-order 2.pre-order 3.post-order
#  1.pre-order : root - left - right
#  2.in-order: left - root - right
#  3.post-order: left - right - root

#                      1
#                 2        3
#               4   5     6  7

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class Binary:
    def __init__(self,root):
        self.root = Node(root)

    def pre_order(self,start,traversal):
        if start:
            traversal  += str(start.value)+" "
            traversal = self.pre_order(start.left,traversal)
            traversal = self.pre_order(start.right,traversal)
        return traversal
    def in_order(self,start,traversal):
        if start:
            traversal = self.in_order(start.left,traversal)
            traversal += str(start.value)+" "
            traversal = self.in_order(start.right,traversal)
        return traversal
    def post_order(self,start,traversal):
        if start:
            traversal = self.in_order(start.left,traversal)
            traversal = self.in_order(start.right,traversal)
            traversal += str(start.value)+" "
        return traversal



tree = Binary(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left  = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


# print(tree.pre_order(tree.root,""))
print(tree.post_order(tree.root,""))












class TreeNode:
    def __init__(self, data, children = None):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('1',[])
two = TreeNode('2',[])
three = TreeNode('3',[])
tree.addChild(two)
tree.addChild(three)

four = TreeNode('a1',[])
five = TreeNode('a2',[])
two.addChild(four)
two.addChild(five)
six = TreeNode('b2',[])
seven = TreeNode('b2',[])
three.addChild(six)
three.addChild(seven)
print(tree)
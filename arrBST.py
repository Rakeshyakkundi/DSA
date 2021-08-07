# missing positive number
# num = [3,4,-1,1]
# i = 0;j = len(num)-1
# ls = [i for i in range(min(num),max(num)+1) if i>0]
# while i<=j:
#     if num[i] in ls:
#         ls.remove(num[i])
#     i +=1
# print(min(ls))

# num = [4,1,2,1,2]
# dir={}
# for i in range(len(num)):
#     if num[i] in dir:
#         dir[num[i]] +=1
#     else:
#         dir[num[i]] = 0
# print('duplicate :',[i for i in dir if dir[i]<1])
COUNT = [10] 
class BinaryTree:
    def __init__(self,data=None):
        if data is None:
            self.data= None
        else:
            self.data = data
        self.left = None
        self.right = None
    
    def insert(self,root,Data):
        if root.data <= Data:
            if root.left is None:
                root.left = BinaryTree(Data)
            else:
                self.insert(root.left,Data)
        elif root.data > Data:
            if root.right is None:
                root.right = BinaryTree(Data)
            else:
                self.insert(root.right,Data)
        return 0


def print2DUtil(root, space) :
    if (root == None) :
        return
    space += COUNT[0]
    print2DUtil(root.right, space) 
    print() 
    for i in range(COUNT[0], space):
        print(end = " ") 
    print(root.data) 
    print2DUtil(root.left, space) 
def print2D(root) :
    print2DUtil(root, 1) 

                #           5
                #     4            6
                # 2       4.5  5.5    8

obj = BinaryTree(5)
obj.insert(obj,4)
obj.insert(obj,6)
obj.insert(obj,2)
obj.insert(obj,5.5)
obj.insert(obj,4.5)
obj.insert(obj,8)
print2D(obj)
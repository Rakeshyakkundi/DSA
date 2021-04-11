class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkList:
    def __init__(self):
        self.head = None
        self.i = 0
        self.j = True
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def create(self,newNode):
        lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next = newNode
    def display(self):
        dispNode = self.head
        while True:
            if dispNode.next is None:
                break
            print(dispNode.data)
            dispNode = dispNode.next
        print(dispNode.data)
    
    def reverse(self):
        prev = None
        current = self.head
        while current.next != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        current.next = prev
        self.head = current

    def M_and_N(self,M,N):
        self.M = M
        self.N = N
        current = self.head
        while True:
            try:
                for i in range(1,self.M):
                    print("Data :",current.data)
                    current = current.next
                temp = current.next
                for j in range(self.N):
                    # print("Data :",current.data)
                    temp =  temp.next
                current.next = temp
                current = temp
            except:
                break
    
    def is_reverse(self,current):
        if current == None:
            return
        self.is_reverse(current.next)
        print(current.data)

    def is_palindrome(self,left,right):
        if right == None:
            return 
        self.is_palindrome(left,right.next)
        a = self.next1(left)
        if right.data == a:
            pass
        else:
            print("not a palindrome")
            self.j = False
            exit()
        return self.j
        
    def next1(self,left):
        if self.i ==0 :
            self.i = 9
            return self.head.data
        else:
            self.head = self.head.next
            return self.head.data
        
                  
        



        

s1 = Node(1)
s2 = Node(3) 
s3 = Node(3) 
s4 = Node(3) 
s5 = Node(1)
# None

# s6 = Node(1)
# s7 = Node(7)
# s8 = Node(8)
# s9 = Node(9)
# s10 = Node(10)

link = LinkList()
link.insert(s1);link.insert(s2);link.insert(s3);link.insert(s4);link.insert(s5)
# link.insert(s6)
# link.insert(s7);link.insert(s8)
# link.insert(s9);link.insert(s10)
# link.display()
# link.reverse()
# link.display()
# link.M_and_N(3,2)
# for i in range(9,0,-1):
#     n = Node(i)
#     link.create(n)
link.display()

# recursion reverse
# link.is_reverse(link.head)

# recursion palindrome
# a = link.is_palindrome(link.head,link.head)
# print(a)

# remove duplicates

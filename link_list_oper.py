
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
        
    def mergeSort(self,current):
        if current == None or current.next == None:
            return current
        prev = None
        slow = current
        fast = current
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        h1 = self.mergeSort(current)
        h2 = self.mergeSort(slow)
        return self.merge(h1,h2)
    def merge(self,h1,h2):
        if h1==None  or h2 == None:
            return  h1
        if h1.data < h2.data:
            h1.next = self.merge(h1.next,h2)
            return h1
        else:
            h2.next = self.merge(h1,h2.next)
            return h2
    def dispach(self,a):
        while True:
            if a==None:
                break
            print(a.data)
            a = a.next

        

s1 = Node(5)
s2 = Node(4) 
s3 = Node(3) 
s4 = Node(2) 
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
for i in range(9,0,-1):
    n = Node(i)
    link.create(n)
link.display()
print()
# recursion reverse
# link.is_reverse(link.head)

# recursion palindrome
# a = link.is_palindrome(link.head,link.head)
# print(a)

# merge sort linklist
a = link.mergeSort(link.head)
link.dispach(a)
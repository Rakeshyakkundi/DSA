class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkList:
    def __init__(self):
        self.head = None
    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastLink = self.head
            while lastLink.next != None:
                lastLink = lastLink.next
            lastLink.next = newNode
    def printl(self):
        while True:
            print(self.head.data,end="")
            self.head = self.head.next
            if self.head is None:
                break
    def M_N(self,M,N):
        self.M = M
        self.N = N
        self.temp = 0
        while True:
            if self.head.data == M:
                
                self.temp += 1
            self.head = self.head.next


s1 = Node(1);s2 = Node(2);s3 = Node(3);s4 = Node(4);s5 = Node(5);s6 = Node(6);s7 = Node(7);s8 = Node(8)
link = LinkList()
link.insert(s1);link.insert(s2);link.insert(s3);link.insert(s4)
link.insert(s5);link.insert(s6);link.insert(s7);link.insert(s8)
link.printl()
print("")


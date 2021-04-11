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
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def display(self):
        current = self.head
        while True:
            if current.next is  None:
                break
            print(current.data)
            current = current.next
        print(current.data)        

    def rearrange(self):
        even = LinkList()
        odd = LinkList()
        current = self.head
        even = current
        odd = current.next
        current = current.next
        current = current.next
        i=2
        while True:
            if i%2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            if current.next is None:
                print(even.data)
                break
            current = current.next
            i +=1
    def createLink(self,data):
        self.data = data
        n = Node(data)
        lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next =n
        


s0 = Node(0);s1 = Node(1);s2 = Node(2);s3 = Node(3);s4 = Node(4);s5 = Node(5);s6 = Node(6)
link = LinkList()
link.insert(s0);link.insert(s1);link.insert(s2);link.insert(s3);link.insert(s4);link.insert(s5);link.insert(s6)
# link.display()
# link.rearrange()
link.createLink(7)
link.createLink(8)
link.createLink(9)
# link.display()
link.rearrange()
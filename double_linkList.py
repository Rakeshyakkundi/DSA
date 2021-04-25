class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double:
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head == None:
            a = Node(data)
            a.prev = None
            self.head = a
        else:
            newNode = Node(data)
            curr = self.head
            while curr.next :
                curr = curr.next
            newNode.prev = curr
            newNode.next = None
            curr.next = newNode
    def preappend(self,data):
        pass
    def print(self):
        curr = self.head
        while curr.next:
            print(curr.data)
            curr = curr.next
        print(curr.data)
        
link = Double()
link.append(1)
link.append(2)
link.append(3)
link.append(4)

link.print()



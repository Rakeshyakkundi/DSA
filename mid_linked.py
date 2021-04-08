from typing import Counter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
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
    def create(self,data):
        n = Node(data)
        self.insert(n)
    def dirplay(self):
        current = self.head
        while True:
            print(current.data)
            if current.next is None:
                break
            current = current.next
    def mid_find(self):
        slow = self.head
        fast  = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def mid_del(self):
        slow = self.head
        fast = self.head
        prev = None
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next




s1 = Node(1)
link = LinkedList()
link.insert(s1)         
link.create(2)          
link.create(3)          
link.create(4)
link.create(5)
# for i in range(6,21):
#     link.create(i)          
# link.dirplay()
a = link.mid_find()
print("mid value :",a)
link.mid_del()
link.dirplay()



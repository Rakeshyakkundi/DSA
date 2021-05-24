from typing import Counter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.app = None
    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = node
    def display(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def line(self,node):
        i = 0
        while node != None:
            node = node.next
            i +=1
        return i

s1 = Node(3);s2 = Node(2)
s3 = Node(9);s4 = Node(5)
link = LinkList()
link.insert(s1);link.insert(s2)
link.insert(s3);link.insert(s4)
link.display()
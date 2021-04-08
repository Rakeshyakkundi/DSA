from typing import Counter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkNode:
    def __init__(self):
        self.head = None
    def insert(self,newNode):
        if self.head is None:
            self.head= newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printl(self):
        preLink = self.head
        print(preLink.data)
        while True:
            if preLink.next is None:
                break
            preLink = preLink.next
            print(preLink.data)
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

    def addNumber(self,num):
        temp = self.head.data + num;carry = 0
        while self.head.next != None:
            if temp >9:
                temp = str(temp)
                self.head.data = int(temp[len(temp)-1])
                carry = int(temp[len(temp)-2])

            else:
                self.head.data  += num
            self.head = self.head.next
        print(self.head.data)

s1 = Node(1)
s2 = Node(9)
s3 = Node(9)
s4 = Node(8)
link = LinkNode()
link.insert(s1);link.insert(s2);link.insert(s3);link.insert(s4)
link.reverse()
link.printl()
link.addNumber(1)
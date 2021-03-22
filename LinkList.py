from typing import Text


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
    def printl(self):
        currentNode = self.head
        if self.head is None:
                print("Link list is empty")
        else:            
            while True:
                print(currentNode.data)
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
    def insertHead(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
    def accendInsert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            if self.head.data >newNode.data:
                temp = self.head
                newNode.next = temp
                self.head = newNode
            elif self.head.data<newNode.data:
                self.head.next = newNode

    def deleteEndNode(self):
        temp = self.head
        while True:
            if temp.next.next is None:
                temp.next = None
                break
            temp = temp.next
    
    def delBetweenNode(self):
        temp = self.head
        temp = temp.next
        self.head.next = temp.next

class SortLinkList:
    def __init__(self,link1,link2):
        self.link1 = link1
        self.link2 = link2
    

    def insertL(self,newNodeA):
        sort1 = self.link1.head
        sort2 = self.link2.head
        while True:
            if sort1 is None:
                newNodeA.insert(sort2)
                break
            if  sort2 is None:
                newNodeA.insert(sort1)
                break
            if sort1.data<sort2.data:
                temp1 = sort1.next
                sort1.next = None
                newNodeA.insert(sort1)
                sort1 = temp1
            else:
                temp2 = sort2.next
                sort2.next = None
                newNodeA.insert(sort2)
                sort2 = temp2
        return newNodeA


            


# link = LinkList()
# first = Node(100)
# second = Node(50)
# third = Node(10)
# four = Node(1)
# link.accendInsert(first);link.accendInsert(second);link.accendInsert(third);link.accendInsert(four)
# link.printl()
# link.insert(first);link.insert(second);link.insert(third)

# print("Inserted list :")
# link.printl()

# link.deleteEndNode()
# link.printl()

# link.delBetweenNode()
# link.printl()

link1 = LinkList();link2 = LinkList()
f1 = Node(1);f2 = Node(3);f3 = Node(5)
f4 = Node(2);f5 = Node(4);f6 = Node(6)
link1.insert(f1);link1.insert(f2);link1.insert(f3)
link2.insert(f4);link2.insert(f5);link2.insert(f6)

link = SortLinkList(link1,link2)
newNodeA = LinkList()
a = link.insertL(newNodeA)
a.printl()
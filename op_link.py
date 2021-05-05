from typing import Counter


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkList:
    def __init__(self):
        self.head = None
    def multy(self,data):
        a = Node(data)
        lastNode = self.head
        if self.head is None:
            self.head = a
        else:
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = a
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
        while True:
            if current is None:
                break
            print(current.data)
            current = current.next
    def first_last(self):
        first = self.head
        last = self.head
        while last.next != None:
            last = last.next
        first.next = last
    def rev(self):
        prev = None
        current = self.head
        while current.next != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        next = current.next
        current.next = prev
        self.head = current
        
link = LinkList()
for i in range(10):
    link.multy(i)
# link.display()
link.rev()
link.display()
# link.first_last()
# print("first and last Node :")
# link.display()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class LinkList:
#     def __init__(self):
#         self.head = None
    
#     def insert(self,data):
#         a = Node(data)
#         if self.head is None:
#             self.head = a
#         else:
#             lastNode = self.head
#             while lastNode.next != None:
#                 lastNode = lastNode.next
#             a.prev = lastNode
#             lastNode.next = a
#     def display(self):
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next
#     def rev_print(self):
#         last = self.head
#         while last.next is not None:
#             last = last.next
#         while last is not None:
#             print(last.data)
#             last = last.prev

# link = LinkList()
# for i in range(10):
#     link.insert(i)
# # link.display()
# link.rev_print()
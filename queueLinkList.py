# from typing import List


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
    
#     def enqueue(self,data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#         else:
#             last = self.head
#             while last.next != None:
#                 last = last.next
#             last.next = node
#     def dequeue(self):
#         if self.head.next == None:
#             self.head = None
#         else:
#             self.head = self.head.next
#     def isEmpty(self):
#         if self.head is None:
#             return True
#         return False
#     def display(self):
#         current = self.head
#         while current != None:
#             print(current.data," ",end="")
#             current = current.next
#         print()
    
# queue = Queue()
# for i in range(10):
#     queue.enqueue(i)
# print("enqueue :",end="")
# queue.display()
# queue.dequeue()
# queue.dequeue()
# print("dequeue :",end="")
# queue.display()
# print(queue.isEmpty())

#   Created by Elshad Karimov on 30/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None




custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.peek())
print(custQueue)
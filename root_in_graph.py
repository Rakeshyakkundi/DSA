from typing import Counter, ValuesView
from itertools import chain

class Graph:

    def __init__(self,gdic=None):
        if gdic is None:
            self.gdic = {}
        self.gdic = gdic
    
    def addNone(self,vertices,edges):
        self.gdic[vertices].append(edges)
    
    def path(self,start,end):
        visit=[];que=[]
        visit.append(start)
        for i in self.gdic[start]:
            que.append(i)
        print("visit :",visit,"que :",que)
        while len(que)!=0:
            current = que.pop()
            visit.append(current)
            print("visit :",visit,"que :",que)
            if current == end:
                print("yes it there")
                return 0
            try:
                for i in self.gdic[current]:
                    que.append(i)
            except:
                print("current :",current)
                pass   
        print("not found")
        return 1
content = {
    "E":["F","A"],
    "F":["I"],
    "A":["C","D","B"],
    "B":["J"],
    "C":["G"],
    "G":["D","H"],
    }
graph = Graph(content)
print(graph.gdic)
print("E to J")
graph.path("A","J")
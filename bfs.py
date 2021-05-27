from typing import Counter


class Graph:
    def __init__(self,gdic=None):
        if gdic is None:
            self.gdic = {}
        self.gdic = gdic
    
    def add(self,vertex,edge):
        self.gdic[vertex].append(edge)
    
    def bfs(self,vertex):
        visited =[];que = []
        visited.append(vertex);que.append(vertex)
        while len(que) != 0:
            current = que.pop(0)
            print(current)
            for adj in self.gdic[current]:
                if adj not in visited:
                    visited.append(adj);que.append(adj)
    
graph = Graph({"a":["b","c"],"b":["a","d","e"],"c":["a","e"],"d":["b","e","f"],"e":["d","f"],"f":["d","e"]})
print(graph.gdic)
graph.bfs("a")
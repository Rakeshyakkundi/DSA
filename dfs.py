class Graph:
    def __init__(self,gdic=None):
        if gdic is None:
            self.gdic = {}
        self.gdic = gdic
    
    def add(self,vertex,edge):
        self.gdic[vertex].append(edge)
    
    def dfs(self,vertex):
        stc = []
        visited = []
        stc.append(vertex)
        visited.append(vertex)
        while len(stc)!=0:
            currrnt = stc.pop()
            print(currrnt)
            for adj in self.gdic[currrnt]:
                if adj not in visited:
                    visited.append(adj)
                    stc.append(adj)
            
graph = Graph({"a":["b","c"],"b":["a","d","e"],"c":["a","e"],"d":["b","e","f"],"e":["d","f"],"f":["d","e"]})
print(graph.gdic)
graph.dfs("a")
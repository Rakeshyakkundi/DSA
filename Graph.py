# graph consists of a finite set of vertices and a set of edges which connect a pair of nodes.
# graph   -> DIRECTED ->WEIGHTED       ->POSTIVE ->NEGATIVE
#                     ->UNWEIGHTED

#         -> UNDIRECTED ->WEIGHTED    ->POSTIVE ->NEGATIVE
#                       ->UNWEIGHTED
#   adjacency matrix
#   adjacency list

class Graph:
    def __init__(self,gdic=None):
        if gdic is None:
            gdic ={}
        self.gdic = gdic

    def addEdge(self,vertex,edge):
        self.gdic[vertex].append(edge)
    

dirc = {
    "a":["b","c","d"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["a","b","c"]
}
graph = Graph(dirc)
print(graph.gdic)
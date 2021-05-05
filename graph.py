#      Directed Graph
#       a----c 
#       |    | \
#       |    |  e
#       |    | /  
#       b----d
# 
#  vertices = a,b,c,d,e
#  edge = (a,c),(a,b),(b,d),(d,c)_ _ _ _ _ 
#  |V| = 5
#  |E| = 6
#  G = <V,E>

#      Undirected Graph
#      Weighted Graph
# 
#      Representation of Graph  
#      ->Adjacency List         
#      ->Adjacency Matrix 
   
#      Breadth first search
#      ->visit all nodes from source
#      ->avoid duplicates
#      ->visit the nodes in level order


adj_list = {
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

visited = {}
level = {}
parent = {}
bfs_travel_output = []
queue = []

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s]= 0
queue.append(s)

while len(queue) != 0:
    u = queue.pop(0)
    bfs_travel_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.append(v)
print(bfs_travel_output)
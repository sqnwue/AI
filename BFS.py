def bfs(graph,start,goal):
    visited=set()
    queue=[(0,start,[start])]
    while queue:
        cost,node,path=queue.pop(0)
        if node==goal:
            print(path,cost)
            return path,cost
        if node not in visited:
            visited.add(node)
            for n in graph.get(node,{}):
                if n not in path:
                    queue.append((cost+graph[node][n],n,path+[n]))
    return None

graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}

bfs(graph,'S','G')
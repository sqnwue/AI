def dfs(graph,start,goal):
    visited=set()
    stack=[(start,[start],0)]
    while stack:
        node,path,cost=stack.pop()
        if node==goal:
            print(path,cost)
            return path,cost
        if node not in visited:
            visited.add(node)
            for n in reversed(graph.get(node,{})):
                if n not in path:
                    stack.append((n,path+[n],cost+graph[node][n]))
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

dfs(graph,'S','G')
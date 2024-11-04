def oraclech(graph,start,goal,heur):
    paths=[]
    stack=[(start,[start],0)]
    while stack:
        node,path,cost=stack.pop()
        if node==goal:
            paths.append((path,cost))
        for n in graph.get(node,{}):
            if n not in path:
                stack.append((n,path+[n],cost+heur.get(n,0)))
    print(paths,cost)
    return paths,cost




graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}

heur={
    'S': float('inf'),
    'A': 7.5,
    'B': 6,
    'C': 7.5,
    'D': 5,
    'E': 4,
    'G': 0
}

oraclech(graph,'S','G',heur)
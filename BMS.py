def bms(graph,start,goal):
    paths=[]
    stack=[(start,[start])]
    while stack:
        node,path=stack.pop()
        if node==goal:
            paths.append(path)
        for n in graph.get(node,{}):
            if n not in path:
                stack.append((n,path+[n]))
    print(paths) 
    return paths


graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}

bms(graph,'S','G')


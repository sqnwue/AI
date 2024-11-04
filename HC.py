def HC(graph,start,goal,heur):
    visited=set()
    stack=[(start,[start])]
    while stack:
        node,path=stack.pop()
        if node==goal:
            print(path)
            return path
        if node not in visited:
            visited.add(node)
            ne=[(n,path+[n])for n in graph.get(node,{}) if n not in visited]
            ne.sort(key=lambda x:heur.get(x[0],float('inf')))
            for a,new in reversed(ne):
                stack.append((a,new))
            

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

HC(graph,'S','G',heur)
    
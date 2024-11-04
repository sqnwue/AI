def BS(graph,start,goal,heur,bw=2):
    stack=[(start,[start])]
    while stack:
        beam=[]
        stack=sorted(stack,key=lambda x:heur.get(x[0],float('inf')))[:bw]
        for node,path in stack:
            if node==goal:
                print(path)
                return path
            for n in graph.get(node,{}):
                if n not in path:
                    beam.append((n,path+[n]))
        stack=beam

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

BS(graph,'S','G',heur)
    
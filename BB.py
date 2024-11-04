def BB(graph,start,goal):
    bpath=None
    bcost=float('inf')
    queue=[(0,start,[start])]
    while queue:
        cost,node,path=queue.pop(0)
        if node==goal and cost<bcost:
            bcost=cost
            bpath=path
        for n in graph.get(node,{}):
            if n not in path:
                ncost=cost+graph[node][n]
                queue.append((ncost,n,path+[n]))
                queue.sort()
    print(bpath)
    return bpath
    

graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}

BB(graph,'S','G')
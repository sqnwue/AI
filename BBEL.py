def BBEL(graph,start,goal):
    bpath=None
    bcost=float('inf')
    queue=[(0,start,[start])]
    visited=set()
    while queue:
        cost,node,path=queue.pop(0)
        if node==goal and cost<bcost:
            bpath=path
            bcost=cost
        if node not in visited:
            visited.add(node)
            for n in graph.get(node,{}):
               ncost=cost+graph[node][n]
               queue.append((ncost,n,path+[n]))
               queue.sort()
    print(bpath)
    return(bpath)


graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}

BBEL(graph,'S','G')
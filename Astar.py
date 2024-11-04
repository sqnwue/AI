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
def Astar(graph,start,goal,heur):
   bpath=None
   bcost=24
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
          if n not in path:
             ncost=cost+graph[node][n]
             a=heur.get(n,0)
             queue.append((ncost+a,n,path+[n]))
             queue.sort()
   print(bcost,bpath)
   return bcost,bpath
               
        
Astar(graph,'S','G',heur)
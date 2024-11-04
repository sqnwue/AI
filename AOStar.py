graph={
    'S': {'A': 3, 'B': 5},
    'A': {'S': 3, 'B': 4, 'D': 3},
    'B': {'S': 5, 'A': 4, 'C': 4},
    'C': {'B': 4, 'E': 6},
    'D': {'A': 3, 'G': 5},
    'E': {'C': 6},
    'G': {'D': 5}
}
heur = {'S': float('inf'), 'A': 7.5, 'B': 6, 'C': 7.5, 'D': 5, 'E': 4, 'G': 0}

def AOstar(graph, start, goal, heur):
   paths={start:[start]}
   costs={start:0}
   while True:
      node=min(costs)
      if node==goal:
         print(paths[node],costs[node])
         return paths[node],costs[node]
      for n in graph.get(node,{}):
         if n not in paths:
            paths[n]=paths[node]+[n]
            costs[n]=costs[node]+graph[node][n]+heur.get(n,0)
      del costs[node]


AOstar(graph,'S','G',heur)
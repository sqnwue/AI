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
def Best(graph,start,goal,heur):
   queue=[(heur.get(start,0),start,[start])]
   visited=set()
   while queue:
      queue.sort()
      _,node,path=queue.pop()
      if node==goal:
         print(path)
         return path
      visited.add(node)
      for n in graph.get(node,{}):
         if n not in visited and all(n!=item[1] for item in queue):
            queue.append((heur.get(n,float('inf')),n,path+[n]))
   return None
               
        
Best(graph,'S','G',heur)
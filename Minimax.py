graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],  
    'E': [],
    'F': [],
    'G': []
}

evals = {
    'D': 3,  
    'E': 5,
    'F': 6,
    'G': 9
}

def minimax(node, depth, maximizing):
    if depth==0 or not graph[node]:
        return evals.get(node,0)
    
    if maximizing:
        max_eval=float('-inf')
        for child in graph[node]:
            eval=minimax(child,depth-1,False)
            max_eval=max(max_eval,eval)
        return max_eval
    
    else:
        min_eval=float('inf')
        for child in graph[node]:
            eval=minimax(child,depth-1,True)
            min_eval=min(min_eval,eval)
        return min_eval
    
a=minimax('A',3,maximizing=True)
print("Optimal minimax Cost: ",a)
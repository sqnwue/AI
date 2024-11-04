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

def alpha_beta(node, depth, alpha, beta, maximizing): #alpha=max and beta=min
    if depth==0 or not graph[node]:
        return evals.get(node,0)
    
    if maximizing:
        max_eval=float('-inf')
        for child in graph[node]:
            eval=alpha_beta(child,depth-1,alpha,beta,False)
            max_eval=max(max_eval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return max_eval
    
    else:
        min_eval=float('inf')
        for child in graph[node]:
            eval=alpha_beta(child,depth-1,alpha,beta,True)
            min_eval=min(min_eval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return min_eval

    
a=alpha_beta('A', depth=3, alpha=float('-inf'), beta=float('inf'), maximizing=True)
print("Optimal alpha-beta Cost: ",a)
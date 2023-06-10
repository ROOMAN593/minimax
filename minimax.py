  
from random_gametree import *
from minimax import *
n=0
def minimax(root):
    
    a = alpha_beta(root,-10,10,2)
    root.key = a
    return n

def alpha_beta(node, alpha, beta,c):
    if (len(node.neighbor) == 0):
        return node
    n=n+1

    if c%2 != 0:
         c=c+1
         for u in node.neighbor:
             beta = min(beta, alpha_beta(u.neighbor, alpha, beta,c))
             if beta <= alpha:
                
                 return beta
             return beta
    if c%2==0:
        c=c+1
        
        for u in node.neighbor:
            alpha = max(alpha,alpha_beta(u.neighbor, alpha, beta,c))
            if beta <= alpha:
            
                return alpha
            return alpha

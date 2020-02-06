import numpy as np
from numpy import linalg as la
def seidel(a, x ,b): 
    n = len(a)                    
    for j in range(0, n):         
        d = b[j]                   
          
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i]        
        x[j] = d / a[j][j]      
    return x     
                     
x = [0, 0, 0,0,0]                         
a = [[6.81, 1.12, 0.95, 1.165, -0.51],
     [1.08, 3.61, 1.3, -1.63, -0.18],
     [0.99, -2.46, 5.99, 2.1, 0.283],
     [1.135, 0.16, 2.1, 5.55, -2],
     [0.99, -0.48, -0.017, 1, 4]]
b = [2.1,0.6,0.43,5.52,-0.75]

error = np.dot(a, x) - b
print(la.norm(error)) 

while la.norm(error) > 0.0001:             
    x = seidel(a, x, b) 
    error = np.dot(a, x) - b
    print('error = ', la.norm(error))   

print(x)
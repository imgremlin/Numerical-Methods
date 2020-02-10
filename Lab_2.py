from __future__ import division
import numpy as np
import math
from numpy import linalg as la

def invert_matrix(A, I):
    n = len(A)
    AM = copy_matrix(A)
    IM = copy_matrix(I)
    indices = list(range(n)) 
    for fd in range(n): 
       
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(n): 
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = AM[i][fd]
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
            r=np.array(AM).dot(IM)
            b = np.array(IM)
            print_matrix('iter', IM)
            print('nevyazka =', la.norm(r-b)) 
            print(' ')
                       
    return IM
        

def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,5)+0 for x in row])
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

   # if colsA != rowsB:
   #     print('Number of A columns must equal number of B rows.')
     #   sys.exit()

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
    return MC

def det(A):
    n = len(A)
    AM = copy_matrix(A)
    
    for fd in range(n):
        for i in range(fd+1,n):
            if AM[fd][fd] == 0:
                AM[fd][fd] == 1.0e-18
        
            crScaler = AM[i][fd] / AM[fd][fd] 
            for j in range(n): 
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][i] 
 
    return product

A = [[6.81, 1.12, 0.95, 1.165, -0.51],
     [1.08, 3.61, 1.3, -1.63, -0.18],
     [0.99, -2.46, 5.99, 2.1, 0.283],
     [1.135, 0.16, 2.1, 5.55, -2],
     [0.99, -0.48, -0.017, 1, 4]]

B = [[2.1,0,0,0,0],
     [0.6,0,0,0,0,],
     [0.43,0,0,0,0],
     [5.52,0,0,0,0],
     [-0.75,0,0,0,0]]

I = [[1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1]]

print('Invert matrix of A:')
print(' ')
print_matrix('matrix A', A)
invert_matrix(A, I)
print_matrix('A * A^(-1)', matrix_multiply(A,invert_matrix(A, I)))
print(' ')
print('detA = ', det(A))
print(' ')
print('SLAR:')
print(' ')
print_matrix('Main matrix: ', A)  
print(' ')
print_matrix('right vector: ', B)   
invert_matrix(A, B)
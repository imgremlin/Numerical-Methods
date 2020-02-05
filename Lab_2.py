from __future__ import division
import numpy as np

def invert_matrix(A, tol=None):
    n = len(A)
    AM = copy_matrix(A)
    I = np.identity(n)
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
    return IM
        

def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x,3)+0 for x in row])
        
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
    return MC

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C   

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

A = [[6.81, 1.12, 0.95, 1.165, -0.51],
     [1.08, 3.61, 1.3, -1.63, -0.18],
     [0.99, -2.46, 5.99, 2.1, 0.283],
     [1.135, 0.16, 2.1, 5.55, -2],
     [0.99, -0.48, -0.017, 1, 4]]
B = [[2.1],[0.6],[0.43],[5.52],[-0.75]]
print('det A = ', round(getMatrixDeternminant(A) , 3))
#print(np.linalg.det(A))

AM = copy_matrix(A)
n = len(A)
BM = copy_matrix(B)

indices = list(range(n))
for fd in range(n):
    fdScaler = 1.0 / AM[fd][fd]

    for j in range(n): 
        AM[fd][j] *= fdScaler
    BM[fd][0] *= fdScaler
     

    for i in indices[0:fd] + indices[fd+1:]: 
        crScaler = AM[i][fd] 
        for j in range(n): 
            AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
        BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
        
print_matrix('AM', AM)      
print_matrix('BM', BM)  
print_matrix('Invert matrix ', invert_matrix(A))     
import math
import numpy as np

n=8
val1=3
val2=5
eps=0.0001

step=0.75

def func(x):
    return 3*( (x+1)/(x*x+1-2*x ) )**(1/3)

def err(x,y):
    return math.fabs(f(x)-y)

def d6(x):
    return (640 * ( (x+1)/( (x**2+1-2*x) **(1/3) ) ) * (x*(13*x*(x*(7*x*(x+3)*(x+15)+540)+405)+2430)+405) )/(243*(x*x-1)**6)

def dy(x):
    return (-x-3)/( ((x-1)**3)*( (x+1)/(x**2+1-2*x) )**(2/3) )

def ddy(x):
    return ( 4*(x**2+6*x+3) ) / ( (3*(x-1)**6) * ( (x+1)/(x**2+1-2*x) )**(5/3) )

def Lagrange(x):
    res=0
    for i in range(n):
        F = 1
        for j in range(n):
            if (i!=j): F*= ( x - vals[j] ) / ( vals[i] - vals[j] )
        res+=f[i]*F
    return res

def Newforward(x0):
    m = np.zeros((n,n))
    for i in range(n):
        m[i][0] = f[i]
    for j in range(1,n):
        for i in range(n-j):
            m[i][j] = (m[i+1][j-1] - m[i][j-1]) / (vals[j+i] - vals[i])
    res = f[0]
    for i in range(n-1):
        F=1
        for j in range(i+1):
            F *= (x0 - vals[j])
            res += F*m[0][i+1]
    return res
            
def Newbackward(x0):
    m = np.zeros((n,n))
    for i in range(n):
        m[i][0] = f[i]
    for j in range(1,n):
        for i in range(n-j):
            m[i][j] = (m[i+1][j-1] - m[i][j-1]) / (vals[j+i] - vals[i])
    res = f[n-1]
    for i in range(n-1,0,-1):
        F=1
        for j in range(n-1,i-1,-1):
            F *= (x0 - vals[j])
            res += F*m[i-1][n-i]
    return res

def Spline(x0, A, move):
    i = n + 1
    z=0
    while (x0 < vals[i-3]):
        i=i-1
    z = z+A[i]*((x0-vals[i-3])/move)**3/6/move
    z = z+A[i-1]*(((vals[i-2]-x0)/move)**3/2/move - ((vals[i-2]-x0)/move)**2/move + 2.0/3/move)
    z = z+A[i-2]*(((x0-vals[i-3])/move)**3/2/move - ((x0-vals[i-3])/move)**2/move + 2.0/3/move)
    z = z+A[i-3]*(((vals[i-2]-x0)/move)**3)/6/move
    return z

def Spl(f, A, move):
    A[1] = f[0]*move - ddy(vals[0])*move**3/6
    A[2] = dy(vals[0])*move**2 + f[0]*3*move - 2*A[1]
    A[0] = A[2] - dy(vals[0])*2*move**2
    for i in range(3,n+2):
        A[i] = f[i-2]*6*move - A[i-2] - 4*A[i-1]
    

move = (val2 - val1) / (val1 - 1)
f = np.zeros(n)
vals = np.zeros(n)
for i in range(n):
    vals[i] = val1 + move*i
    f[i] = func(vals[i])
    print('x{} = {}, f = {}'.format(i, vals[i], f[i]))
print ('lagrange:')
for xi in np.arange(val1, val2+move/5, move/5):
    print('x = {}, lagrange = {}'.format(round(xi,1), Lagrange(xi)))

print ('newton forward: ')
for xi in np.arange(val1, val2+move/5, move/5):
    print('x = {}, newton forward = {}'.format(round(xi,1), Newforward(xi)))
print ('newton backward: ')
for xi in np.arange(val1, val2+move/5, move/5):
    print('x = {}, newton backward = {}'.format(round(xi,1), Newbackward(xi)))
    
print ('spline method: ')
A = np.zeros(n+3)
Spl(f, A, move)
for xi in np.arange(val1, val2+move/5, move/5):
    print('x = {}, spline = {}'.format(round(xi,1), Spline(xi, A, move)))

for xi in np.arange(val1, val2+move/5, move/5):
    yi=func(xi)
    w=1
    for i in range(n):
        w*=(xi-vals[i])
    print('x = {}\nNf-f = {}\nNb-f = {}\nLagr-f = {}\nSpl-f = {}\nMajor = {}\n'.format(round(xi,1), math.fabs(Newforward(xi)-yi), math.fabs(Newbackward(xi)-yi), math.fabs(Lagrange(xi)-yi), math.fabs(Spline(xi,A,move)-yi), math.fabs(d6(xi)*w)/720))    

from numpy import linalg as la
import math

e = 0.001
d = 0.691
B = -0.789
a = 0.312
c = 1.975
b = -0.283
d = 0.281

def x_k_1(y):
     return d - math.sin(y+B)
     
def y_k_1(x):
     return (c - math.cos(x+a))/b
     
def funk_2(x, y):
    return x + math.sin(y+B) - d

def funk_1(x, y):
    return math.cos(x+a) + b*y - c

def simple_iterations(x_k, y_k):
    dx = dy = 1
    f1 = funk_1(x_k, y_k)
    f2 = funk_2(x_k, y_k)
    i=0
     
    while la.norm([f1, f2]) > e or la.norm([dx, dy]) > e:
        i=i+1
        y_k1 = y_k_1(x_k)
        x_k1 = x_k_1(y_k)
        print('x_k1 = ', x_k1, 'y_k1 = ', y_k1)
        dx = x_k1 - x_k
        dy = y_k1 - y_k
        print('norm dx dy =', la.norm([dx, dy]))
        f1 = funk_1(x_k1, y_k1)
        f2 = funk_2(x_k1, y_k1)
        x_k = x_k1
        y_k = y_k1
        print('norm f1 f2 =', la.norm([f1, f2]))  
        print(i)
        
    print('res: x = ', round(x_k1, 4), 'y =', round(y_k1, 4))
     
#print(simple_iterations(-0.69, -3.7))
#print(simple_iterations(1.2, -7))
#print(simple_iterations(1, -6))
    
def det(x, y):
    return (2*y*(math.cos(x+y) + c) - 2*x*(math.cos(x+y)))
    
def funkn_1(x, y):
    return (x*c + math.sin(y+x) - d)

def funkn_2(x, y):
    return (x*x + y*y - 1)

def xn_k_1(x, y):
    return (2*y*funkn_1(x, y) - (math.cos(x+y)) * funkn_2(x,y) )/det(x, y)

def yn_k_1(x, y):
    return (-2*x*funkn_1(x, y) + (math.cos(x+y) + c) * funkn_2(x,y) )/det(x, y)

def newton(x_k, y_k):
    dx = dy = 1
    f1 = funkn_1(x_k, y_k)
    f2 = funkn_2(x_k, y_k)
    i=0
     
    while la.norm([f1, f2]) > e or la.norm([dx, dy]) > e:
        i=i+1
        y_k1 = yn_k_1(x_k, y_k)
        x_k1 = xn_k_1(x_k, y_k)
        print('x_k1 = ', x_k1, 'y_k1 = ', y_k1)
        dx = x_k1 - x_k
        dy = y_k1 - y_k
        print('norm dx dy =', la.norm([dx, dy]))
        f1 = funkn_1(x_k1, y_k1)
        f2 = funkn_2(x_k1, y_k1)
        x_k = x_k1
        y_k = y_k1
        print('norm f1 f2 =', la.norm([f1, f2]))  
        print(i)
        
    print('res: x = ', round(x_k1, 4), 'y =', round(y_k1, 4))

#print(newton(-0.25, 0.967))
#print(b, B)



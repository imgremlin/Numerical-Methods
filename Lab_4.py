import math
from numpy import linalg as la

e = 0.001
A = 0.455
B = -0.288
a = 0.498
b = 1.488
c = 0.352
d = 0.796

def xk_1(y):
    return d-math.cos(y+B)

def yk_1(x):
    return (-math.sin(x+A)+c)/b

def func1(x,y):
    return math.sin(x+A)+b*y-c

def func2(x,y):
    return x+math.cos(y+B)-d

def simple_iteration(xk, yk):
    iter=1
    f1=func1(xk, yk)
    f2=func2(xk, yk)
    print('iteration №', iter)
    print("(x, y) = ({}, {})".format(xk, yk))
    print("(f1, f2) = ({}, {})".format(f1, f2))
    print("norm(f1,f2) = {}".format(la.norm([f1,f2])))
    
    while True:
        
        iter+=1
        x1=xk_1(yk)
        y1=yk_1(xk)
        dx=x1-xk
        dy=y1-yk
        f1=func1(x1, y1)
        f2=func2(x1, y1)
        print()
        print('iteration №', iter)
        print("(x, y) = ({}, {})".format(xk, yk))
        print("(f1, f2) = ({}, {})".format(f1, f2))
        print("norm(f1,f2) = {}".format(la.norm([f1,f2])))
        xk=x1
        yk=y1

        if la.norm([f1,f2])<e and la.norm([dx,dy])<e:
            print("result: (x, y) = ({}, {})".format(x1, y1))
            break
        
def det(x,y):
    return (2*b*y*y-2*a*x*x)/(math.cos(x*y+A)*math.cos(x*y+A))-4*b*x*y

def fun1(x,y):
    return math.tan(x*y+A)-x*x

def fun2(x,y):
    return a*x*x+b*y*y-1

def xn_1(x,y):
    return x-(2*b*y*fun1(x,y)-x*fun2(x,y)/(math.cos(x*y+A)*math.cos(x*y+A)))/det(x,y)       

def yn_1(x,y):
    return y-(-2*a*x*fun1(x,y)+(y/(math.cos(x*y+A)*math.cos(x*y+A))-2*x)*fun2(x,y))/det(x,y)

def newton_method(xk,yk):
    iter=1
    f1=fun1(xk, yk)
    f2=fun2(xk, yk)    
    print()
    print('iteration №', iter)
    print("(x, y) = ({}, {})".format(xk, yk))
    print("(f1, f2) = ({}, {})".format(f1, f2))
    print("norm(f1,f2) = {}".format(la.norm([f1,f2])))
    
    while True:
        iter+=1
        x1=xn_1(xk,yk)
        y1=yn_1(xk,yk)
        dx=x1-xk
        dy=y1-yk
        f1=fun1(x1, y1)
        f2=fun2(x1, y1)
        print()
        print('iteration №', iter)
        print("(x, y) = ({}, {})".format(xk, yk))
        print("(f1, f2) = ({}, {})".format(f1, f2))
        print("norm(f1,f2) = {}".format(la.norm([f1,f2])))
        xk=x1
        yk=y1

        if la.norm([f1,f2])<e and la.norm([dx,dy])<e:
            print("result: (x, y) = ({}, {})".format(x1, y1))
            break
    
    
    
print("simple iterations:")
print()    
simple_iteration(-0.17,0.05)
print()    

print("newton method n1:")         
newton_method(-0.4,-0.78)
print()    

print("newton method n2:")  
newton_method(-1.21,-0.42)
print()    

print("newton method n3:")  
newton_method(0.38,-0.79)
print()    

print("newton method n4:")  
newton_method(1.2,0.43)

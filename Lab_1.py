import math

func_glob =  lambda x: 6*x**5 - 3* x**4 - x**3 + 9
func_first = lambda x: 30 * x**4 - 12 * x**3 -3* x**2
a = -2; b = -0.2; e = 1e-05

def secant_method(a, b, f):
        y1 = f(a)
        y2 = f(b)
        if y1 * y2 >= 0:
            print ('no roots')
        else:
            c = (y2*a - y1*b)/(y2 - y1);
            y3 = f(c)
            while (abs(y3) > e) or math.fabs(b - a) > e:
                print('a=',a,'b=',b,'f(a)=',f(a), 'f(b)=',f(b))
                c = (y2*a - y1*b)/(y2 - y1);
                y3 = f(c)
                if y1 * y3 < 0:
                    b = c
                else:
                    a = c               
            return c

def half_divide_method(a, b, f):
    x = (a + b) / 2
    while math.fabs(f(x)) >= e or math.fabs(b-a)>e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
        print('a=',a,'b=',b,'f(a)=',f(a), 'f(b)=',f(b))
    return (a + b) / 2

def newtons_method(a, b, f, f1):
    x0 = (a + b) / 2
    x1 = x0 - (f(x0) / f1(x0))
    while True:
        if math.fabs(x1 - x0) < e or math.fabs(f(x1))<e: return x1
        x0 = x1
        x1 = x0 - (f(x0) / f1(x0))
        print('x1 =', x1, 'f(x1)=', f(x1))
        
print('half_divide method:')
print ('result:', half_divide_method(a, b, func_glob))
print(' ')
print('newtons method:')
print ('result:', newtons_method(a, b, func_glob, func_first))
print(' ')
print('secant method:')
print ('result:', secant_method(a, b, func_glob))
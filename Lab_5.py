import matplotlib.pyplot as plt

N = 10
a = 2
b = 6

def polinom (x):
    return 3*( (x+1)/(x*x+1-2*x ) )**(1/3)

def deriv_2(x):
    return ( 4*(x**2+6*x+3) ) / ( (3*(x-1)**6) * ( (x+1)/(x**2+1-2*x) )**(5/3) )

def deriv_6(x):
    return (640 * ( (x+1)/( (x**2+1-2*x) **(1/3) ) ) * (x*(13*x*(x*(7*x*(x+3)*(x+15)+540)+405)+2430)+405) )/(243*(x*x-1)**6)

def newton (x, xi): 
    s = polinom(xi[0])
    for i in range(1, len(xi)):
        F = 0
        for j in range (i+1):
            z = 1.0
            for k  in range (i+1):
                if (k!=j):
                    z = z * (xi[j]- xi[k])
            F =  F + polinom(xi[j])/z

        for k in range (i):
            F = F * (x - xi[k])

        s = s + F
    return s

def lagrange (x, xi):
    s = 0 
    for i in range (len(xi)):
        w = 1.0
        for j in range (len(xi)):
            if (i!=j):
                w = w * (x - xi[j])/(xi[i] - xi[j])
        s  = s + w * polinom(xi[i])
    return s

def majoranta(t, a, b, xi):
    if (a>=b):
        a, b = b, a
    if (a>0):
        sup = abs(deriv_6(a))
    elif (a<0):
        sup = abs(deriv_6(b))
    w = 1.0
    for i in range(len(xi)):
    	w = w*(t-xi[i])
    return (sup/120)*abs(w)

def spline(t, x, d2f):
    h = []; l = []; dlt = []; lmb = []
    a = []; b = []; c = []; d = []; y = []
    for i in range(0, N):
        y.append(polinom(x[i]))
        h.append(0); l.append(0); dlt.append(0); lmb.append(0)
        a.append(y[i]); b.append(0); c.append(0); d.append(0)
    
    for k in range(1, N):
        h[k] = x[k] - x[k-1]
        l[k] = (y[k] - y[k-1])/h[k]

    dlt[1] = -h[2]/(2*(h[1] + h[2]))
    lmb[1] = 1.5*(l[2] - l[1])/(h[1] + h[2])

    for k in range(3, N):
        dlt[k-1] = -h[k]/(2*h[k-1] + 2*h[k] + h[k-1]*dlt[k-2])
        lmb[k-1] = (3*l[k] - 3*l[k-1] - h[k-1]*lmb[k-2])/(2*h[k-1] + 2*h[k] + h[k-1]*dlt[k-2])

    c[0] = d2f(x[0])/2; c[N-1] = d2f(x[-1])/2
    for k in range(N-1, 1, -1):
        c[k-1] = dlt[k-1]*c[k] + lmb[k-1]
    for k in range(1, N):
        d[k] = (c[k] - c[k-1])/(3*h[k])
        b[k] = l[k] + (2*c[k]*h[k] + h[k]*c[k-1])/3

    res = 0.0
    for k in range(1, N):
        if (x[k-1]<=t<=x[k]):
            res = a[k] + b[k]*(t-x[k]) + c[k]*(t-x[k])**2 + d[k]*(t-x[k])**3
    return res

if __name__ == "__main__":
    xi = []; xr = []; yi = []
    for i in range (N):
        xi.append(i+2)
    xi.reverse(); xr.extend(xi); xi.reverse()
    
    x = xi[0]
    dx = 0.01
    domain = []
    while not (x >= N+dx):
        domain.append(x)
        x = round(x + dx, 2)
    for i in range (len(domain)):
        yi.append(polinom(domain[i]))
    y_l, y_n, y_nb, y_m, y_s = [], [], [], [], []
    for i in range (len(domain)):
        y_l.append(lagrange(domain[i], xi))
        y_n.append(newton(domain[i], xi))
        y_nb.append(newton(domain[i], xr))
        y_m.append(majoranta(domain[i], a, b, xi))
        y_s.append(spline(domain[i], xi, deriv_2))

    y_l_f, y_n_f, y_nb_f, y_s_f,  = [], [], [], []
    for i in range(len(domain)):
        y_l_f.append(abs(y_l[i]-yi[i]))
        y_n_f.append(abs(y_n[i]-yi[i]))
        y_nb_f.append(abs(y_nb[i]-yi[i]))
        y_s_f.append(abs(y_s[i] - yi[i]))

    fig, axes = plt.subplots(1, figsize = (8,5))
    axes.plot(domain, y_l_f, 'g', label='Lagrange')
    axes.plot(domain, y_n_f, 'b', label='Newton')
    axes.plot(domain,y_nb_f, 'y', label='Newton Back')
    axes.plot(domain, y_s_f, 'm', label='Spline')
    axes.legend(loc=1)
    plt.show()

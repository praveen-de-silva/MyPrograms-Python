# ===============
# Differentiation
# ===============

import sympy as sp

##def y(x):
##    return x**3 + x**2
##
##def dydx(x):
##    dx = 1e-10
##    dydx_val = (y(x+dx)- y(x)) / dx
##    return dydx_val
##
##x = 1.23
##print(f'y = {y(x)}\ndydx = {dydx(x):.2f}')


# -------------------------
# Method 02 : sympy.library
# -------------------------

x = sp.Symbol('x')
y = x**3 + x**2

dydx = sp.diff(y, x)
##print(dydx)

def f(x):
    return x**3 + x**2

def f1(x_val):
    global x,y
    dydx = sp.diff(y, x)
    dydx_at_x = dydx.subs(x, 1.23)
    return dydx_at_x

    
print(f(1.23), f1(1.23))

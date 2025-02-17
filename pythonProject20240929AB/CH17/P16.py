import sympy as sp
import numpy as np
x=sp.Symbol('x')
y=sp.Symbol('y')
f1=2*x+3*y-23
f2=x+4*y-24
print(sp.solve([f1,f2],[x,y]))

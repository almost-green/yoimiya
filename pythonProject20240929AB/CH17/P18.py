import sympy as sp
x=sp.Symbol('x')
y=sp.Symbol('y')
f1=x+y-20
f2=50*x+30*y-800
print(sp.solve([f1,f2],[x,y]))

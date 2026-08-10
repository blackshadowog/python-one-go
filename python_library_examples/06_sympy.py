import sympy as sp

x = sp.symbols("x")
equation = x**2 - 5*x + 6
print(sp.solve(equation, x))

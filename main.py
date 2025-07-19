from minisym_ast import Number, Symbol, Add, Mul
from simplify import simplify

x = Symbol('x')
expr = Add(Mul(Number(2), x), Mul(Number(3), x))  # Represents 2*x + 3*x

simplified = simplify(expr)
print(simplified)

from ast import Number, Symbol, Add, Mul

x = Symbol("x")
expr = Add(Mul(Number(2), x), Mul(Number(3), x))

print(expr)  # Will print something like <__main__.Add object...>

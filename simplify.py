from minisym_ast import Number, Symbol, Add, Mul

def simplify(expr):
    if isinstance(expr, Add):
        left = simplify(expr.left)
        right = simplify(expr.right)
        if isinstance(left, Number) and isinstance(right, Number):
            return Number(left.value + right.value)
        return Add(left, right)
    elif isinstance(expr, Mul):
        left = simplify(expr.left)
        right = simplify(expr.right)
        if isinstance(left, Number) and isinstance(right, Number):
            return Number(left.value * right.value)
        return Mul(left, right)
    else:
        return expr

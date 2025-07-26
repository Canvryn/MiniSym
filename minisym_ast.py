class Expr:
    pass

class Number(Expr):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Symbol(Expr):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"({self.left} + {self.right})"

class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"({self.left} * {self.right})"

class Pow(Expr):
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp
    def __str__(self):
        return f"({self.base} ** {self.exp})"
class Number(Expr):
    # ... existing code ...
    def __repr__(self):
        return f"Number({self.value})"

class Symbol(Expr):
    # ... existing code ...
    def __repr__(self):
        return f"Symbol('{self.name}')"

# Do the same for Add, Mul, Pow

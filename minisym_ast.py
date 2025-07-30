class Expr:
    pass

class Number(Expr):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return f"Number({self.value})"
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        return False

class Symbol(Expr):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return f"Symbol('{self.name}')"
    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.name == other.name
        return False

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"({self.left} + {self.right})"
    def __repr__(self):
        return f"Add({repr(self.left)}, {repr(self.right)})"
    def __eq__(self, other):
        if isinstance(other, Add):
            return self.left == other.left and self.right == other.right
        return False

class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"({self.left} * {self.right})"
    def __repr__(self):
        return f"Mul({repr(self.left)}, {repr(self.right)})"
    def __eq__(self, other):
        if isinstance(other, Mul):
            return self.left == other.left and self.right == other.right
        return False

class Pow(Expr):
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp
    def __str__(self):
        return f"({self.base} ** {self.exp})"
    def __repr__(self):
        return f"Pow({repr(self.base)}, {repr(self.exp)})"
    def __eq__(self, other):
        if isinstance(other, Pow):
            return self.base == other.base and self.exp == other.exp
        return False

# Python operator overloads for basic math operations
def __add__(self, other):
    if isinstance(other, (int, float)):
        other = Number(other)
    return Add(self, other)

def __mul__(self, other):
    if isinstance(other, (int, float)):
        other = Number(other)
    return Mul(self, other)

def __pow__(self, other):
    if isinstance(other, (int, float)):
        other = Number(other)
    return Pow(self, other)

# Add operator overloads to all expression classes
Expr.__add__ = __add__
Expr.__mul__ = __mul__
Expr.__pow__ = __pow__

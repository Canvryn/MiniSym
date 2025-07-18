class Expr: pass

class Number(Expr):
    def __init__(self, value):
        self.value = value

class Symbol(Expr):
    def __init__(self, name):
        self.name = name

class Add(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Mul(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

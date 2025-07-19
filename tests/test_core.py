import unittest
from minisym_ast import Number, Symbol, Add, Mul
from simplify import simplify

class TestSimplify(unittest.TestCase):
    def test_simplify_add(self):
        x = Symbol('x')
        expr = Add(Mul(Number(2), x), Mul(Number(3), x))
        simplified = simplify(expr)
        self.assertEqual(str(simplified), "((2 * x) + (3 * x))")  # Adjust expected output as needed

if __name__ == '__main__':
    unittest.main()  

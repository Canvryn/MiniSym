#!/usr/bin/env python3
"""
Test file for Phase 1: Core Expression Engine
Tests AST construction, string representation, equality, and operator overloads.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow

def test_basic_construction():
    """Test basic AST construction and string representation."""
    print("Testing basic construction...")
    
    # Test Number
    n = Number(42)
    assert str(n) == "42"
    assert repr(n) == "Number(42)"
    
    # Test Symbol
    x = Symbol('x')
    assert str(x) == "x"
    assert repr(x) == "Symbol('x')"
    
    # Test Add
    expr = Add(x, n)
    assert str(expr) == "(x + 42)"
    assert repr(expr) == "Add(Symbol('x'), Number(42))"
    
    # Test Mul
    expr = Mul(x, n)
    assert str(expr) == "(x * 42)"
    assert repr(expr) == "Mul(Symbol('x'), Number(42))"
    
    # Test Pow
    expr = Pow(x, n)
    assert str(expr) == "(x ** 42)"
    assert repr(expr) == "Pow(Symbol('x'), Number(42))"
    
    print("✓ Basic construction tests passed!")

def test_equality():
    """Test structural equality comparison."""
    print("Testing equality...")
    
    x = Symbol('x')
    y = Symbol('y')
    n1 = Number(5)
    n2 = Number(5)
    n3 = Number(6)
    
    # Test Number equality
    assert n1 == n2
    assert n1 != n3
    assert n1 != x
    
    # Test Symbol equality
    assert x == Symbol('x')
    assert x != y
    
    # Test Add equality
    expr1 = Add(x, n1)
    expr2 = Add(x, n2)
    expr3 = Add(y, n1)
    assert expr1 == expr2
    assert expr1 != expr3
    
    # Test Mul equality
    expr1 = Mul(x, n1)
    expr2 = Mul(x, n2)
    expr3 = Mul(y, n1)
    assert expr1 == expr2
    assert expr1 != expr3
    
    # Test Pow equality
    expr1 = Pow(x, n1)
    expr2 = Pow(x, n2)
    expr3 = Pow(y, n1)
    assert expr1 == expr2
    assert expr1 != expr3
    
    print("✓ Equality tests passed!")

def test_operator_overloads():
    """Test Python operator overloads."""
    print("Testing operator overloads...")
    
    x = Symbol('x')
    y = Symbol('y')
    
    # Test addition
    expr = x + y
    assert isinstance(expr, Add)
    assert expr.left == x
    assert expr.right == y
    
    # Test addition with numbers
    expr = x + 5
    assert isinstance(expr, Add)
    assert expr.left == x
    assert isinstance(expr.right, Number)
    assert expr.right.value == 5
    
    # Test multiplication
    expr = x * y
    assert isinstance(expr, Mul)
    assert expr.left == x
    assert expr.right == y
    
    # Test multiplication with numbers
    expr = x * 3
    assert isinstance(expr, Mul)
    assert expr.left == x
    assert isinstance(expr.right, Number)
    assert expr.right.value == 3
    
    # Test power
    expr = x ** y
    assert isinstance(expr, Pow)
    assert expr.base == x
    assert expr.exp == y
    
    # Test power with numbers
    expr = x ** 2
    assert isinstance(expr, Pow)
    assert expr.base == x
    assert isinstance(expr.exp, Number)
    assert expr.exp.value == 2
    
    print("✓ Operator overload tests passed!")

def test_complex_expressions():
    """Test more complex expressions using operators."""
    print("Testing complex expressions...")
    
    x = Symbol('x')
    y = Symbol('y')
    
    # Test nested expressions
    expr = x + y * 2
    assert str(expr) == "(x + (y * 2))"
    
    expr = (x + y) * 2
    assert str(expr) == "((x + y) * 2)"
    
    expr = x ** 2 + y ** 2
    assert str(expr) == "((x ** 2) + (y ** 2))"
    
    print("✓ Complex expression tests passed!")

if __name__ == "__main__":
    print("🧪 Running Phase 1 Tests...\n")
    
    test_basic_construction()
    test_equality()
    test_operator_overloads()
    test_complex_expressions()
    
    print("\n🎉 All Phase 1 tests passed! Your core expression engine is working correctly.")
    print("\nNext steps:")
    print("1. Phase 2: Implement the parser to convert strings to ASTs")
    print("2. Phase 3: Build the simplification engine")
    print("3. Phase 4: Add algebraic manipulations (expand, factor)")
    print("4. Phase 5: Implement symbolic differentiation") 
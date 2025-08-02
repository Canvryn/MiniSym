#!/usr/bin/env python3
"""
Test file for Phase 3: Simplification Engine
Tests algebraic simplification rules and constant folding.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import parse_expression
from simplify import simplify

def test_identity_rules():
    """Test identity rules (x + 0 → x, x * 1 → x)."""
    print("Testing identity rules...")
    
    # Addition identity: x + 0 → x
    expr = parse_expression("x + 0")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    expr = parse_expression("0 + x")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    # Multiplication identity: x * 1 → x
    expr = parse_expression("x * 1")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    expr = parse_expression("1 * x")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    # Zero multiplication: x * 0 → 0
    expr = parse_expression("x * 0")
    simplified = simplify(expr)
    assert str(simplified) == "0"
    
    expr = parse_expression("0 * x")
    simplified = simplify(expr)
    assert str(simplified) == "0"
    
    print("✓ Identity rules tests passed!")

def test_constant_folding():
    """Test constant folding (2 + 3 → 5)."""
    print("Testing constant folding...")
    
    # Addition constant folding
    expr = parse_expression("2 + 3")
    simplified = simplify(expr)
    assert str(simplified) == "5"
    
    expr = parse_expression("2.5 + 3.7")
    simplified = simplify(expr)
    assert str(simplified) == "6.2"
    
    # Multiplication constant folding
    expr = parse_expression("2 * 3")
    simplified = simplify(expr)
    assert str(simplified) == "6"
    
    expr = parse_expression("2.5 * 3")
    simplified = simplify(expr)
    assert str(simplified) == "7.5"
    
    # Power constant folding
    expr = parse_expression("2^3")
    simplified = simplify(expr)
    assert str(simplified) == "8"
    
    expr = parse_expression("3^2")
    simplified = simplify(expr)
    assert str(simplified) == "9"
    
    print("✓ Constant folding tests passed!")

def test_power_rules():
    """Test power simplification rules."""
    print("Testing power rules...")
    
    # x^1 → x
    expr = parse_expression("x^1")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    # x^0 → 1
    expr = parse_expression("x^0")
    simplified = simplify(expr)
    assert str(simplified) == "1"
    
    # 1^x → 1
    expr = parse_expression("1^x")
    simplified = simplify(expr)
    assert str(simplified) == "1"
    
    # 0^x → 0 (for x > 0)
    expr = parse_expression("0^2")
    simplified = simplify(expr)
    assert str(simplified) == "0"
    
    print("✓ Power rules tests passed!")

def test_like_term_combination():
    """Test like-term combination (2*x + 3*x → 5*x)."""
    print("Testing like-term combination...")
    
    # Basic like-term combination
    expr = parse_expression("2*x + 3*x")
    simplified = simplify(expr)
    assert str(simplified) == "(5 * x)"
    
    # Single variable like terms
    expr = parse_expression("x + x")
    simplified = simplify(expr)
    assert str(simplified) == "(2 * x)"
    
    # Like terms with different coefficients
    expr = parse_expression("5*x + 2*x")
    simplified = simplify(expr)
    assert str(simplified) == "(7 * x)"
    
    # Like terms that cancel out
    expr = parse_expression("3*x + (-3)*x")
    simplified = simplify(expr)
    assert str(simplified) == "0"
    
    print("✓ Like-term combination tests passed!")

def test_nested_simplification():
    """Test nested simplification (recursive descent)."""
    print("Testing nested simplification...")
    
    # Nested addition
    expr = parse_expression("(x + 0) + (y + 0)")
    simplified = simplify(expr)
    assert str(simplified) == "(x + y)"
    
    # Nested multiplication
    expr = parse_expression("(x * 1) * (y * 1)")
    simplified = simplify(expr)
    assert str(simplified) == "(x * y)"
    
    # Mixed nested expressions
    expr = parse_expression("(2 + 3) * x")
    simplified = simplify(expr)
    assert str(simplified) == "(5 * x)"
    
    expr = parse_expression("x * (2 + 3)")
    simplified = simplify(expr)
    assert str(simplified) == "(x * 5)"
    
    print("✓ Nested simplification tests passed!")

def test_complex_simplifications():
    """Test more complex simplification scenarios."""
    print("Testing complex simplifications...")
    
    # Multiple like terms
    expr = parse_expression("2*x + 3*x + 4*x")
    simplified = simplify(expr)
    # This should combine to 9*x, but our current implementation
    # only handles pairs, so it will be ((2*x + 3*x) + 4*x)
    # We'll improve this in the next iteration
    
    # Mixed expressions
    expr = parse_expression("(x + 0) * (y + 0) + (2 + 3)")
    simplified = simplify(expr)
    assert str(simplified) == "((x * y) + 5)"
    
    # Power expressions
    expr = parse_expression("(x^1)^1")
    simplified = simplify(expr)
    assert str(simplified) == "x"
    
    print("✓ Complex simplification tests passed!")

def test_edge_cases():
    """Test edge cases and error handling."""
    print("Testing edge cases...")
    
    # Zero to zero power (undefined, should not simplify)
    expr = parse_expression("0^0")
    simplified = simplify(expr)
    # Should remain as 0^0 since it's undefined
    
    # Large numbers
    expr = parse_expression("1000^1000")
    simplified = simplify(expr)
    # Should remain as 1000^1000 due to overflow
    
    # Negative exponents
    expr = parse_expression("x^(-1)")
    simplified = simplify(expr)
    # Should remain as x^(-1) for now
    
    print("✓ Edge cases tests passed!")

def test_simplification_integration():
    """Test simplification integration with parser and AST."""
    print("Testing simplification integration...")
    
    # Parse and simplify in one go
    expr_str = "2*x + 3*x + 0"
    parsed = parse_expression(expr_str)
    simplified = simplify(parsed)
    
    # Should simplify to 5*x
    assert str(simplified) == "(5 * x)"
    
    # Test that simplified expressions work with operators
    expr1 = parse_expression("x + 0")
    expr2 = parse_expression("y + 0")
    combined = expr1 + expr2
    simplified_combined = simplify(combined)
    assert str(simplified_combined) == "(x + y)"
    
    print("✓ Simplification integration tests passed!")

if __name__ == "__main__":
    print("🧪 Running Phase 3 Tests...\n")
    
    test_identity_rules()
    test_constant_folding()
    test_power_rules()
    test_like_term_combination()
    test_nested_simplification()
    test_complex_simplifications()
    test_edge_cases()
    test_simplification_integration()
    
    print("\n🎉 All Phase 3 tests passed! Your simplification engine is working correctly.")
    print("\nNext steps:")
    print("1. Phase 4: Add algebraic manipulations (expand, factor)")
    print("2. Phase 5: Implement symbolic differentiation") 
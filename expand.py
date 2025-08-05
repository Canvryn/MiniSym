#!/usr/bin/env python3
"""
Expansion Engine for MiniSym - Phase 4
Implements algebraic expansion using the distributive property.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from simplify import simplify

def expand(expr):
    """
    Expand an expression using the distributive property.
    
    Examples:
    - (x + 2)(x + 3) → x^2 + 5x + 6
    - 2(x + y) → 2x + 2y
    - (x + y)^2 → x^2 + 2xy + y^2
    """
    if isinstance(expr, Number):
        return expr
    
    elif isinstance(expr, Symbol):
        return expr
    
    elif isinstance(expr, Add):
        return expand_add(expr)
    
    elif isinstance(expr, Mul):
        return expand_mul(expr)
    
    elif isinstance(expr, Pow):
        return expand_pow(expr)
    
    else:
        return expr

def expand_add(expr):
    """Expand addition expressions by expanding each operand."""
    left = expand(expr.left)
    right = expand(expr.right)
    return Add(left, right)

def expand_mul(expr):
    """Expand multiplication expressions using the distributive property."""
    left = expand(expr.left)
    right = expand(expr.right)
    
    # If both operands are sums, apply FOIL method
    if isinstance(left, Add) and isinstance(right, Add):
        return expand_foil(left, right)
    
    # If left operand is a sum, distribute right over it
    elif isinstance(left, Add):
        return expand_distribute(left, right)
    
    # If right operand is a sum, distribute left over it
    elif isinstance(right, Add):
        return expand_distribute(right, left)
    
    # If neither is a sum, just return the multiplication
    else:
        return Mul(left, right)

def expand_foil(left_add, right_add):
    """
    Apply FOIL method to expand (a + b)(c + d) = ac + ad + bc + bd
    """
    a = left_add.left
    b = left_add.right
    c = right_add.left
    d = right_add.right
    
    # FOIL: First, Outer, Inner, Last
    first = Mul(a, c)      # a * c
    outer = Mul(a, d)      # a * d
    inner = Mul(b, c)      # b * c
    last = Mul(b, d)       # b * d
    
    # Combine all terms
    result = Add(first, outer)
    result = Add(result, inner)
    result = Add(result, last)
    
    return simplify(result)

def expand_distribute(sum_expr, other_expr):
    """
    Distribute other_expr over sum_expr: (a + b) * c = a*c + b*c
    """
    a = sum_expr.left
    b = sum_expr.right
    
    # Distribute: (a + b) * c = a*c + b*c
    left_term = Mul(a, other_expr)
    right_term = Mul(b, other_expr)
    
    result = Add(left_term, right_term)
    return simplify(result)

def expand_pow(expr):
    """Expand power expressions using binomial expansion for simple cases."""
    base = expand(expr.base)
    exp = expand(expr.exp)
    
    # If exponent is a number, we can expand
    if isinstance(exp, Number):
        if exp.value == 0:
            return Number(1)
        elif exp.value == 1:
            return base
        elif exp.value == 2 and isinstance(base, Add):
            # Expand (a + b)^2 = a^2 + 2ab + b^2
            return expand_square(base)
        elif exp.value == 3 and isinstance(base, Add):
            # Expand (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
            return expand_cube(base)
        else:
            # For other integer powers, we could implement more general expansion
            # For now, just return the power expression
            return Pow(base, exp)
    else:
        # Non-numeric exponent, can't expand
        return Pow(base, exp)

def expand_square(expr):
    """Expand (a + b)^2 = a^2 + 2ab + b^2"""
    a = expr.left
    b = expr.right
    
    a_squared = Pow(a, Number(2))
    b_squared = Pow(b, Number(2))
    two_ab = Mul(Number(2), Mul(a, b))
    
    result = Add(a_squared, two_ab)
    result = Add(result, b_squared)
    
    return simplify(result)

def expand_cube(expr):
    """Expand (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3"""
    a = expr.left
    b = expr.right
    
    a_cubed = Pow(a, Number(3))
    b_cubed = Pow(b, Number(3))
    three_a2b = Mul(Number(3), Mul(Pow(a, Number(2)), b))
    three_ab2 = Mul(Number(3), Mul(a, Pow(b, Number(2))))
    
    result = Add(a_cubed, three_a2b)
    result = Add(result, three_ab2)
    result = Add(result, b_cubed)
    
    return simplify(result)

def expand_expression(text):
    """Convenience function to parse and expand a string expression."""
    from parser import parse_expression
    parsed = parse_expression(text)
    return expand(parsed)

# Example usage and testing
if __name__ == "__main__":
    from parser import parse_expression
    
    # Test cases
    test_cases = [
        ("(x + 2)(x + 3)", "FOIL expansion"),
        ("2(x + y)", "Simple distribution"),
        ("(x + y)^2", "Square expansion"),
        ("(x + y)^3", "Cube expansion"),
        ("(a + b)(c + d)", "General FOIL"),
        ("3(x + 2)", "Constant distribution"),
    ]
    
    print("🧪 Testing Expansion Engine...\n")
    
    for expr_str, description in test_cases:
        try:
            print(f"{description}: '{expr_str}'")
            expanded = expand_expression(expr_str)
            print(f"  → {expanded}")
        except Exception as e:
            print(f"  → ERROR: {e}")
    
    print("\n✅ Expansion testing complete!") 
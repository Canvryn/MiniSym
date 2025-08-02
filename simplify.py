#!/usr/bin/env python3
"""
Simplification Engine for MiniSym - Phase 3
Applies algebraic rules to simplify expressions.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow

def simplify(expr):
    """
    Simplify an expression by applying algebraic rules.
    
    Rules implemented:
    - Constants and identity rules (x + 0 → x, 1 * x → x)
    - Constant folding (2 + 3 → 5)
    - Like-term combination (2*x + 3*x → 5*x)
    - Nested simplification (recursive descent)
    """
    if isinstance(expr, Number):
        return expr
    
    elif isinstance(expr, Symbol):
        return expr
    
    elif isinstance(expr, Add):
        return simplify_add(expr)
    
    elif isinstance(expr, Mul):
        return simplify_mul(expr)
    
    elif isinstance(expr, Pow):
        return simplify_pow(expr)
    
    else:
        return expr

def simplify_add(expr):
    """Simplify addition expressions."""
    # Simplify both operands first
    left = simplify(expr.left)
    right = simplify(expr.right)
    
    # Rule: x + 0 → x
    if isinstance(right, Number) and right.value == 0:
        return left
    
    if isinstance(left, Number) and left.value == 0:
        return right
    
    # Rule: constant + constant → constant
    if isinstance(left, Number) and isinstance(right, Number):
        return Number(left.value + right.value)
    
    # Rule: like terms combination
    # Handle cases like: 2*x + 3*x → 5*x
    if (isinstance(left, Mul) and isinstance(right, Mul) and
        isinstance(left.left, Number) and isinstance(right.left, Number)):
        
        # Check if they have the same symbolic part
        if left.right == right.right:
            new_coeff = left.left.value + right.left.value
            if new_coeff == 0:
                return Number(0)
            elif new_coeff == 1:
                return left.right
            else:
                return Mul(Number(new_coeff), left.right)
    
    # Handle cases like: x + x → 2*x
    if left == right:
        return Mul(Number(2), left)
    
    # Handle cases like: x + (1*x) → 2*x
    if (isinstance(right, Mul) and isinstance(right.left, Number) and 
        right.left.value == 1 and right.right == left):
        return Mul(Number(2), left)
    
    if (isinstance(left, Mul) and isinstance(left.left, Number) and 
        left.left.value == 1 and left.right == right):
        return Mul(Number(2), right)
    
    # If no simplification rules apply, return the simplified expression
    return Add(left, right)

def simplify_mul(expr):
    """Simplify multiplication expressions."""
    # Simplify both operands first
    left = simplify(expr.left)
    right = simplify(expr.right)
    
    # Rule: x * 1 → x
    if isinstance(right, Number) and right.value == 1:
        return left
    
    if isinstance(left, Number) and left.value == 1:
        return right
    
    # Rule: x * 0 → 0
    if isinstance(right, Number) and right.value == 0:
        return Number(0)
    
    if isinstance(left, Number) and left.value == 0:
        return Number(0)
    
    # Rule: constant * constant → constant
    if isinstance(left, Number) and isinstance(right, Number):
        return Number(left.value * right.value)
    
    # Rule: constant * (constant * symbol) → (constant * symbol)
    if (isinstance(left, Number) and isinstance(right, Mul) and
        isinstance(right.left, Number)):
        new_coeff = left.value * right.left.value
        if new_coeff == 0:
            return Number(0)
        elif new_coeff == 1:
            return right.right
        else:
            return Mul(Number(new_coeff), right.right)
    
    # If no simplification rules apply, return the simplified expression
    return Mul(left, right)

def simplify_pow(expr):
    """Simplify power expressions."""
    # Simplify both operands first
    base = simplify(expr.base)
    exp = simplify(expr.exp)
    
    # Rule: x^1 → x
    if isinstance(exp, Number) and exp.value == 1:
        return base
    
    # Rule: x^0 → 1
    if isinstance(exp, Number) and exp.value == 0:
        return Number(1)
    
    # Rule: 1^x → 1
    if isinstance(base, Number) and base.value == 1:
        return Number(1)
    
    # Rule: 0^x → 0 (for x > 0)
    if isinstance(base, Number) and base.value == 0:
        if isinstance(exp, Number) and exp.value > 0:
            return Number(0)
    
    # Rule: constant^constant → constant
    if isinstance(base, Number) and isinstance(exp, Number):
        try:
            result = base.value ** exp.value
            return Number(result)
        except (OverflowError, ValueError):
            # Handle cases like 0^0 or very large numbers
            pass
    
    # If no simplification rules apply, return the simplified expression
    return Pow(base, exp)

def collect_like_terms(expr):
    """
    Collect like terms in an addition expression.
    This is a more advanced simplification that groups terms with the same variables.
    """
    if not isinstance(expr, Add):
        return expr
    
    # For now, implement basic like-term collection
    # This can be expanded later for more complex cases
    return simplify(expr)

# Example usage and testing
if __name__ == "__main__":
    from parser import parse_expression
    
    # Test cases
    test_cases = [
        ("x + 0", "x"),
        ("0 + x", "x"),
        ("2 + 3", "5"),
        ("x * 1", "x"),
        ("1 * x", "x"),
        ("x * 0", "0"),
        ("0 * x", "0"),
        ("2 * 3", "6"),
        ("x^1", "x"),
        ("x^0", "1"),
        ("1^x", "1"),
        ("2^3", "8"),
        ("2*x + 3*x", "5*x"),
        ("x + x", "2*x"),
    ]
    
    print("Testing Simplification Engine...\n")
    
    for input_expr, expected in test_cases:
        try:
            parsed = parse_expression(input_expr)
            simplified = simplify(parsed)
            print(f"'{input_expr}' → {simplified}")
        except Exception as e:
            print(f"'{input_expr}' → ERROR: {e}")
    
    print("\nSimplification testing complete!")

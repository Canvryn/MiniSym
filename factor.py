#!/usr/bin/env python3
"""
Factoring Engine for MiniSym - Phase 4
Implements algebraic factoring including GCF, difference of squares, and trinomial patterns.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from simplify import simplify
from expand import expand

def factor(expr):
    """
    Factor an expression using various factoring techniques.
    
    Examples:
    - 6x + 9 → 3(2x + 3)  (GCF factoring)
    - x^2 - 9 → (x - 3)(x + 3)  (difference of squares)
    - x^2 + 5x + 6 → (x + 2)(x + 3)  (trinomial factoring)
    """
    if isinstance(expr, Number):
        return expr
    
    elif isinstance(expr, Symbol):
        return expr
    
    elif isinstance(expr, Add):
        return factor_add(expr)
    
    elif isinstance(expr, Mul):
        return factor_mul(expr)
    
    elif isinstance(expr, Pow):
        return factor_pow(expr)
    
    else:
        return expr

def factor_add(expr):
    """Factor addition expressions."""
    left = factor(expr.left)
    right = factor(expr.right)
    
    # Try to factor the entire expression
    factored = try_factor_expression(Add(left, right))
    if factored != Add(left, right):
        return factored
    
    return Add(left, right)

def factor_mul(expr):
    """Factor multiplication expressions."""
    left = factor(expr.left)
    right = factor(expr.right)
    return Mul(left, right)

def factor_pow(expr):
    """Factor power expressions."""
    base = factor(expr.base)
    exp = factor(expr.exp)
    return Pow(base, exp)

def try_factor_expression(expr):
    """Try various factoring techniques on an expression."""
    if not isinstance(expr, Add):
        return expr
    
    # Try GCF factoring first
    gcf_result = factor_gcf(expr)
    if gcf_result != expr:
        return gcf_result
    
    # Try difference of squares
    dos_result = factor_difference_of_squares(expr)
    if dos_result != expr:
        return dos_result
    
    # Try trinomial factoring
    trinomial_result = factor_trinomial(expr)
    if trinomial_result != expr:
        return trinomial_result
    
    return expr

def factor_gcf(expr):
    """Factor out the greatest common factor from an expression."""
    if not isinstance(expr, Add):
        return expr
    
    # Collect all terms
    terms = collect_terms(expr)
    if len(terms) < 2:
        return expr
    
    # Find the GCF of coefficients
    coefficients = [term[0] for term in terms if isinstance(term[0], Number)]
    if not coefficients:
        return expr
    
    gcf_coeff = find_gcf_numbers(coefficients)
    if gcf_coeff == 1:
        return expr
    
    # Factor out the GCF
    factored_terms = []
    for coeff, var_part in terms:
        if isinstance(coeff, Number):
            new_coeff = Number(coeff.value / gcf_coeff)
        else:
            new_coeff = coeff
        
        if new_coeff == Number(1):
            factored_terms.append(var_part)
        elif new_coeff == Number(-1):
            # Handle negative coefficients
            factored_terms.append(Mul(Number(-1), var_part))
        else:
            factored_terms.append(Mul(new_coeff, var_part))
    
    # Reconstruct the expression
    if len(factored_terms) == 1:
        factored_expr = factored_terms[0]
    else:
        factored_expr = factored_terms[0]
        for term in factored_terms[1:]:
            factored_expr = Add(factored_expr, term)
    
    return Mul(Number(gcf_coeff), factored_expr)

def factor_difference_of_squares(expr):
    """Factor expressions of the form a^2 - b^2 = (a + b)(a - b)"""
    if not isinstance(expr, Add):
        return expr
    
    # Look for pattern: term1 + (-term2) where both are perfect squares
    terms = collect_terms(expr)
    if len(terms) != 2:
        return expr
    
    term1_coeff, term1_var = terms[0]
    term2_coeff, term2_var = terms[1]
    
    # Check if one term is negative
    if isinstance(term1_coeff, Number) and term1_coeff.value < 0:
        # term1 is negative, swap
        term1_coeff, term1_var, term2_coeff, term2_var = term2_coeff, term2_var, term1_coeff, term1_var
    
    if isinstance(term2_coeff, Number) and term2_coeff.value >= 0:
        return expr  # Not a difference of squares
    
    # Make term2 positive for analysis
    if isinstance(term2_coeff, Number):
        term2_coeff = Number(-term2_coeff.value)
    
    # Check if both terms are perfect squares
    a = extract_square_root(term1_coeff, term1_var)
    b = extract_square_root(term2_coeff, term2_var)
    
    if a is None or b is None:
        return expr
    
    # Create (a + b)(a - b)
    first_factor = Add(a, b)
    second_factor = Add(a, Mul(Number(-1), b))
    
    return Mul(first_factor, second_factor)

def factor_trinomial(expr):
    """Factor trinomials of the form ax^2 + bx + c"""
    if not isinstance(expr, Add):
        return expr
    
    # For now, implement basic trinomial factoring
    # This is a simplified version - could be expanded for more complex cases
    terms = collect_terms(expr)
    if len(terms) != 3:
        return expr
    
    # Look for pattern: ax^2 + bx + c
    # This is a basic implementation - could be made more sophisticated
    return expr

def collect_terms(expr):
    """Collect all terms in an addition expression."""
    if not isinstance(expr, Add):
        # Handle multiplication terms (extract coefficient)
        if isinstance(expr, Mul) and isinstance(expr.left, Number):
            return [(expr.left, expr.right)]
        # Handle negative terms
        elif isinstance(expr, Mul) and isinstance(expr.left, Number) and expr.left.value < 0:
            return [(expr.left, expr.right)]
        # Handle constant terms
        elif isinstance(expr, Number):
            return [(expr, Number(1))]
        else:
            return [(Number(1), expr)]
    
    terms = []
    
    # Recursively collect terms from left and right
    left_terms = collect_terms(expr.left)
    right_terms = collect_terms(expr.right)
    
    terms.extend(left_terms)
    terms.extend(right_terms)
    
    return terms

def find_gcf_numbers(numbers):
    """Find the greatest common factor of a list of numbers."""
    if not numbers:
        return 1
    
    # Convert to integers for easier calculation
    int_numbers = []
    for num in numbers:
        if isinstance(num, Number):
            if num.value == int(num.value):
                int_numbers.append(int(num.value))
            else:
                # If any number is not an integer, return 1
                return 1
    
    if not int_numbers:
        return 1
    
    # Find GCF using Euclidean algorithm
    gcf = abs(int_numbers[0])
    for num in int_numbers[1:]:
        gcf = gcd(gcf, abs(num))
    
    return gcf

def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def extract_square_root(coeff, var_part):
    """Extract the square root of a term if it's a perfect square."""
    # Check if coefficient is a perfect square
    if isinstance(coeff, Number):
        sqrt_coeff = int(coeff.value ** 0.5)
        if sqrt_coeff ** 2 == coeff.value:
            coeff_sqrt = Number(sqrt_coeff)
        else:
            return None
    else:
        coeff_sqrt = Number(1)
    
    # Check if variable part is a perfect square
    if isinstance(var_part, Pow) and isinstance(var_part.exp, Number):
        if var_part.exp.value % 2 == 0:
            # Even power, can extract square root
            new_exp = Number(var_part.exp.value // 2)
            var_sqrt = Pow(var_part.base, new_exp)
        else:
            return None
    elif isinstance(var_part, Symbol):
        # Single variable, square root is the variable itself
        var_sqrt = var_part
    else:
        return None
    
    # Combine coefficient and variable parts
    if coeff_sqrt.value == 1:
        return var_sqrt
    else:
        return Mul(coeff_sqrt, var_sqrt)

def factor_expression(text):
    """Convenience function to parse and factor a string expression."""
    from parser import parse_expression
    parsed = parse_expression(text)
    return factor(parsed)

# Example usage and testing
if __name__ == "__main__":
    from parser import parse_expression
    
    # Test cases
    test_cases = [
        ("6*x + 9", "GCF factoring"),
        ("x^2 - 9", "Difference of squares"),
        ("x^2 - 4", "Difference of squares"),
        ("2*x + 4*y", "GCF factoring"),
        ("x^2 + 2*x + 1", "Trinomial (perfect square)"),
    ]
    
    print("🧪 Testing Factoring Engine...\n")
    
    for expr_str, description in test_cases:
        try:
            print(f"{description}: '{expr_str}'")
            factored = factor_expression(expr_str)
            print(f"  → {factored}")
            
            # Verify by expanding back
            expanded = expand(factored)
            print(f"  → Expanded back: {expanded}")
            
        except Exception as e:
            print(f"  → ERROR: {e}")
    
    print("\n✅ Factoring testing complete!") 
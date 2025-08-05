#!/usr/bin/env python3
"""
Demo script for Phase 4: Algebraic Manipulations
Shows off the expansion and factoring functionality.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import parse_expression
from simplify import simplify
from expand import expand, expand_expression
from factor import factor, factor_expression

def demo_expansion():
    """Demonstrate expansion functionality."""
    print("🔧 Expansion Engine Demo:")
    print("-" * 40)
    
    expansion_cases = [
        ("(x + 2)(x + 3)", "FOIL expansion"),
        ("2(x + y)", "Simple distribution"),
        ("(x + y)^2", "Square expansion"),
        ("(x + y)^3", "Cube expansion"),
        ("(a + b)(c + d)", "General FOIL"),
        ("3(x + 2)", "Constant distribution"),
        ("(x + 1)(x - 1)", "Difference of squares pattern"),
    ]
    
    for expr_str, description in expansion_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            expanded = expand_expression(expr_str)
            print(f"  → {expanded}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_factoring():
    """Demonstrate factoring functionality."""
    print("\n\n🔍 Factoring Engine Demo:")
    print("-" * 40)
    
    factoring_cases = [
        ("6*x + 9", "GCF factoring"),
        ("x^2 - 9", "Difference of squares"),
        ("x^2 - 4", "Difference of squares"),
        ("2*x + 4*y", "GCF factoring"),
        ("x^2 + 2*x + 1", "Perfect square trinomial"),
        ("3*x + 6", "Simple GCF"),
    ]
    
    for expr_str, description in factoring_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            factored = factor_expression(expr_str)
            print(f"  → {factored}")
            
            # Verify by expanding back
            expanded = expand(factored)
            print(f"  → Expanded back: {expanded}")
            
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_expand_then_factor():
    """Demonstrate the relationship between expansion and factoring."""
    print("\n\n🔄 Expand → Factor Demo:")
    print("-" * 40)
    
    # Start with a factored expression
    factored_expr = "(x + 2)(x + 3)"
    print(f"Starting with: {factored_expr}")
    
    try:
        # Expand it
        expanded = expand_expression(factored_expr)
        print(f"Expanded: {expanded}")
        
        # Try to factor it back
        factored_back = factor(expanded)
        print(f"Factored back: {factored_back}")
        
    except Exception as e:
        print(f"ERROR: {e}")

def demo_factor_then_expand():
    """Demonstrate the relationship between factoring and expansion."""
    print("\n\n🔄 Factor → Expand Demo:")
    print("-" * 40)
    
    # Start with an expanded expression
    expanded_expr = "x^2 - 9"
    print(f"Starting with: {expanded_expr}")
    
    try:
        # Factor it
        factored = factor_expression(expanded_expr)
        print(f"Factored: {factored}")
        
        # Expand it back
        expanded_back = expand(factored)
        print(f"Expanded back: {expanded_back}")
        
    except Exception as e:
        print(f"ERROR: {e}")

def demo_complex_manipulations():
    """Demonstrate complex algebraic manipulations."""
    print("\n\n🎯 Complex Manipulations Demo:")
    print("-" * 40)
    
    complex_cases = [
        ("(x + y + z)^2", "Multivariable square"),
        ("(x + 1)(x + 2)(x + 3)", "Triple product"),
        ("2*(x + y) + 3*(x + y)", "Combining like terms after expansion"),
    ]
    
    for expr_str, description in complex_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            expanded = expand_expression(expr_str)
            print(f"  Expanded: {expanded}")
            
            # Try to simplify the result
            simplified = simplify(expanded)
            print(f"  Simplified: {simplified}")
            
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_integration_with_previous_phases():
    """Demonstrate integration with previous phases."""
    print("\n\n🔗 Integration Demo:")
    print("-" * 40)
    
    print("\n1. Parse → Expand → Simplify workflow:")
    expr_str = "(x + 2)(x + 3)"
    print(f"   Input: '{expr_str}'")
    
    try:
        # Parse
        parsed = parse_expression(expr_str)
        print(f"   Parsed: {parsed}")
        
        # Expand
        expanded = expand(parsed)
        print(f"   Expanded: {expanded}")
        
        # Simplify
        simplified = simplify(expanded)
        print(f"   Simplified: {simplified}")
        
    except Exception as e:
        print(f"   ERROR: {e}")
    
    print("\n2. Using expanded expressions in new operations:")
    try:
        # Create an expanded expression
        expanded_expr = expand_expression("(x + 1)^2")
        print(f"   Expanded: {expanded_expr}")
        
        # Use it in new operations
        result1 = expanded_expr + Number(5)
        print(f"   + 5: {result1}")
        
        result2 = expanded_expr * Symbol('y')
        print(f"   * y: {result2}")
        
    except Exception as e:
        print(f"   ERROR: {e}")

def demo_error_handling():
    """Demonstrate error handling in algebraic manipulations."""
    print("\n\n⚠️ Error Handling Demo:")
    print("-" * 40)
    
    error_cases = [
        ("(x + y)^4", "Higher power not yet implemented"),
        ("x^2 + x + 1", "Complex trinomial not yet implemented"),
        ("(x + y + z)(a + b)", "Multivariable FOIL not yet implemented"),
    ]
    
    for expr_str, description in error_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            expanded = expand_expression(expr_str)
            print(f"  → {expanded}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_phase4_complete():
    """Main demo function."""
    print("🚀 MiniSym Phase 4 Demo: Algebraic Manipulations\n")
    print("This demo shows the expansion and factoring engines that")
    print("implement algebraic manipulation capabilities.\n")
    
    demo_expansion()
    demo_factoring()
    demo_expand_then_factor()
    demo_factor_then_expand()
    demo_complex_manipulations()
    demo_integration_with_previous_phases()
    demo_error_handling()
    
    print("\n" + "="*50)
    print("✅ Phase 4 Complete! Ready for Phase 5: Differentiation")
    print("="*50)
    print("\nKey Features Implemented:")
    print("✓ Expansion using distributive property")
    print("✓ FOIL method for binomial products")
    print("✓ Binomial expansion for squares and cubes")
    print("✓ GCF factoring")
    print("✓ Difference of squares factoring")
    print("✓ Integration with parser, AST, and simplification")
    print("✓ Verification through expand-factor cycles")

if __name__ == "__main__":
    demo_phase4_complete() 
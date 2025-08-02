#!/usr/bin/env python3
"""
Demo script for Phase 3: Simplification Engine
Shows off the algebraic simplification functionality.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import parse_expression
from simplify import simplify

def demo_identity_rules():
    """Demonstrate identity rules simplification."""
    print("Identity Rules Demo:")
    print("-" * 40)
    
    identity_cases = [
        ("x + 0", "x + 0 → x"),
        ("0 + x", "0 + x → x"),
        ("x * 1", "x * 1 → x"),
        ("1 * x", "1 * x → x"),
        ("x * 0", "x * 0 → 0"),
        ("0 * x", "0 * x → 0"),
    ]
    
    for expr_str, description in identity_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_constant_folding():
    """Demonstrate constant folding."""
    print("\n\nConstant Folding Demo:")
    print("-" * 40)
    
    constant_cases = [
        ("2 + 3", "2 + 3 → 5"),
        ("2.5 + 3.7", "2.5 + 3.7 → 6.2"),
        ("2 * 3", "2 * 3 → 6"),
        ("2.5 * 3", "2.5 * 3 → 7.5"),
        ("2^3", "2^3 → 8"),
        ("3^2", "3^2 → 9"),
    ]
    
    for expr_str, description in constant_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_power_rules():
    """Demonstrate power simplification rules."""
    print("\n\nPower Rules Demo:")
    print("-" * 40)
    
    power_cases = [
        ("x^1", "x^1 → x"),
        ("x^0", "x^0 → 1"),
        ("1^x", "1^x → 1"),
        ("0^2", "0^2 → 0"),
    ]
    
    for expr_str, description in power_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_like_term_combination():
    """Demonstrate like-term combination."""
    print("\n\nLike-Term Combination Demo:")
    print("-" * 40)
    
    like_term_cases = [
        ("2*x + 3*x", "2*x + 3*x → 5*x"),
        ("x + x", "x + x → 2*x"),
        ("5*x + 2*x", "5*x + 2*x → 7*x"),
        ("3*x + (-3)*x", "3*x + (-3)*x → 0"),
    ]
    
    for expr_str, description in like_term_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_nested_simplification():
    """Demonstrate nested simplification."""
    print("\n\nNested Simplification Demo:")
    print("-" * 40)
    
    nested_cases = [
        ("(x + 0) + (y + 0)", "(x + 0) + (y + 0) → x + y"),
        ("(x * 1) * (y * 1)", "(x * 1) * (y * 1) → x * y"),
        ("(2 + 3) * x", "(2 + 3) * x → 5*x"),
        ("x * (2 + 3)", "x * (2 + 3) → x * 5"),
    ]
    
    for expr_str, description in nested_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_complex_simplifications():
    """Demonstrate complex simplification scenarios."""
    print("\n\nComplex Simplifications Demo:")
    print("-" * 40)
    
    complex_cases = [
        ("(x + 0) * (y + 0) + (2 + 3)", "(x + 0) * (y + 0) + (2 + 3) → (x * y) + 5"),
        ("(x^1)^1", "(x^1)^1 → x"),
        ("2*x + 3*x + 4*x", "2*x + 3*x + 4*x → ((5 * x) + (4 * x))"),
    ]
    
    for expr_str, description in complex_cases:
        print(f"\n{description}")
        parsed = parse_expression(expr_str)
        simplified = simplify(parsed)
        print(f"  {parsed} → {simplified}")

def demo_simplification_workflow():
    """Demonstrate the complete simplification workflow."""
    print("\n\nSimplification Workflow Demo:")
    print("-" * 40)
    
    print("\nStep-by-step simplification:")
    
    # Start with a complex expression
    expr_str = "2*x + 3*x + 0"
    print(f"\n1. Original expression: '{expr_str}'")
    
    # Parse it
    parsed = parse_expression(expr_str)
    print(f"2. Parsed AST: {parsed}")
    
    # Simplify it
    simplified = simplify(parsed)
    print(f"3. Simplified: {simplified}")
    
    # Show the internal representation
    print(f"4. Internal form: {repr(simplified)}")
    
    # Demonstrate that simplified expressions work with operators
    print(f"\n5. Using simplified expression in new operations:")
    new_expr = simplified + Number(5)
    print(f"   {simplified} + 5 = {new_expr}")
    
    new_expr = simplified * Number(3)
    print(f"   {simplified} * 3 = {new_expr}")

def demo_phase3_complete():
    """Main demo function."""
    print("🚀 MiniSym Phase 3 Demo: Simplification Engine\n")
    print("This demo shows the simplification engine that applies")
    print("algebraic rules to simplify mathematical expressions.\n")
    
    demo_identity_rules()
    demo_constant_folding()
    demo_power_rules()
    demo_like_term_combination()
    demo_nested_simplification()
    demo_complex_simplifications()
    demo_simplification_workflow()
    
    print("\n" + "="*50)
    print("✅ Phase 3 Complete! Ready for Phase 4: Algebraic Manipulations")
    print("="*50)
    print("\nKey Features Implemented:")
    print("✓ Identity rules (x + 0 → x, x * 1 → x)")
    print("✓ Constant folding (2 + 3 → 5)")
    print("✓ Power rules (x^1 → x, x^0 → 1)")
    print("✓ Like-term combination (2*x + 3*x → 5*x)")
    print("✓ Nested simplification (recursive descent)")
    print("✓ Integration with parser and AST")

if __name__ == "__main__":
    demo_phase3_complete() 
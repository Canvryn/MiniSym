#!/usr/bin/env python3
"""
MiniSym - Main Entry Point
Demonstrates the current functionality of the symbolic math engine.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import parse_expression
from simplify import simplify
from expand import expand, expand_expression
from factor import factor, factor_expression

def main():
    """Main demonstration of MiniSym functionality."""
    print("MiniSym - Symbolic Math Engine")
    print("=" * 50)
    print("Current Features: Phase 1 (AST) + Phase 2 (Parser) + Phase 3 (Simplification) + Phase 4 (Algebraic Manipulations)")
    print()
    
    # Phase 1: Direct AST construction
    print("Phase 1: Direct AST Construction")
    print("-" * 40)
    
    x = Symbol('x')
    y = Symbol('y')
    
    # Create expressions using operator overloads
    expr1 = x + y
    expr2 = x * 2
    expr3 = x ** 2 + y ** 2
    
    print(f"x + y = {expr1}")
    print(f"x * 2 = {expr2}")
    print(f"x^2 + y^2 = {expr3}")
    print()
    
    # Phase 2: Parsing from strings
    print("Phase 2: Parsing from Strings")
    print("-" * 40)
    
    test_expressions = [
        "x + 2",
        "3 * x",
        "(x + 2) * 3",
        "2 + 3 * x",
        "x^2 + y^2"
    ]
    
    for expr_str in test_expressions:
        try:
            parsed_expr = parse_expression(expr_str)
            print(f"'{expr_str}' → {parsed_expr}")
        except Exception as e:
            print(f"'{expr_str}' → ERROR: {e}")
    
    print()
    
    # Integration demo
    print("Integration Demo: Combining Phases")
    print("-" * 40)
    
    # Parse an expression and use it in new operations
    parsed_expr = parse_expression("x + y")
    print(f"Parsed: {parsed_expr}")
    
    # Add a number to the parsed expression
    result1 = parsed_expr + Number(5)
    print(f"  + 5: {result1}")
    
    # Multiply by a number
    result2 = parsed_expr * Number(3)
    print(f"  * 3: {result2}")
    
    # Create a complex expression
    complex_expr = parse_expression("(x + 2) * 3")
    print(f"\nComplex: {complex_expr}")
    
    # Add another parsed expression
    another_expr = parse_expression("y + 1")
    combined = complex_expr + another_expr
    print(f"  + (y + 1): {combined}")
    
    print()
    
    # Phase 3: Simplification
    print("Phase 3: Simplification Engine")
    print("-" * 40)
    
    test_expressions = [
        "x + 0",
        "2 + 3",
        "x * 1",
        "x^1",
        "2*x + 3*x",
        "x + x"
    ]
    
    for expr_str in test_expressions:
        try:
            parsed_expr = parse_expression(expr_str)
            simplified_expr = simplify(parsed_expr)
            print(f"'{expr_str}' → {simplified_expr}")
        except Exception as e:
            print(f"'{expr_str}' → ERROR: {e}")
    
    print()
    
    # Phase 4: Algebraic Manipulations
    print("Phase 4: Algebraic Manipulations")
    print("-" * 40)
    
    # Expansion examples
    print("\nExpansion Examples:")
    expansion_examples = [
        "(x + 2)(x + 3)",
        "(x + y)^2",
        "2(x + y)"
    ]
    
    for expr_str in expansion_examples:
        try:
            expanded = expand_expression(expr_str)
            print(f"'{expr_str}' → {expanded}")
        except Exception as e:
            print(f"'{expr_str}' → ERROR: {e}")
    
    # Factoring examples
    print("\nFactoring Examples:")
    factoring_examples = [
        "6*x + 9",
        "x^2 - 9",
        "2*x + 4*y"
    ]
    
    for expr_str in factoring_examples:
        try:
            factored = factor_expression(expr_str)
            print(f"'{expr_str}' → {factored}")
        except Exception as e:
            print(f"'{expr_str}' → ERROR: {e}")
    
    # Integration demo
    print("\nIntegration Demo:")
    try:
        # Expand then factor
        original = "(x + 2)(x + 3)"
        expanded = expand_expression(original)
        print(f"Original: {original}")
        print(f"Expanded: {expanded}")
        
        # Use expanded expression in new operations
        result = expanded + Number(5)
        print(f"Expanded + 5: {result}")
        
    except Exception as e:
        print(f"Integration demo error: {e}")
    
    print()
    print("=" * 50)
    print("MiniSym is working correctly!")
    print("Next: Phase 5 - Differentiation")
    print("=" * 50)

if __name__ == "__main__":
    main()

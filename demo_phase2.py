#!/usr/bin/env python3
"""
Demo script for Phase 2: Parser
Shows off the tokenizer and parser functionality.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import Tokenizer, Parser, parse_expression

def demo_tokenizer():
    """Demonstrate the tokenizer functionality."""
    print("🔍 Tokenizer Demo:")
    print("-" * 40)
    
    test_cases = [
        "x + 2",
        "3.14 * y",
        "my_var + 42",
        "  x   +   2  "  # with extra whitespace
    ]
    
    for text in test_cases:
        print(f"\nInput: '{text}'")
        tokenizer = Tokenizer(text)
        print("Tokens:")
        for i, token in enumerate(tokenizer.tokens):
            print(f"  {i}: {token}")

def demo_basic_parsing():
    """Demonstrate basic parsing functionality."""
    print("\n\n🔧 Basic Parser Demo:")
    print("-" * 40)
    
    test_cases = [
        ("x + 2", "Simple addition"),
        ("3 * x", "Simple multiplication"),
        ("x + y", "Symbol addition"),
        ("42", "Single number"),
        ("3.14", "Single float"),
        ("x", "Single variable")
    ]
    
    for expr_str, description in test_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            ast = parse_expression(expr_str)
            print(f"  → {ast}")
            print(f"  → {repr(ast)}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_operator_precedence():
    """Demonstrate operator precedence handling."""
    print("\n\n⚖️ Operator Precedence Demo:")
    print("-" * 40)
    
    test_cases = [
        ("2 + 3 * x", "Multiplication before addition"),
        ("(2 + 3) * x", "Parentheses override precedence"),
        ("x + y * 2 + z", "Multiple operations with precedence")
    ]
    
    for expr_str, description in test_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            ast = parse_expression(expr_str)
            print(f"  → {ast}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_parentheses():
    """Demonstrate parentheses handling."""
    print("\n\n📝 Parentheses Demo:")
    print("-" * 40)
    
    test_cases = [
        ("(x + 2)", "Simple parentheses"),
        ("((x + 2) * 3)", "Nested parentheses"),
        ("(x + (y * 2)) + z", "Complex nested expression")
    ]
    
    for expr_str, description in test_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            ast = parse_expression(expr_str)
            print(f"  → {ast}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_error_handling():
    """Demonstrate error handling."""
    print("\n\n⚠️ Error Handling Demo:")
    print("-" * 40)
    
    error_cases = [
        ("", "Empty input"),
        ("(x + 2", "Unmatched opening parenthesis"),
        ("x + 2)", "Unmatched closing parenthesis"),
        ("x @ 2", "Unknown character"),
        ("x + 2.3.4", "Invalid number")
    ]
    
    for expr_str, description in error_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            ast = parse_expression(expr_str)
            print(f"  → {ast}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_complex_expressions():
    """Demonstrate complex expression parsing."""
    print("\n\n🎯 Complex Expressions Demo:")
    print("-" * 40)
    
    complex_cases = [
        ("2 * x + 3 * y + 4", "Multiple terms with coefficients"),
        ("(x + y) * (a + b)", "Product of sums"),
        ("2.5 * x + 3.7", "Floating point coefficients")
    ]
    
    for expr_str, description in complex_cases:
        print(f"\n{description}: '{expr_str}'")
        try:
            ast = parse_expression(expr_str)
            print(f"  → {ast}")
        except Exception as e:
            print(f"  → ERROR: {e}")

def demo_parser_integration():
    """Demonstrate parser integration with AST operations."""
    print("\n\n🔗 Parser Integration Demo:")
    print("-" * 40)
    
    # Parse an expression and use it in new operations
    print("\nParsing 'x + y' and using it in new expressions:")
    parsed_expr = parse_expression("x + y")
    print(f"  Parsed: {parsed_expr}")
    
    # Add a number to the parsed expression
    new_expr1 = parsed_expr + Number(5)
    print(f"  + 5: {new_expr1}")
    
    # Multiply the parsed expression by a number
    new_expr2 = parsed_expr * Number(3)
    print(f"  * 3: {new_expr2}")
    
    # Create a more complex expression
    complex_expr = parse_expression("(x + 2) * 3")
    print(f"\nParsing '(x + 2) * 3': {complex_expr}")
    
    # Add another parsed expression
    another_expr = parse_expression("y + 1")
    combined = complex_expr + another_expr
    print(f"  + (y + 1): {combined}")

def demo_phase2_complete():
    """Main demo function."""
    print("🚀 MiniSym Phase 2 Demo: Parser\n")
    print("This demo shows the tokenizer and parser functionality")
    print("that converts mathematical expressions from strings to ASTs.\n")
    
    demo_tokenizer()
    demo_basic_parsing()
    demo_operator_precedence()
    demo_parentheses()
    demo_error_handling()
    demo_complex_expressions()
    demo_parser_integration()
    
    print("\n" + "="*50)
    print("✅ Phase 2 Complete! Ready for Phase 3: Simplification")
    print("="*50)
    print("\nKey Features Implemented:")
    print("✓ Tokenizer for breaking strings into tokens")
    print("✓ Recursive descent parser for building ASTs")
    print("✓ Operator precedence handling")
    print("✓ Parentheses support")
    print("✓ Error handling for invalid inputs")
    print("✓ Integration with existing AST classes")

if __name__ == "__main__":
    demo_phase2_complete() 
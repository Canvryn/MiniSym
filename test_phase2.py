#!/usr/bin/env python3
"""
Test file for Phase 2: Parser
Tests tokenization, parsing, and error handling.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import Tokenizer, Parser, parse_expression, Token

def test_tokenizer():
    """Test the tokenizer functionality."""
    print("Testing tokenizer...")
    
    # Test basic tokens
    tokenizer = Tokenizer("x + 2")
    tokens = tokenizer.tokens
    assert len(tokens) == 3
    assert tokens[0].type == 'IDENTIFIER' and tokens[0].value == 'x'
    assert tokens[1].type == 'OPERATOR' and tokens[1].value == '+'
    assert tokens[2].type == 'NUMBER' and tokens[2].value == 2
    
    # Test numbers (integers and floats)
    tokenizer = Tokenizer("3.14 + 42")
    tokens = tokenizer.tokens
    assert len(tokens) == 3
    assert tokens[0].type == 'NUMBER' and tokens[0].value == 3.14
    assert tokens[1].type == 'OPERATOR' and tokens[1].value == '+'
    assert tokens[2].type == 'NUMBER' and tokens[2].value == 42
    
    # Test identifiers with underscores
    tokenizer = Tokenizer("my_var + x")
    tokens = tokenizer.tokens
    assert len(tokens) == 3
    assert tokens[0].type == 'IDENTIFIER' and tokens[0].value == 'my_var'
    
    # Test whitespace handling
    tokenizer = Tokenizer("  x   +   2  ")
    tokens = tokenizer.tokens
    assert len(tokens) == 3
    assert tokens[0].type == 'IDENTIFIER' and tokens[0].value == 'x'
    assert tokens[1].type == 'OPERATOR' and tokens[1].value == '+'
    assert tokens[2].type == 'NUMBER' and tokens[2].value == 2
    
    print("✓ Tokenizer tests passed!")

def test_basic_parsing():
    """Test basic parsing functionality."""
    print("Testing basic parsing...")
    
    # Test simple expressions
    expr = parse_expression("x + 2")
    expected = Add(Symbol('x'), Number(2))
    assert str(expr) == str(expected)
    
    expr = parse_expression("3 * x")
    expected = Mul(Number(3), Symbol('x'))
    assert str(expr) == str(expected)
    
    expr = parse_expression("x + y")
    expected = Add(Symbol('x'), Symbol('y'))
    assert str(expr) == str(expected)
    
    # Test numbers
    expr = parse_expression("42")
    expected = Number(42)
    assert str(expr) == str(expected)
    
    expr = parse_expression("3.14")
    expected = Number(3.14)
    assert str(expr) == str(expected)
    
    # Test single variables
    expr = parse_expression("x")
    expected = Symbol('x')
    assert str(expr) == str(expected)
    
    print("✓ Basic parsing tests passed!")

def test_operator_precedence():
    """Test operator precedence handling."""
    print("Testing operator precedence...")
    
    # Test multiplication before addition
    expr = parse_expression("2 + 3 * x")
    expected = Add(Number(2), Mul(Number(3), Symbol('x')))
    assert str(expr) == str(expected)
    
    # Test parentheses override precedence
    expr = parse_expression("(2 + 3) * x")
    expected = Mul(Add(Number(2), Number(3)), Symbol('x'))
    assert str(expr) == str(expected)
    
    # Test multiple operations
    expr = parse_expression("x + y * 2 + z")
    expected = Add(Add(Symbol('x'), Mul(Symbol('y'), Number(2))), Symbol('z'))
    assert str(expr) == str(expected)
    
    print("✓ Operator precedence tests passed!")

def test_parentheses():
    """Test parentheses handling."""
    print("Testing parentheses...")
    
    # Test simple parentheses
    expr = parse_expression("(x + 2)")
    expected = Add(Symbol('x'), Number(2))
    assert str(expr) == str(expected)
    
    # Test nested parentheses
    expr = parse_expression("((x + 2) * 3)")
    expected = Mul(Add(Symbol('x'), Number(2)), Number(3))
    assert str(expr) == str(expected)
    
    # Test complex nested expressions
    expr = parse_expression("(x + (y * 2)) + z")
    expected = Add(Add(Symbol('x'), Mul(Symbol('y'), Number(2))), Symbol('z'))
    assert str(expr) == str(expected)
    
    print("✓ Parentheses tests passed!")

def test_error_handling():
    """Test error handling for invalid inputs."""
    print("Testing error handling...")
    
    # Test empty input
    try:
        parse_expression("")
        assert False, "Should have raised ValueError for empty input"
    except ValueError:
        pass
    
    # Test unmatched parentheses
    try:
        parse_expression("(x + 2")
        assert False, "Should have raised ValueError for unmatched parentheses"
    except ValueError:
        pass
    
    try:
        parse_expression("x + 2)")
        assert False, "Should have raised ValueError for unmatched parentheses"
    except ValueError:
        pass
    
    # Test unknown characters
    try:
        parse_expression("x @ 2")
        assert False, "Should have raised ValueError for unknown character"
    except ValueError:
        pass
    
    # Test invalid numbers
    try:
        parse_expression("x + 2.3.4")
        assert False, "Should have raised ValueError for invalid number"
    except ValueError:
        pass
    
    print("✓ Error handling tests passed!")

def test_complex_expressions():
    """Test more complex expressions."""
    print("Testing complex expressions...")
    
    # Test expression with multiple operations
    expr = parse_expression("2 * x + 3 * y + 4")
    expected = Add(Add(Mul(Number(2), Symbol('x')), Mul(Number(3), Symbol('y'))), Number(4))
    assert str(expr) == str(expected)
    
    # Test expression with nested parentheses
    expr = parse_expression("(x + y) * (a + b)")
    expected = Mul(Add(Symbol('x'), Symbol('y')), Add(Symbol('a'), Symbol('b')))
    assert str(expr) == str(expected)
    
    # Test expression with floats
    expr = parse_expression("2.5 * x + 3.7")
    expected = Add(Mul(Number(2.5), Symbol('x')), Number(3.7))
    assert str(expr) == str(expected)
    
    print("✓ Complex expression tests passed!")

def test_parser_integration():
    """Test parser integration with AST classes."""
    print("Testing parser integration...")
    
    # Test that parsed expressions work with existing AST functionality
    expr1 = parse_expression("x + 2")
    expr2 = parse_expression("x + 2")
    assert expr1 == expr2
    
    # Test that parsed expressions can be used in new expressions
    parsed_expr = parse_expression("x + y")
    new_expr = parsed_expr + Number(5)
    expected = Add(Add(Symbol('x'), Symbol('y')), Number(5))
    assert str(new_expr) == str(expected)
    
    # Test that parsed expressions work with multiplication
    parsed_expr = parse_expression("x + 2")
    new_expr = parsed_expr * Number(3)
    expected = Mul(Add(Symbol('x'), Number(2)), Number(3))
    assert str(new_expr) == str(expected)
    
    print("✓ Parser integration tests passed!")

if __name__ == "__main__":
    print("🧪 Running Phase 2 Tests...\n")
    
    test_tokenizer()
    test_basic_parsing()
    test_operator_precedence()
    test_parentheses()
    test_error_handling()
    test_complex_expressions()
    test_parser_integration()
    
    print("\n🎉 All Phase 2 tests passed! Your parser is working correctly.")
    print("\nNext steps:")
    print("1. Phase 3: Build the simplification engine")
    print("2. Phase 4: Add algebraic manipulations (expand, factor)")
    print("3. Phase 5: Implement symbolic differentiation") 
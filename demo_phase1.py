#!/usr/bin/env python3
"""
Demo script for Phase 1: Core Expression Engine
Shows off the AST construction, string representation, and operator overloads.
"""

from minisym_ast import Number, Symbol, Add, Mul, Pow

def demo_basic_usage():
    """Demonstrate basic usage of the expression classes."""
    print("🚀 MiniSym Phase 1 Demo: Core Expression Engine\n")
    
    # Create some basic expressions
    x = Symbol('x')
    y = Symbol('y')
    a = Number(5)
    b = Number(3)
    
    print("1. Basic Expression Construction:")
    print(f"   x = {x}")
    print(f"   y = {y}")
    print(f"   a = {a}")
    print(f"   b = {b}")
    
    # Demonstrate operator overloads
    print("\n2. Using Python Operators:")
    expr1 = x + y
    print(f"   x + y = {expr1}")
    
    expr2 = x * a
    print(f"   x * 5 = {expr2}")
    
    expr3 = x ** b
    print(f"   x ** 3 = {expr3}")
    
    # More complex expressions
    print("\n3. Complex Expressions:")
    expr4 = x + y * 2
    print(f"   x + y * 2 = {expr4}")
    
    expr5 = (x + y) * 2
    print(f"   (x + y) * 2 = {expr5}")
    
    expr6 = x ** 2 + y ** 2
    print(f"   x^2 + y^2 = {expr6}")
    
    # Demonstrate equality
    print("\n4. Equality Testing:")
    expr7 = x + a
    expr8 = x + Number(5)
    print(f"   {expr7} == {expr8}: {expr7 == expr8}")
    
    expr9 = x + b
    print(f"   {expr7} == {expr9}: {expr7 == expr9}")
    
    # Show internal representation
    print("\n5. Internal Representation (repr):")
    print(f"   {expr6} -> {repr(expr6)}")
    
    print("\n" + "="*50)
    print("✅ Phase 1 Complete! Ready for Phase 2: Parser")
    print("="*50)

if __name__ == "__main__":
    demo_basic_usage() 
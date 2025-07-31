#!/usr/bin/env python3
"""
Parser for MiniSym - Phase 2
Converts mathematical expressions from strings to ASTs.
"""

import re
from minisym_ast import Number, Symbol, Add, Mul, Pow

class Token:
    """Represents a single token in the input stream."""
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position
    
    def __str__(self):
        return f"Token({self.type}, '{self.value}', pos={self.position})"
    
    def __repr__(self):
        return self.__str__()

class Tokenizer:
    """Converts input strings into tokens."""
    
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.tokens = []
        self.tokenize()
    
    def tokenize(self):
        """Convert the input text into a list of tokens."""
        while self.position < len(self.text):
            char = self.text[self.position]
            
            # Skip whitespace
            if char.isspace():
                self.position += 1
                continue
            
            # Handle numbers
            if char.isdigit() or char == '.':
                self.read_number()
                continue
            
            # Handle identifiers (variables)
            if char.isalpha() or char == '_':
                self.read_identifier()
                continue
            
            # Handle operators and punctuation
            if char in '+-*/()^':
                self.tokens.append(Token('OPERATOR', char, self.position))
                self.position += 1
                continue
            
            # Unknown character
            raise ValueError(f"Unknown character '{char}' at position {self.position}")
    
    def read_number(self):
        """Read a number (integer or float) from the input."""
        start = self.position
        while (self.position < len(self.text) and 
               (self.text[self.position].isdigit() or self.text[self.position] == '.')):
            self.position += 1
        
        number_str = self.text[start:self.position]
        try:
            if '.' in number_str:
                value = float(number_str)
            else:
                value = int(number_str)
            self.tokens.append(Token('NUMBER', value, start))
        except ValueError:
            raise ValueError(f"Invalid number '{number_str}' at position {start}")
    
    def read_identifier(self):
        """Read an identifier (variable name) from the input."""
        start = self.position
        while (self.position < len(self.text) and 
               (self.text[self.position].isalnum() or self.text[self.position] == '_')):
            self.position += 1
        
        identifier = self.text[start:self.position]
        self.tokens.append(Token('IDENTIFIER', identifier, start))

class Parser:
    """Recursive descent parser for mathematical expressions."""
    
    def __init__(self, text):
        self.tokenizer = Tokenizer(text)
        self.tokens = self.tokenizer.tokens
        self.position = 0
    
    def parse(self):
        """Parse the expression and return an AST."""
        if not self.tokens:
            raise ValueError("Empty expression")
        
        result = self.parse_expression()
        
        # Check if we've consumed all tokens
        if self.position < len(self.tokens):
            raise ValueError(f"Unexpected tokens after expression at position {self.position}")
        
        return result
    
    def parse_expression(self):
        """Parse an expression (lowest precedence)."""
        left = self.parse_term()
        
        while (self.position < len(self.tokens) and 
               self.current_token().value in ['+', '-']):
            op = self.current_token().value
            self.advance()
            right = self.parse_term()
            
            if op == '+':
                left = Add(left, right)
            else:  # op == '-'
                # For now, treat subtraction as addition with negative
                if isinstance(right, Number):
                    right = Number(-right.value)
                else:
                    # For symbolic expressions, we'll need to implement negation
                    # For now, just use addition with a negative coefficient
                    left = Add(left, Mul(Number(-1), right))
        
        return left
    
    def parse_term(self):
        """Parse a term (medium precedence)."""
        left = self.parse_factor()
        
        while (self.position < len(self.tokens) and 
               self.current_token().value in ['*', '/']):
            op = self.current_token().value
            self.advance()
            right = self.parse_factor()
            
            if op == '*':
                left = Mul(left, right)
            else:  # op == '/'
                # For now, treat division as multiplication with reciprocal
                # This is a simplification - proper division would need a Div class
                if isinstance(right, Number) and right.value != 0:
                    left = Mul(left, Number(1 / right.value))
                else:
                    # For symbolic division, we'll need to implement proper division
                    # For now, just use multiplication
                    left = Mul(left, Pow(right, Number(-1)))
        
        return left
    
    def parse_factor(self):
        """Parse a factor (highest precedence)."""
        left = self.parse_primary()
        
        # Handle exponentiation (right-associative)
        while (self.position < len(self.tokens) and 
               self.current_token().value == '^'):
            self.advance()  # consume '^'
            right = self.parse_factor()  # recursive for right-associativity
            left = Pow(left, right)
        
        return left
    
    def parse_primary(self):
        """Parse primary expressions (numbers, variables, parentheses)."""
        token = self.current_token()
        
        if token.type == 'NUMBER':
            self.advance()
            return Number(token.value)
        
        elif token.type == 'IDENTIFIER':
            self.advance()
            return Symbol(token.value)
        
        elif token.value == '(':
            self.advance()  # consume '('
            expr = self.parse_expression()
            
            if (self.position >= len(self.tokens) or 
                self.current_token().value != ')'):
                raise ValueError("Unmatched parentheses")
            
            self.advance()  # consume ')'
            return expr
        
        else:
            raise ValueError(f"Unexpected token '{token.value}' at position {token.position}")
    
    def current_token(self):
        """Get the current token."""
        if self.position >= len(self.tokens):
            raise ValueError("Unexpected end of input")
        return self.tokens[self.position]
    
    def advance(self):
        """Move to the next token."""
        self.position += 1

def parse_expression(text):
    """Convenience function to parse a string expression into an AST."""
    parser = Parser(text)
    return parser.parse()

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_expressions = [
        "x + 2",
        "3 * x",
        "(x + 2) * 3",
        "2 + 3 * x",
        "x^2 + y^2",
        "2.5 * x + 3.7"
    ]
    
    print("🧪 Testing Parser...\n")
    
    for expr_str in test_expressions:
        try:
            ast = parse_expression(expr_str)
            print(f"'{expr_str}' → {ast}")
        except Exception as e:
            print(f"'{expr_str}' → ERROR: {e}")
    
    print("\n✅ Parser testing complete!") 
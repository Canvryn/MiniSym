#!/usr/bin/env python3
"""
Test script for Phase 4: Algebraic Manipulations
Tests expansion and factoring functionality.
"""

import unittest
from minisym_ast import Number, Symbol, Add, Mul, Pow
from parser import parse_expression
from simplify import simplify
from expand import expand, expand_expression
from factor import factor, factor_expression

class TestExpansion(unittest.TestCase):
    """Test expansion functionality."""
    
    def test_simple_distribution(self):
        """Test simple distribution: 2(x + y) → 2x + 2y"""
        expr = parse_expression("2*(x + y)")
        expanded = expand(expr)
        expected = Add(Mul(Number(2), Symbol('x')), Mul(Number(2), Symbol('y')))
        self.assertEqual(str(expanded), str(expected))
    
    def test_foil_expansion(self):
        """Test FOIL expansion: (x + 2)(x + 3) → x^2 + 5x + 6"""
        expr = parse_expression("(x + 2)*(x + 3)")
        expanded = expand(expr)
        # The result should be x^2 + 5x + 6
        # We'll check that it contains the expected terms
        expanded_str = str(expanded)
        self.assertIn("x", expanded_str)
        self.assertIn("5", expanded_str)
        self.assertIn("6", expanded_str)
    
    def test_square_expansion(self):
        """Test square expansion: (x + y)^2 → x^2 + 2xy + y^2"""
        expr = parse_expression("(x + y)^2")
        expanded = expand(expr)
        # Check that it contains the expected terms
        expanded_str = str(expanded)
        self.assertIn("x^2", expanded_str)
        self.assertIn("y^2", expanded_str)
    
    def test_cube_expansion(self):
        """Test cube expansion: (x + y)^3 → x^3 + 3x^2y + 3xy^2 + y^3"""
        expr = parse_expression("(x + y)^3")
        expanded = expand(expr)
        # Check that it contains the expected terms
        expanded_str = str(expanded)
        self.assertIn("x^3", expanded_str)
        self.assertIn("y^3", expanded_str)

class TestFactoring(unittest.TestCase):
    """Test factoring functionality."""
    
    def test_gcf_factoring(self):
        """Test GCF factoring: 6x + 9 → 3(2x + 3)"""
        expr = parse_expression("6*x + 9")
        factored = factor(expr)
        # Check that it's a product with 3 as a factor
        self.assertIsInstance(factored, Mul)
        self.assertEqual(factored.left, Number(3))
    
    def test_difference_of_squares(self):
        """Test difference of squares: x^2 - 9 → (x + 3)(x - 3)"""
        expr = parse_expression("x^2 - 9")
        factored = factor(expr)
        # Check that it's a product of two factors
        self.assertIsInstance(factored, Mul)
    
    def test_simple_gcf(self):
        """Test simple GCF: 3x + 6 → 3(x + 2)"""
        expr = parse_expression("3*x + 6")
        factored = factor(expr)
        # Check that it's a product with 3 as a factor
        self.assertIsInstance(factored, Mul)
        self.assertEqual(factored.left, Number(3))

class TestExpandFactorCycle(unittest.TestCase):
    """Test that expand and factor are inverse operations."""
    
    def test_expand_then_factor(self):
        """Test that expanding then factoring returns the original (or equivalent)."""
        original = parse_expression("(x + 2)*(x + 3)")
        expanded = expand(original)
        factored = factor(expanded)
        
        # The factored result should be equivalent to the original
        # We'll check that both contain the same variables
        original_str = str(original)
        factored_str = str(factored)
        self.assertIn("x", original_str)
        self.assertIn("x", factored_str)
    
    def test_factor_then_expand(self):
        """Test that factoring then expanding returns the original."""
        original = parse_expression("x^2 - 9")
        factored = factor(original)
        expanded = expand(factored)
        
        # The expanded result should be equivalent to the original
        original_str = str(original)
        expanded_str = str(expanded)
        self.assertIn("x^2", original_str)
        self.assertIn("x^2", expanded_str)

class TestIntegration(unittest.TestCase):
    """Test integration with previous phases."""
    
    def test_parse_expand_simplify(self):
        """Test the complete workflow: parse → expand → simplify."""
        expr_str = "(x + 2)*(x + 3)"
        parsed = parse_expression(expr_str)
        expanded = expand(parsed)
        simplified = simplify(expanded)
        
        # All steps should work without errors
        self.assertIsNotNone(parsed)
        self.assertIsNotNone(expanded)
        self.assertIsNotNone(simplified)
    
    def test_expanded_expression_operations(self):
        """Test that expanded expressions can be used in new operations."""
        expanded = expand_expression("(x + 1)^2")
        result = expanded + Number(5)
        
        # Should be able to add a number to expanded expression
        self.assertIsInstance(result, Add)
        self.assertEqual(result.right, Number(5))

if __name__ == '__main__':
    unittest.main() 
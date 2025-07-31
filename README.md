# MiniSym

A lightweight symbolic math engine written in Python.

This project implements a minimal computer algebra system from scratch. It handles symbolic manipulation tasks like simplification, expansion, factoring, and differentiation. Expressions are built as abstract syntax trees (ASTs), which allows for recursive and rule-based transformations.

## Current Status

### Phase 1: Core Expression Engine (Complete)
- AST classes: `Number`, `Symbol`, `Add`, `Mul`, `Pow`
- String representation and equality comparison
- Python operator overloads (`+`, `*`, `**`)

### Phase 2: Parser (Complete)
- Tokenizer for breaking strings into tokens
- Recursive descent parser for building ASTs
- Operator precedence handling
- Parentheses support
- Error handling for invalid inputs

### Phase 3: Simplification Engine (In Progress)
- Constants and identity rules
- Constant folding
- Like-term combination
- Nested simplification

### Phase 4: Algebraic Manipulations (Planned)
- Expansion logic (distributive property)
- Factoring logic (GCF, difference of squares)

### Phase 5: Differentiation (Planned)
- Power rule, product rule, constant rule
- Chain rule (basic)

## Project Structure

```
MiniSym/
├── minisym_ast.py      # Expression node classes (Phase 1)
├── parser.py           # Tokenizer and parser (Phase 2)
├── simplify.py         # Simplification logic (Phase 3)
├── test_phase1.py      # Tests for Phase 1
├── test_phase2.py      # Tests for Phase 2
├── demo_phase1.py      # Demo for Phase 1
├── demo_phase2.py      # Demo for Phase 2
└── README.md
```

## Testing

Run the tests to verify functionality:

```bash
# Test Phase 1 (Core Expression Engine)
python test_phase1.py

# Test Phase 2 (Parser)
python test_phase2.py
```

## Demo

See the parser in action:

```bash
# Demo Phase 1 (Core Expression Engine)
python demo_phase1.py

# Demo Phase 2 (Parser)
python demo_phase2.py
```

## Project Goals

This project is designed to reinforce:
- Symbolic computation techniques
- Recursive tree traversal and manipulation
- Algebraic rule implementation in code
- Foundations of symbolic math engines

It also serves as a platform to explore algebra and calculus logic through hands-on programming.

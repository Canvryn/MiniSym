# MiniSym

MiniSym is a lightweight symbolic math engine written in Python.

This project builds a minimal version of a computer algebra system from scratch. It supports symbolic manipulation tasks such as simplification, expansion, factoring, and differentiation. Expressions are represented as abstract syntax trees (ASTs), enabling recursive and rule-based transformations.

-- Features

- Parses algebraic expressions (e.g., `2*x + 3*x`) into ASTs
- Simplifies expressions by combining like terms and applying basic algebraic identities
- Expands polynomial expressions using the distributive property
- Factors expressions using GCF extraction, difference of squares, and basic trinomials
- Computes derivatives using standard rules (power, product, chain)
- Optional: Streamlit-based web interface for interactive use

-- Folder Structure

minisym/
├── ast.py # Expression node classes
├── parser.py # Tokenizer and recursive descent parser
├── simplify.py # Simplification logic
├── expand.py # Expansion logic
├── factor.py # Factoring logic
├── differentiate.py # Differentiation logic
├── main.py # CLI entry point
├── streamlit_app.py # Optional web interface
├── tests/ # Unit tests
└── requirements.txt

markdown
Copy
Edit

-- Project Goals

This project is designed to reinforce:
- Symbolic computation techniques
- Recursive tree traversal and manipulation
- Algebraic rule implementation in code
- Foundations of symbolic math engines

It also serves as a platform to explore algebra and calculus logic through hands-on programming.

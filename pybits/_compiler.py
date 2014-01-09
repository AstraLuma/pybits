"""
The actual dirty work of the AST transform.
"""
import ast

def compile(txt):
    tree = ast.parse(txt)
    # TODO: Transform
    return tree
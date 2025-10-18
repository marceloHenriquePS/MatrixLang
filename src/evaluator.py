"""Simple AST evaluator for matrix CREATE statements.

Exposes:
- evaluate(ast, env=None) -> env updated and returns env

Supported AST nodes:
    - ('CREATE', matrix)
"""
from typing import Any, Dict
from .validator import validate_matrix


class EvalError(Exception):
    pass


def evaluate(ast: Any, env: Dict[str, Any] = None) -> Dict[str, Any]:
    if env is None:
        env = {}

    if isinstance(ast, tuple):
        tag = ast[0]
        if tag == 'CREATE':
            _, matrix = ast
            try:
                validate_matrix(matrix)
            except ValueError as e:
                raise EvalError(str(e))
            env['_last'] = matrix
            return env
        else:
            raise EvalError(f"Unsupported AST node: {tag}")

    if isinstance(ast, list):
        for node in ast:
            evaluate(node, env)
        return env

    raise EvalError("Invalid AST structure")

__all__ = ["evaluate", "EvalError"]

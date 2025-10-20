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
    env = env if env is not None else globals().get('env', {})

    if not isinstance(ast, tuple):
        raise EvalError(f"Unsupported AST node: {tag}")
    
    tag = ast[0]

    if tag == 'ASSIGN':
        _, var_name, expr = ast
        value_env = evaluate(expr, env)
        env[var_name] = value_env.get('_last', None)
        return env

    if tag == 'CREATE':
        _, var_name, matrix = ast
        try:
            validate_matrix(matrix)
        except ValueError as e:
            raise EvalError(str(e))
        
        env[var_name] = matrix
        env['_last'] = matrix
        return env

    if tag == 'PRINT':
        _, var_name = ast
        if var_name not in env:
            raise EvalError(f"Undefined variable: {var_name}")
        value = env[var_name]
        print(value)
        return env

    raise EvalError("Invalid AST structure")

__all__ = ["evaluate", "EvalError"]

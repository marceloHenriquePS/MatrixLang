"""Simple AST evaluator for matrix CREATE statements.

Exposes:
- evaluate(ast, env=None) -> env updated and returns env

Supported AST nodes:
    - ('CREATE', matrix)
"""
import numpy as np
from typing import Any, Dict
from .validator import validate_matrix
from . import operations

class EvalError(Exception):
    pass

def evaluate_expression(expr: Any, env: Dict[str, Any]) -> Any:
    """Evaluate an expression node and return its value."""
    if isinstance(expr, int) or isinstance(expr, float):
        return expr
    
    elif isinstance(expr, str):
        if expr in env:
            return env[expr]
        else:
            raise EvalError(f"Undefined variable: {expr}")
        
    elif isinstance(expr, list):
        return expr
    
    elif isinstance(expr, tuple):
        tag = expr[0]

        match tag:
            case 'MSUM':
                matrices = [evaluate_expression(e, env) for e in expr[1:]]
                return operations.sum(matrices)

            case 'MSUB':
                matrices = [evaluate_expression(e, env) for e in expr[1:]]
                return operations.subtract(matrices)

            case 'MMULT' | 'MDIV':
                matrices = [evaluate_expression(e, env) for e in expr[1:]]
                if len(matrices) != 2:
                    raise EvalError(f"{tag} requires exactly two matrices")
                func = operations.multiply if tag == 'MMULT' else operations.divide
                return func(matrices[0], matrices[1])

            case 'MINVERSE':
                return operations.inverse(evaluate_expression(expr[1], env))

            case 'MTRANSPOSE':
                return operations.transpose(evaluate_expression(expr[1], env))

            case 'MRANK':
                return operations.rank(evaluate_expression(expr[1], env))

            case 'MDET':
                return operations.determinant(evaluate_expression(expr[1], env))

            case 'MEIGENVALUES':
                return operations.eigenvalues(evaluate_expression(expr[1], env))

            case 'MEIGENVECTORS':
                return operations.eigenvectors(evaluate_expression(expr[1], env))

            case 'MTRILOWER':
                return operations.lower_triangular(evaluate_expression(expr[1], env))

            case 'MTRIUPPER':
                return operations.upper_triangular(evaluate_expression(expr[1], env))

            case 'MESCALE':
                return operations.scaled_echelon_form(evaluate_expression(expr[1], env))

            case _:
                raise EvalError(f"Unknown operation: {tag}")
    else:
        raise EvalError(f"Unsupported expression type: {type(expr)}")

def evaluate(ast: Any, env: Dict[str, Any] = None) -> Dict[str, Any]:
    env = env if env is not None else {}

    if isinstance(ast, list):
        for node in ast:
            evaluate(node, env)
        return env

    if not isinstance(ast, tuple):
        raise EvalError(f"Unsupported AST node: {ast}")
    
    tag = ast[0]

    match tag:
        case 'ASSIGN':
            _, var_name, expr = ast
            value_env = evaluate_expression(expr, env)
            env[var_name] = value_env
            env['_last'] = value_env
            return env

        case 'CREATE':
            _, var_name, matrix = ast
            try:
                validate_matrix(matrix)
            except ValueError as e:
                raise EvalError(str(e))
            
            env[var_name] = np.array(matrix)
            env['_last'] = matrix
            return env

        case 'PRINT':
            _, expr = ast
            value = evaluate_expression(expr, env)
            print(value)
            env['_last'] = value
            return env

        case _:
            raise EvalError(f"Unsupported statement type: {tag}")

    raise EvalError("Invalid AST structure")

__all__ = ["evaluate", "EvalError"]

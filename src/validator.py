
"""Simple validator for matrices.

Public function:
- validate_matrix(matrix) -> returns True if valid, or raises ValueError with message.
"""
from typing import Any

def validate_matrix(matrix: Any) -> bool:
    """Validate that `matrix` is a non-empty list of non-empty lists containing only numbers.

    Minimal rules:
    - matrix must be a non-empty list
    - each element of matrix must be a non-empty list
    - all rows must have the same length
    - each row element must be int or float

    Returns True if valid; raises ValueError with an explanatory message otherwise.
    """
    if not isinstance(matrix, list) or not matrix:
        raise ValueError("Matrix must be a non-empty list")

    row_len = None
    for i, row in enumerate(matrix):
        if not isinstance(row, list) or not row:
            raise ValueError(f"Invalid row {i}: must be a non-empty list")
        
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise ValueError("All rows must have the same length")

        for j, elem in enumerate(row):
            if not isinstance(elem, (int, float)):
                raise ValueError(f"Non-numeric element at ({i},{j}): {elem}")

    return True

__all__ = ["validate_matrix"]

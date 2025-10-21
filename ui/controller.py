"""UI controller for MatrixLang."""

from src import matrix_parser as mp
from src import evaluator as ev
from typing import Callable
import re, io, sys, copy

def get_help_text() -> str:
    """Return a help text describing available commands and examples."""
    return (
        "MatrixLang Help\n\n"
        "MatrixLang is a simple language for performing matrix operations.\n\n"
        "Available commands:\n"
        "  - CREATE name [[row1], [row2], ...]: Create a matrix with the given name\n"
        "  - PRINT(name): Print the matrix with the given name\n\n"
        "Matrix operations:\n"
        "  - MSUM(A, B, ...): Sum of matrices A, B, ...\n"
        "  - MSUB(A, B, ...): Subtraction of matrices A, B, ...\n"
        "  - MMULT(A, B): Multiplication of matrices A and B\n"
        "  - MDIV(A, B): Division of matrix A by B\n"
        "  - MINVERSE(A): Inverse of matrix A\n"
        "  - MTRANSPOSE(A): Transpose of matrix A\n"
        "  - MRANK(A): Rank of matrix A\n"
        "  - MDET(A): Determinant of matrix A\n"
        "  - MEIGENVALUES(A): Eigenvalues of matrix A\n"
        "  - MEIGENVECTORS(A): Eigenvectors of matrix A\n"
        "  - MTRIUPPER(A): Upper triangular form of matrix A\n"
        "  - MTRILOWER(A): Lower triangular form of matrix A\n"
        "  - MESCALE(A): Scaled echelon form of matrix A\n\n"
        "Example usage:\n"
        "  CREATE A [[1, 2], [3, 4]];\n"
        "  CREATE B [[5, 6], [7, 8]];\n"
        "  CREATE C [[1, 2], [4, 5]];\n"
        "  D = MSUM(A, B, C);\n"
        "  E = MMULT(A, B);\n"
        "  F = MINVERSE(A);\n"
    )

def run_code(code: str, append_output: Callable[[str], None]) -> None:
    """Placeholder: run code and send output via append_output.

    Implement this function to parse and execute MatrixLang code and use
    append_output to display results in the UI.
    """
    global _env
    _env = {}
    if not code or not code.strip():
        append_output('No code to run.\n')
        return

    stmts = re.findall(r'[^;]+;', code, flags=re.S)
    if not stmts:
        append_output('No complete statements (need semicolons).\n')
        return

    for st in stmts:
        st_strip = st.strip()
        temp_env = copy.copy(_env)

        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            try:
                ast = mp.matrix_parser.parse(st_strip)
                if not ast:
                    append_output(f'Could not parse statement: {st_strip}\n')
                    return
                ev.evaluate(ast, env=temp_env)
            except ev.EvalError as ee:
                append_output(f'EvalError: {ee}\n')
                return
            except Exception as e:
                append_output(f'Execution error: {e}\n')
                return
        finally:
            sys.stdout = old_stdout

        _env.update(temp_env)

        output_text = buf.getvalue().strip()
        if output_text:
            lines = output_text.splitlines()
            formatted_output = ">>> " + lines[0]
            if len(lines) > 1:
                formatted_output += "\n" + "\n".join("... " + line for line in lines[1:])
            append_output(formatted_output + "\n")


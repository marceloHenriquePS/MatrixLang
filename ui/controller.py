"""Empty controller skeleton — start from scratch.

Replace the contents of this file with the controller implementation you want.
Common functions the UI expects:
- run_code(code: str, append_output: Callable[[str], None]) -> None
- open_help() -> None

For now these are minimal placeholders.
"""
from src import matrix_parser as mp
from src import evaluator as ev
from typing import Callable
import re, io, sys, copy

def get_help_text() -> str:
    """Return a help text describing available commands and examples.

    The UI will display this text in a dialog when the user clicks Help.
    """
    return (
        "Available commands:\n\n"
        "1) CREATE matrix;\n"
        "   - Example: A = CREATE [[1, 2], [3, 4]];\n\n"
        "2) PRINT matrix_name;\n"
        "   - Example: PRINT A;\n\n"
        "Notes:\n"
        "- Statements must end with a semicolon (;).\n"
        "- CREATE expects numeric values (int or float) inside the nested lists.\n"
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
        temp_env = copy.deepcopy(_env)

        old_stdout = sys.stdout
        buf = io.StringIO()
        try:
            sys.stdout = buf
            try:
                ast = mp.matrix_parser.parse(st_strip)
                if not ast:
                    append_output(f'Could not parse statement: {st_strip}\n')
                    continue
                ev.evaluate(ast, env=temp_env)
            except ev.EvalError as ee:
                append_output(f'EvalError: {ee}\n')
                continue
            except Exception as e:
                append_output(f'Execution error: {e}\n')
                continue
        finally:
            sys.stdout = old_stdout

        _env.update(temp_env)

        output = buf.getvalue()
        if output:
            append_output(output)


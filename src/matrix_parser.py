import ply.yacc as yacc
from .matrix_lexer import tokens

def p_statement_create(p):
    """statement : CREATE '(' matrix ')' SEMICOLON"""
    # New form: CREATE(matrix) -> produce ('CREATE', matrix)
    p[0] = ('CREATE', p[3])

def p_matrix(p):
    """matrix : '[' row_list ']'"""
    p[0] = p[2]

def p_row_list(p):
    """row_list : row
                | row COMMA row_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_row(p):
    """row : '[' value_list ']'"""
    p[0] = p[2]

def p_value_list(p):
    """value_list : value
                    | value COMMA value_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value(p):
    """value : NUMBER
            | STRING"""
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Sintax error in the file {__file__}, token: {p.type}, value: '{p.value}'")
    else:
        print(f"Sintax error in the file {__file__}, in end of file.")

matrix_parser = yacc.yacc()
import ply.yacc as yacc
from .matrix_lexer import tokens

def p_statement_create(p):
    """statement : CREATE ID matrix SEMICOLON"""
    p[0] = ('CREATE', p[2], p[3])

def p_statement_print(p):
    """statement : PRINT ID SEMICOLON"""
    p[0] = ('PRINT', p[2])

def p_statement_assign(p):
    """statement : ID ASSIGN CREATE matrix SEMICOLON"""
    p[0] = ('ASSIGN', p[1], ('CREATE', p[3], p[4]))

def p_matrix(p):
    """matrix : LBRACKET rows RBRACKET"""
    p[0] = p[2]

def p_rows(p):
    """rows : row
                | row COMMA rows"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_row(p):
    """row : LBRACKET value_list RBRACKET"""
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
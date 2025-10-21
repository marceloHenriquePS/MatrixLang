import ply.yacc as yacc
from .matrix_lexer import tokens

def p_statements(p):
    """statements : statement
                    | statement statements"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement_create(p):
    """statement : CREATE ID matrix SEMICOLON"""
    p[0] = ('CREATE', p[2], p[3])

def p_statement_assign(p):
    """statement : ID ASSIGN expression SEMICOLON"""
    p[0] = ('ASSIGN', p[1], p[3])

def p_statement_print(p):
    """statement : PRINT LPAREN expression RPAREN SEMICOLON"""
    p[0] = ('PRINT', p[3])

def p_expression_msum(p):
    """expression : MSUM LPAREN expression_list RPAREN"""
    p[0] = ('MSUM',) + tuple(p[3])

def p_expression_msub(p):
    """expression : MSUB LPAREN expression_list RPAREN"""
    p[0] = ('MSUB',) + tuple(p[3])

def p_expression_mmult(p):
    """expression : MMULT LPAREN expression_list RPAREN"""
    p[0] = ('MMULT',) + tuple(p[3])

def p_expression_mdiv(p):
    """expression : MDIV LPAREN expression_list RPAREN"""
    p[0] = ('MDIV',) + tuple(p[3])

def p_expression_minverse(p):
    """expression : MINVERSE LPAREN expression RPAREN"""
    p[0] = ('MINVERSE', p[3])

def p_expression_mtranspose(p):
    """expression : MTRANSPOSE LPAREN expression RPAREN"""
    p[0] = ('MTRANSPOSE', p[3])

def p_expression_mrank(p):
    """expression : MRANK LPAREN expression RPAREN"""
    p[0] = ('MRANK', p[3])

def p_expression_mdet(p):
    """expression : MDET LPAREN expression RPAREN"""
    p[0] = ('MDET', p[3])

def p_expression_eigenvalues(p):
    """expression : MEIGENVALUES LPAREN expression RPAREN"""
    p[0] = ('MEIGENVALUES', p[3])

def p_expression_eigenvectors(p):
    """expression : MEIGENVECTORS LPAREN expression RPAREN"""
    p[0] = ('MEIGENVECTORS', p[3])

def p_expression_triupper(p):
    """expression : MTRIUPPER LPAREN expression RPAREN"""
    p[0] = ('MTRIUPPER', p[3])

def p_expression_trilower(p):
    """expression : MTRILOWER LPAREN expression RPAREN"""
    p[0] = ('MTRILOWER', p[3])

def p_expression_mescale(p):
    """expression : MESCALE LPAREN expression RPAREN"""
    p[0] = ('MESCALE', p[3])

def p_expression_list(p):
    """expression_list : expression
                        | expression COMMA expression_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression(p):
    """expression : matrix
                    | ID"""
    if len(p) == 2:
        p[0] = p[1]

def p_matrix(p):
    """matrix : LBRACKET rows RBRACKET"""
    p[0] = p[2]

def p_row(p):
    """row : LBRACKET value_list RBRACKET"""
    p[0] = p[2]

def p_rows(p):
    """rows : row
                | row COMMA rows"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_value(p):
    """value : NUMBER
            | STRING
            | ID"""
    p[0] = p[1]

def p_value_list(p):
    """value_list : value
                    | value COMMA value_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_error(p):
    if p:
        print(f"Syntax error, token: {p.type}, value: '{p.value}'")
    else:
        print(f"Syntax error at end of file.")

matrix_parser = yacc.yacc( write_tables=False, debug=False)
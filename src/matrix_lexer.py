import ply.lex as lex

tokens = (
    'CREATE',
    'PRINT', 
    'ASSIGN',
    'ID',
    'NUMBER',
    'STRING',
    'COMMA',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'MSUM',
    'MSUB',
    'MMULT',
    'MDIV',
    'MINVERSE',
    'MTRANSPOSE',
    'MRANK',
    'MDET',
    'MEIGENVALUES',
    'MEIGENVECTORS',
    'MTRIUPPER',
    'MTRILOWER',
    'MESCALE'
)

reserved = {
    'create': 'CREATE',
    'print': 'PRINT',
    'msum': 'MSUM',
    'msub': 'MSUB',
    'mmult': 'MMULT',
    'mdiv': 'MDIV',
    'minverse': 'MINVERSE',
    'mtranspose': 'MTRANSPOSE',
    'mrank': 'MRANK',
    'mdet': 'MDET',
    'meigenvalues': 'MEIGENVALUES',
    'meigenvectors': 'MEIGENVECTORS',
    'mtrilower': 'MTRILOWER',
    'mtriupper': 'MTRIUPPER',
    'mescale': 'MESCALE'
    }

t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error lexical in the file {__file__} : invalid character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
import ply.lex as lex

tokens = (
    'CREATE',
    'ID',
    'NUMBER',
    'STRING',
    'COMMA',
    'SEMICOLON',
)

literals = '[]()'

reserved = {
    'create': 'CREATE'
    }

t_COMMA = r','
t_SEMICOLON = r';'

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
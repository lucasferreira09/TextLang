import ply.lex as lex

reserved = {
    'LOAD': 'LOAD',
    'LINES': 'LINES',
    'WORDS': 'WORDS',
    'CHARACTERS': 'CHARACTERS',
    'COUNT': 'COUNT',
    'SEARCH': 'SEARCH',
    'FREQUENCY': 'FREQUENCY',
    'TOP': 'TOP',
    'IGNORE': 'IGNORE',
    'REPLACE': 'REPLACE',
    'WITH': 'WITH',
    'EXPORT': 'EXPORT',
}


tokens = [
    'STRING',
    'NUMBER',
    'ID',
    'NEWLINE'
] + list(reserved.values())


literals = [',']


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

    t.type = reserved.get(t.value, 'ID')

    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    return t

t_ignore = ' \t'

def t_COMMENT(t):
    r'\#[^\n]*'
    pass

def t_error(t):
    print(f"Caractere não suportado '{t.value[0]}' em linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()



if __name__ == '__main__':
    data = '''
LOAD "dom_casmurro.txt"

LINES
WORDS
COUNT "Capitu"
TOP 10
'''

    lexer.input(data)

    for token in lexer:
        print(token)
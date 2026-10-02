import ply.yacc as yacc

from lexer import tokens


def p_program(p):
    '''program : lines'''
    p[0] = p[1]


def p_lines_multiple(p):
    '''lines : lines line'''
    p[0] = p[1] + p[2]


def p_lines_single(p):
    '''lines : line'''
    p[0] = p[1]


def p_line_command(p):
    '''line : command'''
    p[0] = [p[1]]


def p_line_empty(p):
    '''line : NEWLINE'''
    p[0] = []

def p_load_command(p):
    '''command : LOAD STRING NEWLINE'''
    p[0] = ('LOAD', p[2])


def p_statistic_command(p):
    '''command : LINES NEWLINE
                | WORDS NEWLINE
                | CHARACTERS NEWLINE'''
    p[0] = (p[1],)


def p_count_command(p):
    '''command : COUNT STRING NEWLINE'''
    p[0] = ('COUNT', p[2])


def p_search_command(p):
    '''command : SEARCH STRING NEWLINE'''
    p[0] = ('SEARCH', p[2])


def p_frequency_command(p):
    '''command : FREQUENCY NEWLINE'''
    p[0] = ('FREQUENCY',)


def p_top_command(p):
    '''command : TOP NUMBER NEWLINE'''
    p[0] = ('TOP', p[2])


def p_ignore_command(p):
    '''command : IGNORE string_list NEWLINE'''
    p[0] = ('IGNORE', p[2])


def p_string_list_multiple(p):
    '''string_list : string_list ',' STRING'''
    p[0] = p[1] + [p[3]]


def p_string_list_single(p):
    '''string_list : STRING'''
    p[0] = [p[1]]


def p_replace_command(p):
    '''command : REPLACE STRING WITH STRING NEWLINE'''
    p[0] = ('REPLACE', p[2], p[4])


def p_export_command(p):
    '''command : EXPORT STRING NEWLINE'''
    p[0] = ('EXPORT', p[2])


def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' (linha {p.lineno})")
    else:
        print("Erro de sintaxe em EOF")


parser = yacc.yacc()
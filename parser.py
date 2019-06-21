import ply.yacc as yacc
from miniPascal import tokens
import miniPascal
import sys

VERBOSE = 1
errors = 0


def p_program(p):
    'program : declaration_list'
    pass


def p_declaration_list_1(p):
    'declaration_list : declaration_list  declaration'
    pass


def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass


def p_declaration(p):
    '''declaration : header_declaration
                            | var_declaration
                            | function_declaration
                            | procedure_declaration'''
    pass


def p_header_declaration_1(p):
    'header_declaration : PROGRAM ID SEMICOLON'
    pass


def p_header_declaration_2(p):
    'header_declaration : USES ID header_declaration_3 SEMICOLON'
    pass


def p_header_declaration_3(p):
    '''header_declaration_3 : COMMA ID header_declaration_3 
                                                | empty'''
    pass


def p_var_declaration_1(p):
    'var_declaration : VAR var_declaration_2'
    pass


def p_var_declaration_2(p):
    '''var_declaration_2 : ID var_declaration_3 COLON type_specifier SEMICOLON var_declaration_4'''
    pass


def p_var_declaration_3(p):
    '''var_declaration_3 : COMMA ID var_declaration_3 
                                            | empty'''
    pass


def p_var_declaration_4(p):
    '''var_declaration_4 : var_declaration_2 
                                    | empty'''
    pass


def p_empty(p):
    'empty :'
    pass


def p_math(p):
    'math : factor mathi'
    pass


def p_mathi(p):
    '''mathi : type_op_math factor mathi
             | empty'''
    pass


def p_factor(p):
    '''factor : LPAREN math RPAREN
              | NUMBER
              | ID'''
    pass


def p_type_specifier_1(p):
    'type_specifier : INTEGER'
    pass


def p_type_specifier_3(p):
    'type_specifier : REAL'
    pass


def p_type_specifier_4(p):
    'type_specifier : CHAR'
    pass


def p_type_specifier_5(p):
    'type_specifier : BOOLEAN'
    pass


def p_type_specifier_6(p):
    'type_specifier : DOUBLE'
    pass


def p_procedure_declaration(p):
    'procedure_declaration : BEGIN instruction END DOT'
    pass


def p_instruction(p):
    '''instruction : asignation instruction
                        | writing instruction
                        | cycles instruction
                        | callFunctions instruction
                                    | empty'''
    pass


def p_callFunctions(p):
    'callFunctions : ID LPAREN params RPAREN '
    pass


def p_params(p):
    'params : math params2'
    pass


def p_params2(p):
    '''params2 : COMMA math 
                | empty'''
    pass


def p_instruction_one_line(p):
    '''instruction_one_line : asignation
                        | writing
                        | cycles'''
    pass


def p_id_text_l(p):
    '''id_text_l : callFunctions COMMA id_text_l 
               | ID COMMA id_text_l            
               | empty'''
    pass


def p_id_text_r(p):
    '''id_text_r : COMMA callFunctions id_text_r
               | COMMA ID id_text_r
               | empty'''
    pass


def p_writing_1(p):
    '''writing : WRITELN LPAREN id_text_l TEXT id_text_r RPAREN SEMICOLON
                | WRITELN LPAREN id_num RPAREN SEMICOLON
                | READLN LPAREN ID RPAREN SEMICOLON
                | READLN LPAREN RPAREN SEMICOLON
                | READLN SEMICOLON'''
    pass


def p_writing_2(p):
    'writing : WRITELN SEMICOLON'
    pass


def p_asignation(p):
    '''asignation : ID EQUAL callFunctions SEMICOLON
                | ID EQUAL math SEMICOLON 
                | ID EQUAL boolean SEMICOLON
                | ID EQUAL TEXT SEMICOLON'''
    pass


def p_asignation_for(p):
    'asignation_for : ID EQUAL id_num'
    pass


def p_cycles(p):
    'cycles : type_cycle'
    pass


def p_type_cycle(p):
    '''type_cycle : while
                    | if 
                    | for 
                    | cycles instruction'''
    pass  # // TODO recordar que falta el FOR


def p_while(p):
    '''while : WHILE internexpression op_cycle DO otherBegin'''  # //TODO La expresion interna puede ser una operacion
    pass


def p_if(p):
    '''if : IF internexpression op_cycle THEN otherBegin_if 
            | IF internexpression op_cycle THEN instruction_one_line
            | IF internexpression op_cycle THEN otherBegin_if ELSE otherBegin
            | IF internexpression op_cycle THEN otherBegin_if ELSE instruction_one_line
            | IF internexpression op_cycle THEN instruction_one_line ELSE otherBegin
            | IF internexpression op_cycle THEN instruction_one_line ELSE instruction_one_line'''
    pass


def p_for(p):
    '''for : FOR asignation_for TO id_num DO otherBegin
            | FOR asignation_for DOWNTO id_num DO otherBegin'''
    pass


def p_op_cycle(p):
    '''op_cycle : op_logic internexpression op_cycle
                                        | empty'''


def p_internexpression_1(p):
    'internexpression : parentheses'
    pass


def p_internexpression_2(p):
    'internexpression : expression'
    pass


def p_parentheses(p):
    '''parentheses : LPAREN expression RPAREN'''
    pass


def p_expression_1(p):
    '''expression : math type_op math
                    | ID
                    | math ISEQUAL boolean
                    | boolean ISEQUAL math
                    | expression2'''
    pass


def p_expression2(p):
    '''expression2 : TEXT type_op TEXT
                  | TEXT type_op ID'''  # TODO Tratar de arreglar esto ID type_op TEXT
    pass


# def p_expression_2(p):
#     'expression : ID type_op ID'
#     pass

# def p_expression_1(p):
#     'expression : ID type_op math'
#     pass


# def p_expression_2(p):
#     'expression : ID'
#     pass


# def p_expression_3(p):
#     '''expression : ID ISEQUAL math
#                   | math ISEQUAL boolean'''
#     pass


# def p_expression_4(p):
#     '''expression : ID type_op TEXT
#                   | TEXT type_op TEXT
#                   | TEXT type_op ID'''
#     pass


def p_type_op_1(p):
    'type_op : LESSEQUAL'
    pass


def p_type_op_2(p):
    'type_op : LESS'
    pass


def p_type_op_3(p):
    'type_op : GREATER'
    pass


def p_type_op_4(p):
    'type_op : GREATEREQUAL'
    pass


def p_type_op_5(p):
    'type_op : DEQUAL'
    pass


def p_type_op_6(p):
    'type_op : DISTINT'
    pass


def p_type_op_6(p):
    'type_op : ISEQUAL'
    pass


def p_type_op_math_1(p):
    'type_op_math : PLUS'
    pass


def p_type_op_math_2(p):
    'type_op_math : MINUS'
    pass


def p_type_op_math_3(p):
    'type_op_math : TIMES'
    pass


def p_type_op_math_4(p):
    'type_op_math : DIVIDE'
    pass


def p_type_op_math_5(p):
    'type_op_math : MOD'
    pass


def p_op_logic_1(p):
    'op_logic : AND'
    pass


def p_op_logic_2(p):
    'op_logic : OR'
    pass


def p_op_logic_3(p):
    'op_logic : XOR'
    pass


def p_op_logic_4(p):
    'op_logic : NOT'
    pass


def p_id_num(p):
    '''id_num : NUMBER
                | ID'''


def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''


def p_otherBegin(p):
    'otherBegin : BEGIN instruction END SEMICOLON instruction'
    pass


def p_otherBegin_if(p):
    'otherBegin_if : BEGIN instruction END instruction'
    pass


def p_Begin_function(p):
    '''Begin_function : var_declaration BEGIN instruction END SEMICOLON instruction
                        | BEGIN instruction END SEMICOLON instruction'''
    pass


def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN fun_param RPAREN COLON type_specifier SEMICOLON Begin_function
                            | PROCEDURE ID LPAREN fun_param RPAREN SEMICOLON Begin_function
                            | PROCEDURE ID SEMICOLON Begin_function'''
    pass


def p_fun_param_1(p):
    '''fun_param : ID fun_param_2 COLON type_specifier fun_param
                 | SEMICOLON ID fun_param_2 COLON type_specifier fun_param
                 | empty'''
    pass


def p_fun_param_2(p):
    '''fun_param_2 : COMMA ID fun_param_2
                            | empty'''
    pass


def p_error(p):
    global errors
    if VERBOSE:
        if p is not None:
            print("Error sintactico en la linea " + str(p.lexer.lineno) +
                  " No se esperaba el token  " + str(p.value))
            errors += 1
        else:
            print("Error sintantico en la linea: " +
                  str(cminus_lexer.lexer.lineno))
            errors += 1

    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'testingsFiles/recurisividad.pas'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, tracking=True)
    if not errors:
        print("Congratulations, your code is vientos")
    # input()

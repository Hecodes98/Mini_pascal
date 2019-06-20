import ply.yacc as yacc
from miniPascal import tokens
import miniPascal
import sys

VERBOSE = 1


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


def p_procedure_declaration(p):
    'procedure_declaration : BEGIN instruction END DOT'
    pass


def p_instruction(p):
    '''instruction : asignation instruction
                        | writing instruction
                        | cycles instruction
                                    | empty'''
    pass


def p_instruction_one_line(p):
    '''instruction_one_line : asignation
                        | writing
                        | cycles'''
    pass


def p_writing_1(p):
    '''writing : WRITELN LPAREN TEXT RPAREN SEMICOLON
                | WRITELN LPAREN id_num RPAREN SEMICOLON   '''
    pass


def p_writing_2(p):
    'writing : WRITELN SEMICOLON'
    pass


def p_asignation(p):
    'asignation : ID EQUAL id_num SEMICOLON'
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
    'expression : ID type_op ID'
    pass


def p_id_num(p):
    '''id_num : NUMBER
                | ID'''


def p_expression_2(p):
    'expression : id_num type_op id_num'
    pass


def p_expression_5(p):
    'expression : id_num'
    pass


def p_expression_6(p):
    '''expression : id_num type_op_math id_num ISEQUAL id_num'''
    pass


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
    'type_op : ISEQUAL'
    pass


def p_type_op_6(p):
    'type_op : DEQUAL'
    pass


def p_type_op_7(p):
    'type_op : DISTINT'
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


def p_otherBegin(p):
    'otherBegin : BEGIN instruction END SEMICOLON instruction'
    pass


def p_otherBegin_if(p):
    'otherBegin_if : BEGIN instruction END instruction'
    pass

# def p_fun_declaration(p):
# 	'fun_declaration : type_specifier ID LPAREN params RPAREN compount_stmt'
# 	pass

# def p_params_1(p):
# 	'params : param_list'
# 	pass

# def p_params_2(p):
# 	'params : VOID'
# 	pass

# def p_param_list_1(p):
# 	'param_list : param_list COMMA param'
# 	pass

# def p_param_list_2(p):
# 	'param_list : param'
# 	pass

# def p_param_list_3(p):
# 	'param_list : empty'
# 	pass

# def p_param_1(p):
# 	'param : type_specifier ID'
# 	pass

# def p_param_2(p):
# 	'param : type_specifier ID LBRACKET RBRACKET'
# 	pass

# def p_compount_stmt(p):
# 	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
# 	pass

# def p_local_declarations_1(p):
# 	'local_declarations : local_declarations var_declaration'
# 	pass

# def p_local_declarations_2(p):
# 	'local_declarations : empty'
# 	pass

# def p_statement_list_1(p):
# 	'statement_list : statement_list statement'
# 	pass

# def p_statement_list_2(p):
# 	'statement_list : empty'
# 	pass

# def p_statement(p):
# 	'''statement : expression_stmt
# 				| compount_stmt
# 				| selection_stmt
# 				| iteration_stmt
# 				| return_stmt
# 	'''
# 	pass

# def p_expression_stmt_1(p):
# 	'expression_stmt : expression SEMICOLON'
# 	pass

# def p_expression_stmt_2(p):
# 	'expression_stmt : SEMICOLON'
# 	pass

# def p_selection_stmt_1(p):
# 	'selection_stmt : IF LPAREN expression RPAREN statement'
# 	pass

# def p_selection_stmt_2(p):
# 	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
# 	pass

# def p_selection_stmt_3(p):
# 	'selection_stmt : SWITCH LPAREN var RPAREN statement'
# 	pass

# def p_selection_stmt_4(p):
# 	'selection_stmt : CASE NUMBER COLON statement BREAK SEMICOLON'
# 	pass

# def p_selection_stmt_5(p):
# 	'selection_stmt : DEFAULT COLON statement BREAK SEMICOLON'
# 	pass

# def p_iteration_stmt_1(p):
# 	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
# 	pass


# def p_iteration_stmt_2(p):
# 	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
# 	pass

# def p_return_stmt_1(p):
# 	'return_stmt : RETURN SEMICOLON'
# 	pass

# def p_return_stmt_2(p):
# 	'return_stmt : RETURN expression SEMICOLON'
# 	pass

# def p_expression_1(p):
# 	'expression : var EQUAL expression'
# 	pass

# def p_expression_2(p):
# 	'expression : simple_expression'
# 	pass

# def p_expression_3(p):
# 	'expression : var EQUAL AMPERSANT ID'
# 	pass

# def p_var_1(p):
# 	'var : ID'
# 	pass

# def p_var_2(p):
# 	'var : ID LBRACKET expression RBRACKET'
# 	pass

# def p_simple_expression_1(p):
# 	'simple_expression : additive_expression relop additive_expression'
# 	pass

# def p_simple_expression_2(p):
# 	'simple_expression : additive_expression'
# 	pass


# def p_relop(p):
# 	'''relop : LESS
# 			| LESSEQUAL
# 			| GREATER
# 			| GREATEREQUAL
# 			| DEQUAL
# 			| DISTINT
# 			| ISEQUAL
# 	'''
# 	pass

# def p_additive_expression_1(p):
# 	'''additive_expression : additive_expression addop term

#         '''
# 	pass

# def p_additive_expression_2(p):
# 	'additive_expression : term'
# 	pass

# def p_additive_expression_3(p):
# 	'additive_expression : term MINUSMINUS'
# 	pass

# def p_additive_expression_4(p):
# 	'additive_expression : term PLUSPLUS'
# 	pass

# def p_addop(p):
# 	'''addop : PLUS
# 			| MINUS
# 	'''
# 	pass

# def p_term_1(p):
# 	'term : term mulop factor'
# 	pass

# def p_term_2(p):
# 	'term : factor'
# 	pass


# def p_mulop(p):
# 	'''mulop : 	TIMES
# 				| DIVIDE
# 	'''
# 	pass

# def p_factor_1(p):
# 	'factor : LPAREN expression RPAREN'
# 	pass

# def p_factor_2(p):
# 	'factor : var'
# 	pass

# def p_factor_3(p):
# 	'factor : call'
# 	pass

# def p_factor_4(p):
# 	'factor : NUMBER'
# 	pass


# def p_call(p):
# 	'call : ID LPAREN args RPAREN'
# 	pass

# def p_args(p):
# 	'''args : args_list
# 			| empty
# 	'''
# 	pass

# def p_args_list_1(p):
# 	'args_list : args_list COMMA expression'
# 	pass

# def p_args_list_2(p):
# 	'args_list : expression'
# 	pass

# def p_empty(p):
# 	'empty :'
# 	pass


def p_error(p):
    if VERBOSE:
        if p is not None:
            print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) +
                  " NO SE ESPERABA EL Token  " + str(p.value))
        else:
            print("ERROR SINTACTICO EN LA LINEA: " +
                  str(cminus_lexer.lexer.lineno))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'parser.pas'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, tracking=True)
    print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
    # input()

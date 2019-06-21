
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSOLUTE AMPERSANT AND ARRAY ASM BEGIN BOOLEAN BREAK CASE CHAR CLRSCR COLON COMMA CONST CONSTRUCTOR DEQUAL DESTRUCTOR DISTINT DIVIDE DO DOT DOUBLE DOWNTO ELSE END EQUAL FALSE FILE FLOAT FOR FUNCTION GOTO GREATER GREATEREQUAL HASHTAG ID IF IMPLEMENTATION IN INHERITED INLINE INTEGER INTERFACE ISEQUAL LABEL LBLOCK LBRACKET LESS LESSEQUAL LONG LPAREN MINUS MINUSMINUS MOD NIL NOT NUMBER OBJECT OF OPERATOR OR PACKED PLUS PLUSPLUS PROCEDURE PROGRAM RBLOCK RBRACKET READLN REAL RECORD REINTRODUCE REPEAT RPAREN SELF SEMICOLON SET SHL SHR STRING TEXT THEN TIMES TO TRUE TYPE UNIT UNTIL USES VAR WHILE WITH WRITE WRITELN XORprogram : declaration_listdeclaration_list : declaration_list  declarationdeclaration_list : declarationdeclaration : header_declaration\n                            | var_declaration\n                            | function_declaration\n                            | procedure_declarationheader_declaration : PROGRAM ID SEMICOLONheader_declaration : USES ID header_declaration_3 SEMICOLONheader_declaration_3 : COMMA ID header_declaration_3 \n                                                | emptyvar_declaration : VAR var_declaration_2var_declaration_2 : ID var_declaration_3 COLON type_specifier SEMICOLON var_declaration_4var_declaration_3 : COMMA ID var_declaration_3 \n                                            | emptyvar_declaration_4 : var_declaration_2 \n                                    | emptyempty :math : factor mathimathi : type_op_math factor mathi\n             | emptyfactor : LPAREN math RPAREN\n              | NUMBER\n              | IDtype_specifier : INTEGERtype_specifier : REALtype_specifier : CHARtype_specifier : BOOLEANtype_specifier : DOUBLEprocedure_declaration : BEGIN instruction END DOTinstruction : asignation instruction\n                        | writing instruction\n                        | cycles instruction\n                        | callFunctions instruction\n                                    | emptycallFunctions : ID LPAREN params RPAREN params : math params2params2 : COMMA math \n                | emptyinstruction_one_line : asignation\n                        | writing\n                        | cyclesid_text_l : callFunctions COMMA id_text_l \n               | ID COMMA id_text_l            \n               | emptyid_text_r : COMMA callFunctions id_text_r\n               | COMMA ID id_text_r\n               | emptywriting : WRITELN LPAREN id_text_l TEXT id_text_r RPAREN SEMICOLON\n                | WRITELN LPAREN id_num RPAREN SEMICOLON\n                | READLN LPAREN ID RPAREN SEMICOLON\n                | READLN LPAREN RPAREN SEMICOLON\n                | READLN SEMICOLONwriting : WRITELN SEMICOLONasignation : ID EQUAL callFunctions SEMICOLON\n                | ID EQUAL math SEMICOLON \n                | ID EQUAL boolean SEMICOLON\n                | ID EQUAL TEXT SEMICOLONasignation_for : ID EQUAL id_numcycles : type_cycletype_cycle : while\n                    | if \n                    | for \n                    | cycles instructionwhile : WHILE internexpression op_cycle DO otherBeginif : IF internexpression op_cycle THEN otherBegin_if \n            | IF internexpression op_cycle THEN instruction_one_line\n            | IF internexpression op_cycle THEN otherBegin_if ELSE otherBegin\n            | IF internexpression op_cycle THEN otherBegin_if ELSE instruction_one_line\n            | IF internexpression op_cycle THEN instruction_one_line ELSE otherBegin\n            | IF internexpression op_cycle THEN instruction_one_line ELSE instruction_one_linefor : FOR asignation_for TO id_num DO otherBegin\n            | FOR asignation_for DOWNTO id_num DO otherBeginop_cycle : op_logic internexpression op_cycle\n                                        | emptyinternexpression : parenthesesinternexpression : expressionparentheses : LPAREN expression RPARENexpression : callFunctions\n                    | callFunctions type_op math\n                    | callFunctions type_op callFunctions\n                    | math type_op math\n                    | ID\n                    | math ISEQUAL boolean\n                    | boolean ISEQUAL math\n                    | expression2expression2 : TEXT type_op TEXT\n                  | TEXT type_op IDtype_op : LESSEQUALtype_op : LESStype_op : GREATERtype_op : GREATEREQUALtype_op : DEQUALtype_op : ISEQUALtype_op_math : PLUStype_op_math : MINUStype_op_math : TIMEStype_op_math : DIVIDEtype_op_math : MODop_logic : ANDop_logic : ORop_logic : XORop_logic : NOTid_num : NUMBER\n                | IDboolean : TRUE\n                | FALSEotherBegin : BEGIN instruction END SEMICOLON instructionotherBegin_if : BEGIN instruction END instructionBegin_function : var_declaration BEGIN instruction END SEMICOLON instruction\n                        | BEGIN instruction END SEMICOLON instructionfunction_declaration : FUNCTION ID LPAREN fun_param RPAREN COLON type_specifier SEMICOLON Begin_function\n                            | PROCEDURE ID LPAREN fun_param RPAREN SEMICOLON Begin_function\n                            | PROCEDURE ID SEMICOLON Begin_functionfun_param : ID fun_param_2 COLON type_specifier fun_param\n                 | SEMICOLON ID fun_param_2 COLON type_specifier fun_param\n                 | emptyfun_param_2 : COMMA ID fun_param_2\n                            | empty'
    
_lr_action_items = {'REAL':([131,186,187,215,],[175,175,175,175,]),'DO':([43,45,46,47,48,51,52,53,54,55,93,95,97,103,116,120,125,143,144,145,146,148,149,150,151,152,154,155,156,157,158,164,189,192,],[-23,-106,-18,-79,-18,-86,-83,-76,-107,-77,147,-75,-19,-21,-104,-24,-24,-87,-88,-85,-18,-81,-80,-18,-82,-84,-78,-22,193,-105,194,-36,-74,-20,]),'LESS':([42,43,47,48,49,52,97,103,109,120,150,155,164,192,],[83,-23,83,-18,83,-24,-19,-21,83,-24,-18,-22,-36,-20,]),'TEXT':([17,25,50,61,63,81,82,83,84,85,86,87,89,90,91,92,94,114,118,160,163,195,201,],[42,42,42,-18,122,-92,-91,-90,-93,-94,143,-89,-100,-102,42,-103,-101,161,-45,-18,-18,-43,-44,]),'THEN':([43,45,47,48,51,52,53,54,55,64,95,97,103,120,125,127,143,144,145,146,148,149,150,151,152,154,155,164,189,192,],[-23,-106,-79,-18,-86,-83,-76,-107,-77,-18,-75,-19,-21,-24,-24,172,-87,-88,-85,-18,-81,-80,-18,-82,-84,-78,-22,-36,-74,-20,]),'NUMBER':([17,25,50,61,62,63,81,82,83,84,85,87,88,89,90,91,92,94,96,98,99,100,101,102,104,105,106,107,110,111,112,166,],[43,43,43,116,43,43,-92,-91,-90,-93,-94,-89,43,-100,-102,43,-103,-101,43,-98,-97,-95,43,-96,-99,43,-94,43,116,116,116,43,]),'CHAR':([131,186,187,215,],[178,178,178,178,]),'LESSEQUAL':([42,43,47,48,49,52,97,103,109,120,150,155,164,192,],[87,-23,87,-18,87,-24,-19,-21,87,-24,-18,-22,-36,-20,]),'WHILE':([4,18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,172,173,183,190,191,200,203,204,205,207,208,209,210,220,221,226,227,228,232,241,242,243,244,245,246,248,251,252,254,],[17,17,17,-62,-35,-63,17,-60,-61,17,-32,-34,-54,-31,-53,-33,17,-36,-58,-57,-55,-56,17,-52,17,17,-65,-50,17,-41,-67,-40,-66,17,-51,-73,-72,17,17,-64,17,-49,17,-71,-70,-69,-68,17,17,-109,-108,]),'PROGRAM':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,220,221,228,229,230,231,232,234,241,242,243,244,245,246,247,248,250,251,252,253,254,],[2,-5,-4,-3,-6,-7,2,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-113,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'USES':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,220,221,228,229,230,231,232,234,241,242,243,244,245,246,247,248,250,251,252,253,254,],[3,-5,-4,-3,-6,-7,3,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-113,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'XOR':([43,45,46,47,48,51,52,53,54,55,64,97,103,120,125,143,144,145,146,148,149,150,151,152,154,155,164,192,],[-23,-106,90,-79,-18,-86,-83,-76,-107,-77,90,-19,-21,-24,-24,-87,-88,-85,90,-81,-80,-18,-82,-84,-78,-22,-36,-20,]),'TRUE':([17,25,50,63,89,90,91,92,94,106,],[45,45,45,45,-100,-102,45,-103,-101,45,]),'MINUS':([43,48,52,120,125,150,155,],[-23,102,-24,-24,-24,102,-22,]),'DOT':([65,],[128,]),'BEGIN':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,73,80,128,134,135,147,164,168,169,170,171,172,173,191,193,194,200,204,205,207,208,209,210,211,214,220,221,226,227,228,229,230,231,232,234,236,241,242,243,244,245,246,247,248,250,251,252,253,254,],[4,-5,-4,-3,-6,-7,4,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,133,-9,-30,183,-114,190,-36,-58,-57,-55,-56,203,-52,-65,190,190,-50,-41,-67,-40,-66,-18,-51,-18,133,-73,-72,190,190,-64,-13,-16,-17,-18,-113,133,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'RPAREN':([37,43,45,47,48,51,52,54,68,74,76,78,97,103,108,109,115,116,117,119,120,121,125,130,136,143,144,145,148,149,150,151,152,153,155,161,164,165,167,175,177,178,179,180,192,198,199,202,217,222,223,235,237,239,240,249,],[-18,-23,-106,-79,-18,-86,-24,-107,129,-18,138,-117,-19,-21,154,155,162,-104,-105,164,-24,-18,-24,174,184,-87,-88,-85,-81,-80,-18,-82,-84,155,-22,-18,-36,-37,-39,-26,-29,-27,-28,-25,-20,224,-48,-38,-18,-18,-18,-18,-115,-46,-47,-116,]),'SEMICOLON':([15,16,23,29,35,37,40,41,43,45,48,54,74,79,97,103,120,122,123,124,125,126,129,142,150,155,162,164,174,175,176,177,178,179,180,184,192,212,216,217,224,233,235,238,],[38,-18,60,67,73,75,80,-11,-23,-106,-18,-107,75,-18,-19,-21,-24,168,169,170,-24,171,173,-10,-18,-22,200,-36,210,-26,211,-29,-27,-28,-25,214,-20,232,236,75,241,248,75,251,]),'PLUS':([43,48,52,120,125,150,155,],[-23,100,-24,-24,-24,100,-22,]),'TO':([58,116,157,159,],[111,-104,-105,-59,]),'COMMA':([16,34,43,48,77,79,97,103,113,117,120,121,132,137,150,155,161,164,188,192,196,222,223,],[39,71,-23,-18,140,39,-19,-21,160,163,-24,166,71,140,-18,-22,197,-36,140,-20,163,197,197,]),'COLON':([34,70,72,77,132,137,138,139,141,181,185,188,218,],[-18,131,-15,-18,-18,-18,186,187,-119,-14,215,-18,-118,]),'$end':([5,6,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,220,221,228,229,230,231,232,234,241,242,243,244,245,246,247,248,250,251,252,253,254,],[-5,0,-4,-3,-6,-7,-1,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-113,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'FUNCTION':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,220,221,228,229,230,231,232,234,241,242,243,244,245,246,247,248,250,251,252,253,254,],[1,-5,-4,-3,-6,-7,1,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-113,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'END':([4,18,19,20,21,26,27,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,173,182,183,190,191,200,203,204,205,207,208,209,210,213,219,220,221,225,228,241,242,243,244,245,246,251,252,254,],[-18,-18,-18,-62,-35,-63,65,-18,-60,-61,-18,-32,-34,-54,-31,-53,-33,-18,-36,-58,-57,-55,-56,-52,212,-18,-18,-65,-50,-18,-41,-67,-40,-66,-18,-51,233,238,-73,-72,242,-64,-49,-18,-71,-70,-69,-68,-18,-109,-108,]),'DIVIDE':([43,48,52,120,125,150,155,],[-23,98,-24,-24,-24,98,-22,]),'FOR':([4,18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,172,173,183,190,191,200,203,204,205,207,208,209,210,220,221,226,227,228,232,241,242,243,244,245,246,248,251,252,254,],[22,22,22,-62,-35,-63,22,-60,-61,22,-32,-34,-54,-31,-53,-33,22,-36,-58,-57,-55,-56,22,-52,22,22,-65,-50,22,-41,-67,-40,-66,22,-51,-73,-72,22,22,-64,22,-49,22,-71,-70,-69,-68,22,22,-109,-108,]),'EQUAL':([24,59,206,],[63,112,63,]),'GREATEREQUAL':([42,43,47,48,49,52,97,103,109,120,150,155,164,192,],[81,-23,81,-18,81,-24,-19,-21,81,-24,-18,-22,-36,-20,]),'ELSE':([18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,164,168,169,170,171,173,191,200,204,205,207,208,209,210,220,221,228,241,242,243,244,245,246,251,252,254,],[-18,-18,-62,-35,-63,-18,-60,-61,-18,-32,-34,-54,-31,-53,-33,-36,-58,-57,-55,-56,-52,-65,-50,-41,226,-40,227,-18,-51,-73,-72,-64,-49,-18,-71,-70,-69,-68,-18,-109,-108,]),'WRITELN':([4,18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,172,173,183,190,191,200,203,204,205,207,208,209,210,220,221,226,227,228,232,241,242,243,244,245,246,248,251,252,254,],[23,23,23,-62,-35,-63,23,-60,-61,23,-32,-34,-54,-31,-53,-33,23,-36,-58,-57,-55,-56,23,-52,23,23,-65,-50,23,-41,-67,-40,-66,23,-51,-73,-72,23,23,-64,23,-49,23,-71,-70,-69,-68,23,23,-109,-108,]),'LPAREN':([14,17,23,24,25,29,35,50,52,62,63,81,82,83,84,85,87,88,89,90,91,92,94,96,98,99,100,101,102,104,105,106,107,117,125,166,196,223,],[37,50,61,62,50,68,74,107,62,107,107,-92,-91,-90,-93,-94,-89,107,-100,-102,50,-103,-101,107,-98,-97,-95,107,-96,-99,107,-94,107,62,62,107,62,62,]),'INTEGER':([131,186,187,215,],[180,180,180,180,]),'VAR':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,73,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,214,220,221,228,229,230,231,232,234,236,241,242,243,244,245,246,247,248,250,251,252,253,254,],[9,-5,-4,-3,-6,-7,9,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,9,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,9,-73,-72,-64,-13,-16,-17,-18,-113,9,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'TIMES':([43,48,52,120,125,150,155,],[-23,99,-24,-24,-24,99,-22,]),'ID':([1,2,3,4,9,10,17,18,19,20,21,22,25,26,28,30,31,32,37,39,50,56,57,60,61,62,63,66,67,68,69,71,74,75,81,82,83,84,85,86,87,88,89,90,91,92,94,96,98,99,100,101,102,104,105,106,107,110,111,112,133,140,160,163,164,166,168,169,170,171,172,173,175,177,178,179,180,183,190,191,197,200,203,204,205,207,208,209,210,211,217,220,221,226,227,228,232,235,241,242,243,244,245,246,248,251,252,254,],[14,15,16,24,34,35,52,24,24,-62,-35,59,52,-63,24,-60,-61,24,77,79,52,-32,-34,-54,117,120,125,-31,-53,130,-33,132,77,137,-92,-91,-90,-93,-94,144,-89,120,-100,-102,52,-103,-101,125,-98,-97,-95,120,-96,-99,120,-94,120,157,157,157,24,188,196,196,-36,120,-58,-57,-55,-56,206,-52,-26,-29,-27,-28,-25,24,24,-65,223,-50,24,-41,-67,-40,-66,24,-51,34,77,-73,-72,206,206,-64,24,77,-49,24,-71,-70,-69,-68,24,24,-109,-108,]),'PROCEDURE':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,56,57,60,66,67,69,80,128,135,164,168,169,170,171,173,191,200,204,205,207,208,209,210,211,220,221,228,229,230,231,232,234,241,242,243,244,245,246,247,248,250,251,252,253,254,],[10,-5,-4,-3,-6,-7,10,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-114,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-113,-49,-18,-71,-70,-69,-68,-111,-18,-112,-18,-109,-110,-108,]),'IF':([4,18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,172,173,183,190,191,200,203,204,205,207,208,209,210,220,221,226,227,228,232,241,242,243,244,245,246,248,251,252,254,],[25,25,25,-62,-35,-63,25,-60,-61,25,-32,-34,-54,-31,-53,-33,25,-36,-58,-57,-55,-56,25,-52,25,25,-65,-50,25,-41,-67,-40,-66,25,-51,-73,-72,25,25,-64,25,-49,25,-71,-70,-69,-68,25,25,-109,-108,]),'AND':([43,45,46,47,48,51,52,53,54,55,64,97,103,120,125,143,144,145,146,148,149,150,151,152,154,155,164,192,],[-23,-106,89,-79,-18,-86,-83,-76,-107,-77,89,-19,-21,-24,-24,-87,-88,-85,89,-81,-80,-18,-82,-84,-78,-22,-36,-20,]),'FALSE':([17,25,50,63,89,90,91,92,94,106,],[54,54,54,54,-100,-102,54,-103,-101,54,]),'GREATER':([42,43,47,48,49,52,97,103,109,120,150,155,164,192,],[82,-23,82,-18,82,-24,-19,-21,82,-24,-18,-22,-36,-20,]),'DOUBLE':([131,186,187,215,],[177,177,177,177,]),'DEQUAL':([42,43,47,48,49,52,97,103,109,120,150,155,164,192,],[84,-23,84,-18,84,-24,-19,-21,84,-24,-18,-22,-36,-20,]),'READLN':([4,18,19,20,21,26,28,30,31,32,56,57,60,66,67,69,133,164,168,169,170,171,172,173,183,190,191,200,203,204,205,207,208,209,210,220,221,226,227,228,232,241,242,243,244,245,246,248,251,252,254,],[29,29,29,-62,-35,-63,29,-60,-61,29,-32,-34,-54,-31,-53,-33,29,-36,-58,-57,-55,-56,29,-52,29,29,-65,-50,29,-41,-67,-40,-66,29,-51,-73,-72,29,29,-64,29,-49,29,-71,-70,-69,-68,29,29,-109,-108,]),'DOWNTO':([58,116,157,159,],[110,-104,-105,-59,]),'BOOLEAN':([131,186,187,215,],[179,179,179,179,]),'ISEQUAL':([42,43,44,45,47,48,49,52,54,97,103,109,120,150,155,164,192,],[85,-23,88,-106,85,-18,106,-24,-107,-19,-21,106,-24,-18,-22,-36,-20,]),'NOT':([43,45,46,47,48,51,52,53,54,55,64,97,103,120,125,143,144,145,146,148,149,150,151,152,154,155,164,192,],[-23,-106,92,-79,-18,-86,-83,-76,-107,-77,92,-19,-21,-24,-24,-87,-88,-85,92,-81,-80,-18,-82,-84,-78,-22,-36,-20,]),'OR':([43,45,46,47,48,51,52,53,54,55,64,97,103,120,125,143,144,145,146,148,149,150,151,152,154,155,164,192,],[-23,-106,94,-79,-18,-86,-83,-76,-107,-77,94,-19,-21,-24,-24,-87,-88,-85,94,-81,-80,-18,-82,-84,-78,-22,-36,-20,]),'MOD':([43,48,52,120,125,150,155,],[-23,104,-24,-24,-24,104,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'id_text_l':([61,160,163,],[114,195,201,]),'fun_param_2':([77,137,188,],[139,185,218,]),'otherBegin':([147,193,194,226,227,],[191,220,221,244,246,]),'id_num':([61,110,111,112,],[115,156,158,159,]),'boolean':([17,25,50,63,91,106,],[44,44,44,123,44,152,]),'type_specifier':([131,186,187,215,],[176,216,217,235,]),'declaration_list':([0,],[13,]),'header_declaration_3':([16,79,],[40,142,]),'if':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'asignation_for':([22,],[58,]),'for':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'type_op':([42,47,49,109,],[86,96,105,105,]),'internexpression':([17,25,91,],[46,64,146,]),'writing':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[18,18,18,18,18,18,204,18,18,18,18,204,204,18,18,18,18,]),'var_declaration':([0,13,73,214,236,],[5,5,134,134,134,]),'op_logic':([46,64,146,],[91,91,91,]),'program':([0,],[6,]),'params':([62,],[119,]),'callFunctions':([4,17,18,19,25,28,32,50,61,63,91,96,133,160,163,183,190,197,203,209,232,242,248,251,],[19,47,19,19,47,19,19,47,113,124,47,148,19,113,113,19,19,222,19,19,19,19,19,19,]),'factor':([17,25,50,62,63,88,91,96,101,105,107,166,],[48,48,48,48,48,48,48,48,150,48,48,48,]),'Begin_function':([73,214,236,],[135,234,250,]),'empty':([4,16,18,19,28,32,34,37,46,48,61,64,74,77,79,121,132,133,137,146,150,160,161,163,183,188,190,203,209,211,217,222,223,232,235,242,248,251,],[21,41,21,21,21,21,72,78,95,103,118,95,78,141,41,167,72,21,141,95,103,118,199,118,21,141,21,21,21,231,78,199,199,21,78,21,21,21,]),'id_text_r':([161,222,223,],[198,239,240,]),'header_declaration':([0,13,],[7,7,]),'mathi':([48,150,],[97,192,]),'var_declaration_4':([211,],[229,]),'var_declaration_2':([9,211,],[33,230,]),'var_declaration_3':([34,132,],[70,181,]),'fun_param':([37,74,217,235,],[76,136,237,249,]),'instruction_one_line':([172,226,227,],[205,243,245,]),'params2':([121,],[165,]),'declaration':([0,13,],[8,36,]),'op_cycle':([46,64,146,],[93,127,189,]),'expression2':([17,25,50,91,],[51,51,51,51,]),'parentheses':([17,25,91,],[53,53,53,]),'function_declaration':([0,13,],[11,11,]),'procedure_declaration':([0,13,],[12,12,]),'instruction':([4,18,19,28,32,133,183,190,203,209,232,242,248,251,],[27,56,57,66,69,182,213,219,225,228,247,252,253,254,]),'asignation':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[28,28,28,28,28,28,207,28,28,28,28,207,207,28,28,28,28,]),'type_cycle':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'while':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'math':([17,25,50,62,63,88,91,96,105,107,166,],[49,49,109,121,126,145,49,149,151,153,202,]),'type_op_math':([48,150,],[101,101,]),'otherBegin_if':([172,],[208,]),'cycles':([4,18,19,28,32,133,172,183,190,203,209,226,227,232,242,248,251,],[32,32,32,32,32,32,209,32,32,32,32,209,209,32,32,32,32,]),'expression':([17,25,50,91,],[55,55,108,55,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','parser.py',11),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_1','parser.py',16),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list_2','parser.py',21),
  ('declaration -> header_declaration','declaration',1,'p_declaration','parser.py',26),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',27),
  ('declaration -> function_declaration','declaration',1,'p_declaration','parser.py',28),
  ('declaration -> procedure_declaration','declaration',1,'p_declaration','parser.py',29),
  ('header_declaration -> PROGRAM ID SEMICOLON','header_declaration',3,'p_header_declaration_1','parser.py',34),
  ('header_declaration -> USES ID header_declaration_3 SEMICOLON','header_declaration',4,'p_header_declaration_2','parser.py',39),
  ('header_declaration_3 -> COMMA ID header_declaration_3','header_declaration_3',3,'p_header_declaration_3','parser.py',44),
  ('header_declaration_3 -> empty','header_declaration_3',1,'p_header_declaration_3','parser.py',45),
  ('var_declaration -> VAR var_declaration_2','var_declaration',2,'p_var_declaration_1','parser.py',50),
  ('var_declaration_2 -> ID var_declaration_3 COLON type_specifier SEMICOLON var_declaration_4','var_declaration_2',6,'p_var_declaration_2','parser.py',55),
  ('var_declaration_3 -> COMMA ID var_declaration_3','var_declaration_3',3,'p_var_declaration_3','parser.py',60),
  ('var_declaration_3 -> empty','var_declaration_3',1,'p_var_declaration_3','parser.py',61),
  ('var_declaration_4 -> var_declaration_2','var_declaration_4',1,'p_var_declaration_4','parser.py',66),
  ('var_declaration_4 -> empty','var_declaration_4',1,'p_var_declaration_4','parser.py',67),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',72),
  ('math -> factor mathi','math',2,'p_math','parser.py',77),
  ('mathi -> type_op_math factor mathi','mathi',3,'p_mathi','parser.py',82),
  ('mathi -> empty','mathi',1,'p_mathi','parser.py',83),
  ('factor -> LPAREN math RPAREN','factor',3,'p_factor','parser.py',88),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',89),
  ('factor -> ID','factor',1,'p_factor','parser.py',90),
  ('type_specifier -> INTEGER','type_specifier',1,'p_type_specifier_1','parser.py',95),
  ('type_specifier -> REAL','type_specifier',1,'p_type_specifier_3','parser.py',100),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier_4','parser.py',105),
  ('type_specifier -> BOOLEAN','type_specifier',1,'p_type_specifier_5','parser.py',110),
  ('type_specifier -> DOUBLE','type_specifier',1,'p_type_specifier_6','parser.py',115),
  ('procedure_declaration -> BEGIN instruction END DOT','procedure_declaration',4,'p_procedure_declaration','parser.py',120),
  ('instruction -> asignation instruction','instruction',2,'p_instruction','parser.py',125),
  ('instruction -> writing instruction','instruction',2,'p_instruction','parser.py',126),
  ('instruction -> cycles instruction','instruction',2,'p_instruction','parser.py',127),
  ('instruction -> callFunctions instruction','instruction',2,'p_instruction','parser.py',128),
  ('instruction -> empty','instruction',1,'p_instruction','parser.py',129),
  ('callFunctions -> ID LPAREN params RPAREN','callFunctions',4,'p_callFunctions','parser.py',134),
  ('params -> math params2','params',2,'p_params','parser.py',139),
  ('params2 -> COMMA math','params2',2,'p_params2','parser.py',144),
  ('params2 -> empty','params2',1,'p_params2','parser.py',145),
  ('instruction_one_line -> asignation','instruction_one_line',1,'p_instruction_one_line','parser.py',150),
  ('instruction_one_line -> writing','instruction_one_line',1,'p_instruction_one_line','parser.py',151),
  ('instruction_one_line -> cycles','instruction_one_line',1,'p_instruction_one_line','parser.py',152),
  ('id_text_l -> callFunctions COMMA id_text_l','id_text_l',3,'p_id_text_l','parser.py',157),
  ('id_text_l -> ID COMMA id_text_l','id_text_l',3,'p_id_text_l','parser.py',158),
  ('id_text_l -> empty','id_text_l',1,'p_id_text_l','parser.py',159),
  ('id_text_r -> COMMA callFunctions id_text_r','id_text_r',3,'p_id_text_r','parser.py',164),
  ('id_text_r -> COMMA ID id_text_r','id_text_r',3,'p_id_text_r','parser.py',165),
  ('id_text_r -> empty','id_text_r',1,'p_id_text_r','parser.py',166),
  ('writing -> WRITELN LPAREN id_text_l TEXT id_text_r RPAREN SEMICOLON','writing',7,'p_writing_1','parser.py',171),
  ('writing -> WRITELN LPAREN id_num RPAREN SEMICOLON','writing',5,'p_writing_1','parser.py',172),
  ('writing -> READLN LPAREN ID RPAREN SEMICOLON','writing',5,'p_writing_1','parser.py',173),
  ('writing -> READLN LPAREN RPAREN SEMICOLON','writing',4,'p_writing_1','parser.py',174),
  ('writing -> READLN SEMICOLON','writing',2,'p_writing_1','parser.py',175),
  ('writing -> WRITELN SEMICOLON','writing',2,'p_writing_2','parser.py',180),
  ('asignation -> ID EQUAL callFunctions SEMICOLON','asignation',4,'p_asignation','parser.py',185),
  ('asignation -> ID EQUAL math SEMICOLON','asignation',4,'p_asignation','parser.py',186),
  ('asignation -> ID EQUAL boolean SEMICOLON','asignation',4,'p_asignation','parser.py',187),
  ('asignation -> ID EQUAL TEXT SEMICOLON','asignation',4,'p_asignation','parser.py',188),
  ('asignation_for -> ID EQUAL id_num','asignation_for',3,'p_asignation_for','parser.py',193),
  ('cycles -> type_cycle','cycles',1,'p_cycles','parser.py',198),
  ('type_cycle -> while','type_cycle',1,'p_type_cycle','parser.py',203),
  ('type_cycle -> if','type_cycle',1,'p_type_cycle','parser.py',204),
  ('type_cycle -> for','type_cycle',1,'p_type_cycle','parser.py',205),
  ('type_cycle -> cycles instruction','type_cycle',2,'p_type_cycle','parser.py',206),
  ('while -> WHILE internexpression op_cycle DO otherBegin','while',5,'p_while','parser.py',211),
  ('if -> IF internexpression op_cycle THEN otherBegin_if','if',5,'p_if','parser.py',216),
  ('if -> IF internexpression op_cycle THEN instruction_one_line','if',5,'p_if','parser.py',217),
  ('if -> IF internexpression op_cycle THEN otherBegin_if ELSE otherBegin','if',7,'p_if','parser.py',218),
  ('if -> IF internexpression op_cycle THEN otherBegin_if ELSE instruction_one_line','if',7,'p_if','parser.py',219),
  ('if -> IF internexpression op_cycle THEN instruction_one_line ELSE otherBegin','if',7,'p_if','parser.py',220),
  ('if -> IF internexpression op_cycle THEN instruction_one_line ELSE instruction_one_line','if',7,'p_if','parser.py',221),
  ('for -> FOR asignation_for TO id_num DO otherBegin','for',6,'p_for','parser.py',226),
  ('for -> FOR asignation_for DOWNTO id_num DO otherBegin','for',6,'p_for','parser.py',227),
  ('op_cycle -> op_logic internexpression op_cycle','op_cycle',3,'p_op_cycle','parser.py',232),
  ('op_cycle -> empty','op_cycle',1,'p_op_cycle','parser.py',233),
  ('internexpression -> parentheses','internexpression',1,'p_internexpression_1','parser.py',237),
  ('internexpression -> expression','internexpression',1,'p_internexpression_2','parser.py',242),
  ('parentheses -> LPAREN expression RPAREN','parentheses',3,'p_parentheses','parser.py',247),
  ('expression -> callFunctions','expression',1,'p_expression_1','parser.py',252),
  ('expression -> callFunctions type_op math','expression',3,'p_expression_1','parser.py',253),
  ('expression -> callFunctions type_op callFunctions','expression',3,'p_expression_1','parser.py',254),
  ('expression -> math type_op math','expression',3,'p_expression_1','parser.py',255),
  ('expression -> ID','expression',1,'p_expression_1','parser.py',256),
  ('expression -> math ISEQUAL boolean','expression',3,'p_expression_1','parser.py',257),
  ('expression -> boolean ISEQUAL math','expression',3,'p_expression_1','parser.py',258),
  ('expression -> expression2','expression',1,'p_expression_1','parser.py',259),
  ('expression2 -> TEXT type_op TEXT','expression2',3,'p_expression2','parser.py',264),
  ('expression2 -> TEXT type_op ID','expression2',3,'p_expression2','parser.py',265),
  ('type_op -> LESSEQUAL','type_op',1,'p_type_op_1','parser.py',297),
  ('type_op -> LESS','type_op',1,'p_type_op_2','parser.py',302),
  ('type_op -> GREATER','type_op',1,'p_type_op_3','parser.py',307),
  ('type_op -> GREATEREQUAL','type_op',1,'p_type_op_4','parser.py',312),
  ('type_op -> DEQUAL','type_op',1,'p_type_op_5','parser.py',317),
  ('type_op -> ISEQUAL','type_op',1,'p_type_op_6','parser.py',327),
  ('type_op_math -> PLUS','type_op_math',1,'p_type_op_math_1','parser.py',332),
  ('type_op_math -> MINUS','type_op_math',1,'p_type_op_math_2','parser.py',337),
  ('type_op_math -> TIMES','type_op_math',1,'p_type_op_math_3','parser.py',342),
  ('type_op_math -> DIVIDE','type_op_math',1,'p_type_op_math_4','parser.py',347),
  ('type_op_math -> MOD','type_op_math',1,'p_type_op_math_5','parser.py',352),
  ('op_logic -> AND','op_logic',1,'p_op_logic_1','parser.py',357),
  ('op_logic -> OR','op_logic',1,'p_op_logic_2','parser.py',362),
  ('op_logic -> XOR','op_logic',1,'p_op_logic_3','parser.py',367),
  ('op_logic -> NOT','op_logic',1,'p_op_logic_4','parser.py',372),
  ('id_num -> NUMBER','id_num',1,'p_id_num','parser.py',377),
  ('id_num -> ID','id_num',1,'p_id_num','parser.py',378),
  ('boolean -> TRUE','boolean',1,'p_boolean','parser.py',382),
  ('boolean -> FALSE','boolean',1,'p_boolean','parser.py',383),
  ('otherBegin -> BEGIN instruction END SEMICOLON instruction','otherBegin',5,'p_otherBegin','parser.py',387),
  ('otherBegin_if -> BEGIN instruction END instruction','otherBegin_if',4,'p_otherBegin_if','parser.py',392),
  ('Begin_function -> var_declaration BEGIN instruction END SEMICOLON instruction','Begin_function',6,'p_Begin_function','parser.py',397),
  ('Begin_function -> BEGIN instruction END SEMICOLON instruction','Begin_function',5,'p_Begin_function','parser.py',398),
  ('function_declaration -> FUNCTION ID LPAREN fun_param RPAREN COLON type_specifier SEMICOLON Begin_function','function_declaration',9,'p_function_declaration','parser.py',403),
  ('function_declaration -> PROCEDURE ID LPAREN fun_param RPAREN SEMICOLON Begin_function','function_declaration',7,'p_function_declaration','parser.py',404),
  ('function_declaration -> PROCEDURE ID SEMICOLON Begin_function','function_declaration',4,'p_function_declaration','parser.py',405),
  ('fun_param -> ID fun_param_2 COLON type_specifier fun_param','fun_param',5,'p_fun_param_1','parser.py',410),
  ('fun_param -> SEMICOLON ID fun_param_2 COLON type_specifier fun_param','fun_param',6,'p_fun_param_1','parser.py',411),
  ('fun_param -> empty','fun_param',1,'p_fun_param_1','parser.py',412),
  ('fun_param_2 -> COMMA ID fun_param_2','fun_param_2',3,'p_fun_param_2','parser.py',417),
  ('fun_param_2 -> empty','fun_param_2',1,'p_fun_param_2','parser.py',418),
]

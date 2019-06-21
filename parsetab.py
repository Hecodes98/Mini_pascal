
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSOLUTE AMPERSANT AND ARRAY ASM BEGIN BOOLEAN BREAK CASE CHAR CLRSCR COLON COMMA CONST CONSTRUCTOR DEQUAL DESTRUCTOR DISTINT DIVIDE DO DOT DOUBLE DOWNTO ELSE END EQUAL FALSE FILE FLOAT FOR FUNCTION GOTO GREATER GREATEREQUAL HASHTAG ID IF IMPLEMENTATION IN INHERITED INLINE INTEGER INTERFACE ISEQUAL LABEL LBLOCK LBRACKET LESS LESSEQUAL LONG LPAREN MINUS MINUSMINUS MOD NIL NOT NUMBER OBJECT OF OPERATOR OR PACKED PLUS PLUSPLUS PROCEDURE PROGRAM RBLOCK RBRACKET READLN REAL RECORD REINTRODUCE REPEAT RPAREN SELF SEMICOLON SET SHL SHR STRING TEXT THEN TIMES TO TRUE TYPE UNIT UNTIL USES VAR WHILE WITH WRITE WRITELN XORprogram : declaration_listdeclaration_list : declaration_list  declarationdeclaration_list : declarationdeclaration : header_declaration\n                            | var_declaration\n                            | function_declaration\n                            | procedure_declarationheader_declaration : PROGRAM ID SEMICOLONheader_declaration : USES ID header_declaration_3 SEMICOLONheader_declaration_3 : COMMA ID header_declaration_3 \n                                                | emptyvar_declaration : VAR var_declaration_2var_declaration_2 : ID var_declaration_3 COLON type_specifier SEMICOLON var_declaration_4var_declaration_3 : COMMA ID var_declaration_3 \n                                            | emptyvar_declaration_4 : var_declaration_2 \n                                    | emptyempty :math : factor mathimathi : type_op_math factor mathi\n             | emptyfactor : LPAREN math RPAREN\n              | NUMBER\n              | IDtype_specifier : INTEGERtype_specifier : REALtype_specifier : CHARtype_specifier : BOOLEANtype_specifier : DOUBLEprocedure_declaration : BEGIN instruction END DOTinstruction : asignation instruction\n                        | writing instruction\n                        | cycles instruction\n                        | callFunctions instruction\n                                    | emptycallFunctions : ID LPAREN params RPAREN params : math params2params2 : COMMA math \n                | emptyinstruction_one_line : asignation\n                        | writing\n                        | cyclesid_text_l : callFunctions COMMA id_text_l \n               | ID COMMA id_text_l            \n               | emptyid_text_r : COMMA callFunctions id_text_r\n               | COMMA ID id_text_r\n               | emptywriting : WRITELN LPAREN id_text_l TEXT id_text_r RPAREN SEMICOLON\n                | WRITELN LPAREN id_num RPAREN SEMICOLON\n                | READLN LPAREN ID RPAREN SEMICOLON\n                | READLN LPAREN RPAREN SEMICOLON\n                | READLN SEMICOLONwriting : WRITELN SEMICOLONasignation : ID EQUAL callFunctions SEMICOLON\n                | ID EQUAL math SEMICOLON \n                | ID EQUAL boolean SEMICOLON\n                | ID EQUAL TEXT SEMICOLONasignation_for : ID EQUAL id_numcycles : type_cycletype_cycle : while\n                    | if \n                    | for \n                    | cycles instructionwhile : WHILE internexpression op_cycle DO otherBeginif : IF internexpression op_cycle THEN otherBegin_if \n            | IF internexpression op_cycle THEN instruction_one_line\n            | IF internexpression op_cycle THEN otherBegin_if ELSE otherBegin\n            | IF internexpression op_cycle THEN otherBegin_if ELSE instruction_one_line\n            | IF internexpression op_cycle THEN instruction_one_line ELSE otherBegin\n            | IF internexpression op_cycle THEN instruction_one_line ELSE instruction_one_linefor : FOR asignation_for TO id_num DO otherBegin\n            | FOR asignation_for DOWNTO id_num DO otherBeginop_cycle : op_logic internexpression op_cycle\n                                        | emptyinternexpression : parenthesesinternexpression : expressionparentheses : LPAREN expression RPARENexpression : math type_op math\n                    | ID\n                    | math ISEQUAL boolean\n                    | boolean ISEQUAL math\n                    | expression2expression2 : TEXT type_op TEXT\n                  | TEXT type_op IDtype_op : LESSEQUALtype_op : LESStype_op : GREATERtype_op : GREATEREQUALtype_op : DEQUALtype_op : ISEQUALtype_op_math : PLUStype_op_math : MINUStype_op_math : TIMEStype_op_math : DIVIDEtype_op_math : MODop_logic : ANDop_logic : ORop_logic : XORop_logic : NOTid_num : NUMBER\n                | IDboolean : TRUE\n                | FALSEotherBegin : BEGIN instruction END SEMICOLON instructionotherBegin_if : BEGIN instruction END instructionBegin_function : var_declaration BEGIN instruction END SEMICOLON instruction\n                        | BEGIN instruction END SEMICOLON instructionfunction_declaration : FUNCTION ID LPAREN fun_param RPAREN COLON type_specifier SEMICOLON Begin_function\n                            | PROCEDURE ID LPAREN fun_param RPAREN SEMICOLON Begin_function\n                            | PROCEDURE ID SEMICOLON Begin_functionfun_param : ID fun_param_2 COLON type_specifier fun_param\n                 | SEMICOLON ID fun_param_2 COLON type_specifier fun_param\n                 | emptyfun_param_2 : COMMA ID fun_param_2\n                            | empty'
    
_lr_action_items = {'REAL':([129,182,183,211,],[171,171,171,171,]),'THEN':([42,44,45,46,50,51,52,53,63,86,98,104,118,125,141,143,144,145,147,148,149,150,151,185,188,],[-76,-23,-104,-103,-18,-83,-77,-80,-18,-75,-19,-21,-24,168,-18,-82,-84,-85,-78,-22,-18,-79,-81,-74,-20,]),'DO':([42,43,44,45,46,50,51,52,53,84,86,98,104,114,118,141,143,144,145,147,148,149,150,151,152,153,154,185,188,],[-76,-18,-23,-104,-103,-18,-83,-77,-80,142,-75,-19,-21,-101,-24,-18,-82,-84,-85,-78,-22,-18,-79,-81,189,-102,190,-74,-20,]),'TEXT':([17,25,49,60,62,80,81,82,83,85,88,89,90,91,92,93,94,112,116,156,159,191,197,],[48,48,48,-18,120,-97,-99,48,-100,-98,-89,-88,-87,-90,-91,144,-86,157,-45,-18,-18,-43,-44,]),'NUMBER':([17,25,49,60,61,62,80,81,82,83,85,87,88,89,90,91,94,95,99,100,101,102,103,105,106,107,108,109,110,162,],[44,44,44,114,44,44,-97,-99,44,-100,-98,44,-89,-88,-87,-90,-86,44,-95,-94,-92,44,-93,-96,44,-91,114,114,114,44,]),'CHAR':([129,182,183,211,],[174,174,174,174,]),'LESSEQUAL':([44,48,50,53,54,97,98,104,118,148,149,188,],[-23,94,-18,-24,94,94,-19,-21,-24,-22,-18,-20,]),'WHILE':([4,18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,168,169,179,186,187,196,199,200,201,203,204,205,206,216,217,222,223,224,228,237,238,239,240,241,242,244,247,248,250,],[17,17,17,-62,-35,-63,17,-60,-61,17,-32,-34,-54,-31,-53,-33,17,-36,-58,-57,-55,-56,17,-52,17,17,-65,-50,17,-41,-67,-40,-66,17,-51,-73,-72,17,17,-64,17,-49,17,-71,-70,-69,-68,17,17,-106,-105,]),'PROGRAM':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,216,217,224,225,226,227,228,230,237,238,239,240,241,242,243,244,246,247,248,249,250,],[2,-5,-4,-3,-6,-7,2,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-110,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'USES':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,216,217,224,225,226,227,228,230,237,238,239,240,241,242,243,244,246,247,248,249,250,],[3,-5,-4,-3,-6,-7,3,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-110,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'XOR':([42,43,44,45,46,50,51,52,53,63,98,104,118,141,143,144,145,147,148,149,150,151,188,],[-76,81,-23,-104,-103,-18,-83,-77,-80,81,-19,-21,-24,81,-82,-84,-85,-78,-22,-18,-79,-81,-20,]),'TRUE':([17,25,49,62,80,81,82,83,85,107,],[46,46,46,46,-97,-99,46,-100,-98,46,]),'MINUS':([44,50,53,118,123,148,149,],[-23,103,-24,-24,-24,-22,103,]),'DOT':([64,],[126,]),'BEGIN':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,72,79,126,132,133,142,160,164,165,166,167,168,169,187,189,190,196,200,201,203,204,205,206,207,210,216,217,222,223,224,225,226,227,228,230,232,237,238,239,240,241,242,243,244,246,247,248,249,250,],[4,-5,-4,-3,-6,-7,4,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,131,-9,-30,179,-111,186,-36,-58,-57,-55,-56,199,-52,-65,186,186,-50,-41,-67,-40,-66,-18,-51,-18,131,-73,-72,186,186,-64,-13,-16,-17,-18,-110,131,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'RPAREN':([37,44,45,46,50,51,53,67,73,75,77,96,97,98,104,113,114,115,117,118,119,128,134,143,144,145,146,148,149,150,151,157,160,161,163,171,173,174,175,176,188,194,195,198,213,218,219,231,233,235,236,245,],[-18,-23,-104,-103,-18,-83,-24,127,-18,136,-114,147,148,-19,-21,158,-101,-102,160,-24,-18,170,180,-82,-84,-85,148,-22,-18,-79,-81,-18,-36,-37,-39,-26,-29,-27,-28,-25,-20,220,-48,-38,-18,-18,-18,-18,-112,-46,-47,-113,]),'SEMICOLON':([15,16,23,29,35,37,40,41,44,45,46,50,73,78,98,104,118,120,121,122,123,124,127,140,148,149,158,160,170,171,172,173,174,175,176,180,188,208,212,213,220,229,231,234,],[38,-18,59,66,72,74,79,-11,-23,-104,-103,-18,74,-18,-19,-21,-24,164,165,166,-24,167,169,-10,-22,-18,196,-36,206,-26,207,-29,-27,-28,-25,210,-20,228,232,74,237,244,74,247,]),'LESS':([44,48,50,53,54,97,98,104,118,148,149,188,],[-23,90,-18,-24,90,90,-19,-21,-24,-22,-18,-20,]),'PLUS':([44,50,53,118,123,148,149,],[-23,101,-24,-24,-24,-22,101,]),'TO':([57,114,153,155,],[109,-101,-102,-59,]),'COMMA':([16,34,44,50,76,78,98,104,111,115,118,119,130,135,148,149,157,160,184,188,192,218,219,],[39,70,-23,-18,138,39,-19,-21,156,159,-24,162,70,138,-22,-18,193,-36,138,-20,159,193,193,]),'COLON':([34,69,71,76,130,135,136,137,139,177,181,184,214,],[-18,129,-15,-18,-18,-18,182,183,-116,-14,211,-18,-115,]),'$end':([5,6,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,216,217,224,225,226,227,228,230,237,238,239,240,241,242,243,244,246,247,248,249,250,],[-5,0,-4,-3,-6,-7,-1,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-110,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'FUNCTION':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,216,217,224,225,226,227,228,230,237,238,239,240,241,242,243,244,246,247,248,249,250,],[1,-5,-4,-3,-6,-7,1,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-110,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'END':([4,18,19,20,21,26,27,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,169,178,179,186,187,196,199,200,201,203,204,205,206,209,215,216,217,221,224,237,238,239,240,241,242,247,248,250,],[-18,-18,-18,-62,-35,-63,64,-18,-60,-61,-18,-32,-34,-54,-31,-53,-33,-18,-36,-58,-57,-55,-56,-52,208,-18,-18,-65,-50,-18,-41,-67,-40,-66,-18,-51,229,234,-73,-72,238,-64,-49,-18,-71,-70,-69,-68,-18,-106,-105,]),'DIVIDE':([44,50,53,118,123,148,149,],[-23,99,-24,-24,-24,-22,99,]),'FOR':([4,18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,168,169,179,186,187,196,199,200,201,203,204,205,206,216,217,222,223,224,228,237,238,239,240,241,242,244,247,248,250,],[22,22,22,-62,-35,-63,22,-60,-61,22,-32,-34,-54,-31,-53,-33,22,-36,-58,-57,-55,-56,22,-52,22,22,-65,-50,22,-41,-67,-40,-66,22,-51,-73,-72,22,22,-64,22,-49,22,-71,-70,-69,-68,22,22,-106,-105,]),'EQUAL':([24,58,202,],[62,110,62,]),'GREATEREQUAL':([44,48,50,53,54,97,98,104,118,148,149,188,],[-23,88,-18,-24,88,88,-19,-21,-24,-22,-18,-20,]),'ELSE':([18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,160,164,165,166,167,169,187,196,200,201,203,204,205,206,216,217,224,237,238,239,240,241,242,247,248,250,],[-18,-18,-62,-35,-63,-18,-60,-61,-18,-32,-34,-54,-31,-53,-33,-36,-58,-57,-55,-56,-52,-65,-50,-41,222,-40,223,-18,-51,-73,-72,-64,-49,-18,-71,-70,-69,-68,-18,-106,-105,]),'WRITELN':([4,18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,168,169,179,186,187,196,199,200,201,203,204,205,206,216,217,222,223,224,228,237,238,239,240,241,242,244,247,248,250,],[23,23,23,-62,-35,-63,23,-60,-61,23,-32,-34,-54,-31,-53,-33,23,-36,-58,-57,-55,-56,23,-52,23,23,-65,-50,23,-41,-67,-40,-66,23,-51,-73,-72,23,23,-64,23,-49,23,-71,-70,-69,-68,23,23,-106,-105,]),'LPAREN':([14,17,23,24,25,29,35,49,61,62,80,81,82,83,85,87,88,89,90,91,94,95,99,100,101,102,103,105,106,107,115,123,162,192,219,],[37,49,60,61,49,67,73,95,95,95,-97,-99,49,-100,-98,95,-89,-88,-87,-90,-86,95,-95,-94,-92,95,-93,-96,95,-91,61,61,95,61,61,]),'INTEGER':([129,182,183,211,],[176,176,176,176,]),'VAR':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,72,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,210,216,217,224,225,226,227,228,230,232,237,238,239,240,241,242,243,244,246,247,248,249,250,],[9,-5,-4,-3,-6,-7,9,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,9,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,9,-73,-72,-64,-13,-16,-17,-18,-110,9,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'TIMES':([44,50,53,118,123,148,149,],[-23,100,-24,-24,-24,-22,100,]),'ID':([1,2,3,4,9,10,17,18,19,20,21,22,25,26,28,30,31,32,37,39,49,55,56,59,60,61,62,65,66,67,68,70,73,74,80,81,82,83,85,87,88,89,90,91,92,93,94,95,99,100,101,102,103,105,106,107,108,109,110,131,138,156,159,160,162,164,165,166,167,168,169,171,173,174,175,176,179,186,187,193,196,199,200,201,203,204,205,206,207,213,216,217,222,223,224,228,231,237,238,239,240,241,242,244,247,248,250,],[14,15,16,24,34,35,53,24,24,-62,-35,58,53,-63,24,-60,-61,24,76,78,53,-32,-34,-54,115,118,123,-31,-53,128,-33,130,76,135,-97,-99,53,-100,-98,118,-89,-88,-87,-90,-91,145,-86,118,-95,-94,-92,118,-93,-96,118,-91,153,153,153,24,184,192,192,-36,118,-58,-57,-55,-56,202,-52,-26,-29,-27,-28,-25,24,24,-65,219,-50,24,-41,-67,-40,-66,24,-51,34,76,-73,-72,202,202,-64,24,76,-49,24,-71,-70,-69,-68,24,24,-106,-105,]),'PROCEDURE':([0,5,7,8,11,12,13,18,19,20,21,26,28,30,31,32,33,36,38,55,56,59,65,66,68,79,126,133,160,164,165,166,167,169,187,196,200,201,203,204,205,206,207,216,217,224,225,226,227,228,230,237,238,239,240,241,242,243,244,246,247,248,249,250,],[10,-5,-4,-3,-6,-7,10,-18,-18,-62,-35,-63,-18,-60,-61,-18,-12,-2,-8,-32,-34,-54,-31,-53,-33,-9,-30,-111,-36,-58,-57,-55,-56,-52,-65,-50,-41,-67,-40,-66,-18,-51,-18,-73,-72,-64,-13,-16,-17,-18,-110,-49,-18,-71,-70,-69,-68,-108,-18,-109,-18,-106,-107,-105,]),'IF':([4,18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,168,169,179,186,187,196,199,200,201,203,204,205,206,216,217,222,223,224,228,237,238,239,240,241,242,244,247,248,250,],[25,25,25,-62,-35,-63,25,-60,-61,25,-32,-34,-54,-31,-53,-33,25,-36,-58,-57,-55,-56,25,-52,25,25,-65,-50,25,-41,-67,-40,-66,25,-51,-73,-72,25,25,-64,25,-49,25,-71,-70,-69,-68,25,25,-106,-105,]),'AND':([42,43,44,45,46,50,51,52,53,63,98,104,118,141,143,144,145,147,148,149,150,151,188,],[-76,80,-23,-104,-103,-18,-83,-77,-80,80,-19,-21,-24,80,-82,-84,-85,-78,-22,-18,-79,-81,-20,]),'FALSE':([17,25,49,62,80,81,82,83,85,107,],[45,45,45,45,-97,-99,45,-100,-98,45,]),'GREATER':([44,48,50,53,54,97,98,104,118,148,149,188,],[-23,89,-18,-24,89,89,-19,-21,-24,-22,-18,-20,]),'DOUBLE':([129,182,183,211,],[173,173,173,173,]),'DEQUAL':([44,48,50,53,54,97,98,104,118,148,149,188,],[-23,91,-18,-24,91,91,-19,-21,-24,-22,-18,-20,]),'READLN':([4,18,19,20,21,26,28,30,31,32,55,56,59,65,66,68,131,160,164,165,166,167,168,169,179,186,187,196,199,200,201,203,204,205,206,216,217,222,223,224,228,237,238,239,240,241,242,244,247,248,250,],[29,29,29,-62,-35,-63,29,-60,-61,29,-32,-34,-54,-31,-53,-33,29,-36,-58,-57,-55,-56,29,-52,29,29,-65,-50,29,-41,-67,-40,-66,29,-51,-73,-72,29,29,-64,29,-49,29,-71,-70,-69,-68,29,29,-106,-105,]),'DOWNTO':([57,114,153,155,],[108,-101,-102,-59,]),'BOOLEAN':([129,182,183,211,],[175,175,175,175,]),'ISEQUAL':([44,45,46,47,48,50,53,54,97,98,104,118,148,149,188,],[-23,-104,-103,87,92,-18,-24,107,107,-19,-21,-24,-22,-18,-20,]),'NOT':([42,43,44,45,46,50,51,52,53,63,98,104,118,141,143,144,145,147,148,149,150,151,188,],[-76,83,-23,-104,-103,-18,-83,-77,-80,83,-19,-21,-24,83,-82,-84,-85,-78,-22,-18,-79,-81,-20,]),'OR':([42,43,44,45,46,50,51,52,53,63,98,104,118,141,143,144,145,147,148,149,150,151,188,],[-76,85,-23,-104,-103,-18,-83,-77,-80,85,-19,-21,-24,85,-82,-84,-85,-78,-22,-18,-79,-81,-20,]),'MOD':([44,50,53,118,123,148,149,],[-23,105,-24,-24,-24,-22,105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'id_text_l':([60,156,159,],[112,191,197,]),'fun_param_2':([76,135,184,],[137,181,214,]),'otherBegin':([142,189,190,222,223,],[187,216,217,240,242,]),'id_num':([60,108,109,110,],[113,152,154,155,]),'boolean':([17,25,49,62,82,107,],[47,47,47,121,47,151,]),'type_specifier':([129,182,183,211,],[172,212,213,231,]),'declaration_list':([0,],[13,]),'header_declaration_3':([16,78,],[40,140,]),'if':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'asignation_for':([22,],[57,]),'for':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'type_op':([48,54,97,],[93,106,106,]),'internexpression':([17,25,82,],[43,63,141,]),'writing':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[18,18,18,18,18,18,200,18,18,18,18,200,200,18,18,18,18,]),'var_declaration':([0,13,72,210,232,],[5,5,132,132,132,]),'op_logic':([43,63,141,],[82,82,82,]),'program':([0,],[6,]),'params':([61,],[117,]),'callFunctions':([4,18,19,28,32,60,62,131,156,159,179,186,193,199,205,228,238,244,247,],[19,19,19,19,19,111,122,19,111,111,19,19,218,19,19,19,19,19,19,]),'factor':([17,25,49,61,62,82,87,95,102,106,162,],[50,50,50,50,50,50,50,50,149,50,50,]),'Begin_function':([72,210,232,],[133,230,246,]),'empty':([4,16,18,19,28,32,34,37,43,50,60,63,73,76,78,119,130,131,135,141,149,156,157,159,179,184,186,199,205,207,213,218,219,228,231,238,244,247,],[21,41,21,21,21,21,71,77,86,104,116,86,77,139,41,163,71,21,139,86,104,116,195,116,21,139,21,21,21,227,77,195,195,21,77,21,21,21,]),'id_text_r':([157,218,219,],[194,235,236,]),'header_declaration':([0,13,],[7,7,]),'mathi':([50,149,],[98,188,]),'var_declaration_4':([207,],[225,]),'var_declaration_2':([9,207,],[33,226,]),'var_declaration_3':([34,130,],[69,177,]),'fun_param':([37,73,213,231,],[75,134,233,245,]),'instruction_one_line':([168,222,223,],[201,239,241,]),'params2':([119,],[161,]),'declaration':([0,13,],[8,36,]),'op_cycle':([43,63,141,],[84,125,185,]),'expression2':([17,25,49,82,],[51,51,51,51,]),'parentheses':([17,25,82,],[42,42,42,]),'function_declaration':([0,13,],[11,11,]),'procedure_declaration':([0,13,],[12,12,]),'instruction':([4,18,19,28,32,131,179,186,199,205,228,238,244,247,],[27,55,56,65,68,178,209,215,221,224,243,248,249,250,]),'asignation':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[28,28,28,28,28,28,203,28,28,28,28,203,203,28,28,28,28,]),'type_cycle':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'while':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'math':([17,25,49,61,62,82,87,95,106,162,],[54,54,97,119,124,54,143,146,150,198,]),'type_op_math':([50,149,],[102,102,]),'otherBegin_if':([168,],[204,]),'cycles':([4,18,19,28,32,131,168,179,186,199,205,222,223,228,238,244,247,],[32,32,32,32,32,32,205,32,32,32,32,205,205,32,32,32,32,]),'expression':([17,25,49,82,],[52,52,96,52,]),}

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
  ('expression -> math type_op math','expression',3,'p_expression_1','parser.py',252),
  ('expression -> ID','expression',1,'p_expression_1','parser.py',253),
  ('expression -> math ISEQUAL boolean','expression',3,'p_expression_1','parser.py',254),
  ('expression -> boolean ISEQUAL math','expression',3,'p_expression_1','parser.py',255),
  ('expression -> expression2','expression',1,'p_expression_1','parser.py',256),
  ('expression2 -> TEXT type_op TEXT','expression2',3,'p_expression2','parser.py',261),
  ('expression2 -> TEXT type_op ID','expression2',3,'p_expression2','parser.py',262),
  ('type_op -> LESSEQUAL','type_op',1,'p_type_op_1','parser.py',294),
  ('type_op -> LESS','type_op',1,'p_type_op_2','parser.py',299),
  ('type_op -> GREATER','type_op',1,'p_type_op_3','parser.py',304),
  ('type_op -> GREATEREQUAL','type_op',1,'p_type_op_4','parser.py',309),
  ('type_op -> DEQUAL','type_op',1,'p_type_op_5','parser.py',314),
  ('type_op -> ISEQUAL','type_op',1,'p_type_op_6','parser.py',324),
  ('type_op_math -> PLUS','type_op_math',1,'p_type_op_math_1','parser.py',329),
  ('type_op_math -> MINUS','type_op_math',1,'p_type_op_math_2','parser.py',334),
  ('type_op_math -> TIMES','type_op_math',1,'p_type_op_math_3','parser.py',339),
  ('type_op_math -> DIVIDE','type_op_math',1,'p_type_op_math_4','parser.py',344),
  ('type_op_math -> MOD','type_op_math',1,'p_type_op_math_5','parser.py',349),
  ('op_logic -> AND','op_logic',1,'p_op_logic_1','parser.py',354),
  ('op_logic -> OR','op_logic',1,'p_op_logic_2','parser.py',359),
  ('op_logic -> XOR','op_logic',1,'p_op_logic_3','parser.py',364),
  ('op_logic -> NOT','op_logic',1,'p_op_logic_4','parser.py',369),
  ('id_num -> NUMBER','id_num',1,'p_id_num','parser.py',374),
  ('id_num -> ID','id_num',1,'p_id_num','parser.py',375),
  ('boolean -> TRUE','boolean',1,'p_boolean','parser.py',379),
  ('boolean -> FALSE','boolean',1,'p_boolean','parser.py',380),
  ('otherBegin -> BEGIN instruction END SEMICOLON instruction','otherBegin',5,'p_otherBegin','parser.py',384),
  ('otherBegin_if -> BEGIN instruction END instruction','otherBegin_if',4,'p_otherBegin_if','parser.py',389),
  ('Begin_function -> var_declaration BEGIN instruction END SEMICOLON instruction','Begin_function',6,'p_Begin_function','parser.py',394),
  ('Begin_function -> BEGIN instruction END SEMICOLON instruction','Begin_function',5,'p_Begin_function','parser.py',395),
  ('function_declaration -> FUNCTION ID LPAREN fun_param RPAREN COLON type_specifier SEMICOLON Begin_function','function_declaration',9,'p_function_declaration','parser.py',400),
  ('function_declaration -> PROCEDURE ID LPAREN fun_param RPAREN SEMICOLON Begin_function','function_declaration',7,'p_function_declaration','parser.py',401),
  ('function_declaration -> PROCEDURE ID SEMICOLON Begin_function','function_declaration',4,'p_function_declaration','parser.py',402),
  ('fun_param -> ID fun_param_2 COLON type_specifier fun_param','fun_param',5,'p_fun_param_1','parser.py',407),
  ('fun_param -> SEMICOLON ID fun_param_2 COLON type_specifier fun_param','fun_param',6,'p_fun_param_1','parser.py',408),
  ('fun_param -> empty','fun_param',1,'p_fun_param_1','parser.py',409),
  ('fun_param_2 -> COMMA ID fun_param_2','fun_param_2',3,'p_fun_param_2','parser.py',414),
  ('fun_param_2 -> empty','fun_param_2',1,'p_fun_param_2','parser.py',415),
]

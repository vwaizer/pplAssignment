grammar CSlang;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

        program: classdecl+ EOF;
        classdecl: CLASS (id_type|(id_type RARROW id_type))  LCB classbody* RCB ;
        classbody: (var_decl|funct_declare|const_decl) ;
        const_decl: CONST full_form_const SEMI;
        full_form_const: id_type identifier_list  expr;
        var_decl: (VAR) (short_form|full_form) SEMI;
        short_form: short_identifier_list COLON whole_type;
        short_identifier_list: id_type COMMA short_identifier_list | id_type;
        full_form: id_type identifier_list  expr;
        identifier_list: COMMA id_type identifier_list expr COMMA | COLON whole_type EQUAL;
        expression_list: expr COMMA expression_list | expr;
        expr: expr0;
        expr0: expr1 STRING_OP expr1 | expr1;
        expr1: expr2 compare_ops expr2 | expr2;
        expr2: expr2 (AND_OP | OR_OP) expr3 | expr3;
        expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
        expr4: expr4 (MUL_OP | F_DIV_OP | REM_OP|I_DIV_OP) expr5 | expr5;
        expr5: NOT_OP expr5 | expr6;
        expr6: SUB_OP expr6 | expr7;
        expr7: expr8 index_expression | expr8;
        expr8: expr8 DOT expr9| expr9;
        expr9: expr10 DOT SIGN expr10| expr10;
        expr10:  class_create expr10 |expr11;
        expr11: array_idx | operands ;
        array_idx: id_type index_expression;
        index_expression: LSB expression_list? RSB;
        operands: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT  | function_call | id_type | subexpression|instance_access|static_access;
        subexpression: LB expr RB ;
        compare_ops: EQ_OP | NEQ_OP | LT_OP| GT_OP | LEQ_OP | GEQ_OP;
        // ------------------------------------------
        whole_type: core_type|arr_type;
        core_type: INT|FLOAT|BOOL|STRING|arr_type;
        id_type: ID| at_id;
        at_id: SIGN ID;
        function_call: id_type function_call_params;
        function_call_params: LB function_call_param_list? RB;
        function_call_param_list: expr COMMA function_call_param_list | expr;
        arr_type: LCB DIM RCB core_type;
        class_create: NEW whole_type LB (expression_list)? RB;

        funct_declare: FUNCTION funct_prototype  (funct_body);
        funct_prototype:  (id_type params COLON funct_return_type)| (CONTRUCTOR params) ;
        params: LB parameter_list? RB;
        parameter_list: parameter_declare COMMA parameter_list | parameter_declare;
        parameter_declare:  id_type COLON whole_type;

        funct_body: block_statement;

        funct_return_type: VOID | core_type;
        continue_statement: CONTINUE SEMI;
        break_statement: BREAK SEMI;
        return_statement: RETURN (expr)? SEMI;

        block_statement:LCB stateVinhs? RCB;
        stateVinhs:stateVinh+;
        stateVinh: assignment_statement
                | if_statement
                | for_statement
                | return_statement
                | break_statement
                | continue_statement
                | function_call
                | block_statement 
                | var_decl
                |method_access;
        assignment_statement: assignment_content SEMI;
        assignment_content: lhs ASSGIN_OP assign_expressions;
        lhs: id_type | array_idx;
        assign_expressions: expr;


        // Flow control
        if_statement: IF (pre_state)? bool_expression true_statements else_expression?;
        pre_state: block_statement;
        bool_expression:  expr ;
        true_statements: block_statement;
        else_expression: ELSE block_statement;
        // Loop
        for_statement: FOR  assignment_statement  expr SEMI assignment_statement  for_body;
        for_body: block_statement ;
        method_access: instance_access|static_access|instance_method_access|static_method_access;
        instance_access: (ID|SELF) DOT ID;
        static_access:  (ID|SELF)DOT at_id;

        instance_method_access: expr DOT ID LB expression_list RB SEMI;
        static_method_access: ( ID DOT )?  at_id LB expression_list RB SEMI; 



//-------------------------------------------------------------------------------------------------

NULL:'null';
SELF:'self';
CONTRUCTOR:'contructor';
IF:'if';
ELSE:'else';
FOR:'for';
CONTINUE:'continue';
BREAK:'break';
RETURN:'return';

VOID:'void';
FUNCTION:'func';
NEW:'new';
CONST:'const';
VAR:'var';
CLASS: 'class';
LCB:'{';
RCB:'}';
SEMI:';';
COLON:':';

RARROW:'<-';
EQUAL:'=';
COMMA:',';

INT:'int';
FLOAT:'float';
SIGN:'@';
RB:')';
LB:'(';
LSB:'[';
RSB:']';
STRING_OP:'^';
EQ_OP:'==';
NEQ_OP:'!=';
LT_OP:'<';
GT_OP:'>';
LEQ_OP:'<=';
GEQ_OP:'>=';
AND_OP:'&&';
OR_OP:'||';
ADD_OP:'+';
SUB_OP:'-';
MUL_OP:'*';
F_DIV_OP:'/';
NOT_OP:'!';
I_DIV_OP:[\\];
REM_OP:'%';
BOOL:'bool';
DOT:'.';
STRING:'string';
ASSGIN_OP:':=';
INTLIT:[0-9]+;
fragment DecimalPart: [.][0-9]+;
fragment ExponentPart: ([eE][+-]?)[0-9]+;
FLOATLIT: INTLIT DecimalPart ExponentPart
        | INTLIT ExponentPart
        | INTLIT DecimalPart;


BOOLLIT: TRUE | FALSE;
TRUE:'true';
FALSE:'false';
DIM:[1-9][0-9]*;
// fragment StringChars: ~[ \f\r\n\\"] | '\b' | '\t'; 

// fragment DoubleQuotes: '"';
// STRINGLIT: '"' (DoubleQuotes | StringChars)* '"'
//           {
//             self.text = self.text[1:-1]
//           };
fragment STR_CHAR:   ~[\\\b\f\r\n\t]|'\\' ;
fragment ESC_SEQ: '\\' [btnfr'\\];
STRINGLIT: '"' (STR_CHAR|["] STR_CHAR* ["])* '"' {self.text = self.text[1:-1]};

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
C_COMMENT: '/*' .*? '*/' -> skip;
CPP_COMMENT: '//' ~[\r\n]* -> skip;
fragment ESC_ILLEGAL: '\\' [btnfr\\];
ID: [a-zA-Z0-9_]+;
  // UNCLOSE_STRING: '"' (DoubleQuotes | StringChars)* 
  //               {
  //                 escape_sequences = ['\b', '\f', '\r', '\n', '\t', '\'', '\\']
  //                 if(self.text[-1] in escape_sequences):
  //                   raise UncloseString(self.text[1:-1])
  //                 else: 
  //                   raise UncloseString(self.text[1:])
  //               };
  // fragment ESCAPE_ILLEGAL: '\\' ~[bfrnt\\];
  // ILLEGAL_ESCAPE: '"' (DoubleQuotes | StringChars)* ESCAPE_ILLEGAL  '"'?
  //               {
  //                 if(self.text[-1] == "\""):
  //                   raise IllegalEscape(self.text[1:-1])
  //                 raise IllegalEscape(self.text[1:])
  //               };
  // ERROR_CHAR: .{raise ErrorToken(self.text)};
  UNCLOSE_STRING: '"'  EOF { raise UncloseString(self.text[1:])};
// 
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL { raise IllegalEscape(self.text[1:] )};
ERROR_CHAR: . { raise ErrorToken(self.text) };
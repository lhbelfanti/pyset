grammar Grammar;

/*
 * Parser Rules
 */

 expression :
		sett
		| VARIABLE
		| VARIABLE '=' expression
		| CREATION_FUNCTION '({' (NUMBER | (NUMBER ',' NUMBER)*)  '})'
		| CREATION_FUNCTION '(' NUMBER ',' NUMBER ')'
		| CREATION_FUNCTION '(' NUMBER ',' NUMBER ',' NUMBER ')'
		| BINARY_FUNCTION '(' expression ',' expression ')'
		| UNARY_FUNCTION '(' expression ')'
		| ELEMENT_FUNCTION '(' expression ',' NUMBER ')'
		;
 
sett :
      '['	(NUMBER | (NUMBER ',' NUMBER)*)	']'
      ;

/*
 * Lexer Rules
 */

NUMBER : [0-9]+   ;
           
VARIABLE : [a-z]+ ;
            
CREATION_FUNCTION : 'set'		;
BINARY_FUNCTION  : 'int'|'uni'|'ext' ;
UNARY_FUNCTION   : 'max'|'min'|'len'|'avg' ;
ELEMENT_FUNCTION : 'add'|'del' ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

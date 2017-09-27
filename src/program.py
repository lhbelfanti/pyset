import sys
from parser.tokenizer import Tokenizer
from parser.token import Token
from parser.parser import Parser

class Program:

    def __init__(self):
        code = ("    var myset = set() \n var oo = set() n = 653")
        self.tokenizator(code)

    def tokenizator(self, code):
        tk = Tokenizer()

        TokenConst = Token('','')
        tk.add("\\[", TokenConst.OPEN_BRACKET);
        tk.add("\\]", TokenConst.CLOSE_BRACKET);
        tk.add(",", TokenConst.COMMA);
        tk.add("=", TokenConst.ASIGNATION);
        tk.add("[0-9]+", TokenConst.NUMBER);

        tk.tokenize(code)
        tokens = tk.tokens
        for t in tokens:
            print t.sequence

        p = Parser();
        p.parse(tokens);
    
        raw_input("Press Enter to continue...")

Program()
import sys
from tokenizer import Tokenizer

class Program:

    def __init__(self):
        code = ("    var myset = Set() \n var oo = Set() n = 653")
        self.tokenizator(code)

    def tokenizator(self, code):
        tk = Tokenizer()
        tk.add("var", 1)
        tk.add("[a-z]+", 2)
        tk.add("[0-9]+", 3)
        tk.add("=", 4)
        tk.add("Set|Int|Uni|Ext|If|Then|EndIf|For|In|Do|EndFor|Max|Min|Push|Med|Len", 5)
        tk.add("\\(", 6)
        tk.add("\\)", 7)
        tk.add("\\[", 8)
        tk.add("\\]", 9)
        tk.add("\\'", 10)

        tk.tokenize(code)
        tokens = tk.tokens
        for t in tokens:
            print t.sequence
    
        raw_input("Press Enter to continue...")

Program()
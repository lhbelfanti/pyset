import sys
from parser.parser import Parser

class Program:

    def __init__(self):
        code = ("    var myset = set() \n var oo = set() n = 653")

        p = Parser();
        p.parse(code);
        
        raw_input("Press Enter to continue...")

Program()
import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from GrammarListener import GrammarListener
 
class GrammarOKPrintListener(GrammarListener):
	def enterExpression(self, ctx):
		print("Start")
	def exitExpression(self, ctx):
		print("Finish")

def main():
	lexer = GrammarLexer(StdinStream())
	stream = CommonTokenStream(lexer)
	parser = GrammarParser(stream)
	tree = parser.expression()
	printer = GrammarOKPrintListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
 
if __name__ == '__main__':
	main()
import sys
from tokenizer import Tokenizer
from token import Token

class Parser:

	def __init__(self):
		self.tokens = []
		self.lookahead = None
		self.Token = Token()

	def parse(self, code):
		tk = self.buildTokenizer(code)
		self.tokens = tk.tokens

		for t in self.tokens:
			print t.sequence 

		self.parseTokens()

	def buildTokenizer(self, code):
		tk = Tokenizer()
		tk.add("\\[", self.Token.OPEN_BRACKET)
		tk.add("\\]", self.Token.CLOSE_BRACKET)
		tk.add(",", self.Token.COMMA)
		tk.add("=", self.Token.ASIGNATION)
		tk.add("[0-9]+", self.Token.NUMBER)
		tk.tokenize(code)
		return tk

	def nextToken(self):
		self.lookahead = self.tokens.pop()

	def parseTokens(self):
		self.nextToken()
		self.expression()

	def expression(self):
		self.setExpr()
		self.variableExpr()

	def setExpr(self):
		if self.lookahead.token == self.Token.OPEN_BRACKET:
			self.nextToken()
			self.number()

	def variableExpr(self):
		if self.lookahead.token == self.Token.VARIABLE:
			self.nextToken()
			if self.lookahead.token == self.Token.ASIGNATION:
				self.nextToken()
				self.expression()

	def number(self):
		if self.lookahead.token == self.Token.NUMBER:
			self.nextToken()
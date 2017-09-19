import sys
import re
from tokenInfo import TokenInfo
from token import Token

class Tokenizer:

	def __init__(self):
		self.tokenInfos = []
		self.tokens = []

	def add(self, regex, token):
		self.tokenInfos.append(TokenInfo("^(" + regex + ")", token))

	def tokenize(self, str):
		s = str.strip()
		self.tokens = []
		while s != '':
			match = False
			for info in self.tokenInfos:
				matches = re.finditer(info.regex, s)
				for matchNum, match in enumerate(matches):
					for groupNum in range(0, len(match.groups())):
						m = match.group(groupNum)
						match = True
						tok = m.strip()
						s = s[len(m):].strip()
						self.tokens.append(Token(info.token, tok))
						break
			if not match:
				raise Exception('Unexpected character in input: \n' + s)

	@property
	def tokens(self):
		return self.tokens
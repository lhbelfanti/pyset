import sys

class TokenInfo:
	
	def __init__(self, regex, token):
		self.regex = regex
		self.token = token

	@property
	def regex(self):
		return self.regex

	@property
	def token(self):
		return self.token
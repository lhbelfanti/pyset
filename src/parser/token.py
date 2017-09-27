import sys

class Token:
	
	MAXIMUN = 0
	MINIMUN = 1
	MEDIAN = 2
	INTERSECTION= 3
	UNION = 4
	EXTRACT = 5
	CREATE = 6
	LONGITUDE = 7
	ADD = 8
	DELETE = 9
	OPEN_BRACKET = 10
	CLOSE_BRACKET = 11
	VARIABLE = 12
	NUMBER = 13
	COMMA = 14
	ASIGNATION = 15

	def __init__(self, token = None, sequence = None):
		self.token = token
		self.sequence = sequence
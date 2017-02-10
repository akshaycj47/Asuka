import re

def calculate(string):
	expression = re.findall("\s([\s0-9\+\-\*\/\(\)\.]+)", string)
	if not expression:
		return "I can't calculate that"
	expression = expression[0]

	# Evaluate the expression
	try:
		calculation = eval(expression)
		return calculation
	except:
		return "I can't calculate that"
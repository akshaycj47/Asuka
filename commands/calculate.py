import re

def calculate(string):
	expression = re.findall("\s([\s0-9\+\-\*\(\)\.]+)", string)
	if not expression:
		print "I can't calculate that"
	expression = expression[0]

	# Evaluate the expression
	try:
		print eval(expression)
	except:
		print "I can't calculate that"
		return
import unirest
import resources.speech

def process_stock_data(response):
	

def stock(string):
	response = unirest.get("http://finance.google.com/finance/info?client=ig&q=INTC")
	#response = unirest.get("http://finance.google.com/finance/info?client=ig&q=NYSE:INFY")
	print type(response.body)
	print response.body


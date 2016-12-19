import re
import unirest

import resources.speech

"""
Function to process stock data obtained from Google Finance API
@param {http response} response - HTTP response obtained from API
@return {dict} Processed data
"""
def process_stock_data(response):
	re_ticker_symbol   = re.search("\"t\" : \"([A-Z]+)\".*", response.body)
	re_stock_exchange  = re.search("\"e\" : \"([A-Z]+)\".*", response.body)
	re_stock_value     = re.search("\"l_fix\" : \"([\d\.]+)\".*", response.body)
	re_stock_change    = re.search("\"c\" : \"([\d\.\+\-]+)\".*", response.body)
	re_stock_change_pc = re.search("\"cp\" : \"([\d\.\+\-]+)\".*", response.body)

	data = {}
	if re_ticker_symbol and re_stock_exchange and re_stock_value and re_stock_change and re_stock_change_pc:
		data['isValid']         = True
		data['ticker_symbol']   = re_ticker_symbol.group(1)
		data['stock_exchange']  = re_stock_exchange.group(1)
		data['stock_value']     = re_stock_value.group(1)
		data['stock_change']    = re_stock_change.group(1)
		data['stock_change_pc'] = re_stock_change_pc.group(1)
	else:
		data['isValid']         = False
	return data

"""
Function which obtains stock prices for a given stock_value using Google Finance API
@param {string} string - Input string obtained from the user. Input string
may contain stock name or both stock name and stock exchange
"""
def stock(string):
	ticker_symbol = ""
	if re.match("^.+\s([A-Z]+:[A-Z]+).*$", string):
		re_stock = re.match("^.+\s([A-Z]+:[A-Z]+).*$", string)
		ticker_symbol = re_stock.group(1)
		response = unirest.get("http://finance.google.com/finance/info?client=ig&q=%s"%(ticker_symbol))
	elif re.match("^.+\s([A-Z]+).*$", string):
		re_stock = re.match("^.+\s([A-Z]+).*$", string)
		ticker_symbol = re_stock.group(1)
		response = unirest.get("http://finance.google.com/finance/info?client=ig&q=%s"%(ticker_symbol))
	else:
		print resources.speech.stock_incorrect_request()
		return
	
	# Process information obtained from Google Finance API
	data = process_stock_data(response)
	if data['isValid']:
		print resources.speech.stock(data)
	else:
		print resources.speech.stock_no_info(ticker_symbol)
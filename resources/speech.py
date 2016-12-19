
def welcome():
	return "\
Welcome to Asuka Console.\n\
I'm Asuka, I can perform basic tasks based on commands in simple English.\n\
Some basic commands include: calculate 56 + 72, find a pizza place near New York.\n\
Type 'quit' to exit."

def cannot_understand():
	return "\
Sorry, I didn't understand your request."

def weather(data):
	return "\
Weather in %s is %s.\n\
Current temperature is %s, with minimum %s and maximum is %s.\n\
Humidity is %s and atmospheric pressure is %s.\n\
Sunrise is at %s and sunset is at %s (%s)"%(data['city'], data['weather_desc'], data['temp'], data['temp_min'], data['temp_max'], data['humidity'], data['pressure'], data['sunrise'], data['sunset'], data['timezone'])

"""
Function that returns response for correct stock request
@param {object} data - Processed response for stock request
@param {string} data.stock_exchange - Name of the stock stock_exchange
@param {string} data.ticker_symbol - Ticker symbol for stock
@param {string} data.stock_value - Stock value
@param {string} data.stock_change - Change in stock value (absolute)
@param {string} data.stock_change_pc - Change in stock value (percentage)
@return {string} Response
"""
def stock(data):
	return "\
Stock %s:%s has value %s (%s, %s%%)"%(data['stock_exchange'], data['ticker_symbol'], data['stock_value'], data['stock_change'], data['stock_change_pc'])

"""
Function that responds to incorrect stock request
@return {string} Response
"""
def stock_incorrect_request():
	return "\
Sorry, I didn't understand your request.\n\
If you want to learn about stock prices, say:\n\
Please find me stock prices for INTC\n\
Can you show me stock prices for NYSE:INFY"

"""
Function that responds to stock request for which there is no information available
@param {string} ticker_symbol - Ticker symbol for stock_exchange
@return {string} Response
"""
def stock_no_info(ticker_symbol):
	return "\
I could not find and stock information for %s"%(ticker_symbol)
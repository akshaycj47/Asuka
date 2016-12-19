
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

def stock(data):
	return "\
Stock %s:%s has value %s (%s, %s%%)"%(data['stock_exchange'], data['ticker_symbol'], data['stock_value'], data['stock_change'], data['stock_change_pc'])

def stock_incorrect_request():
	return "\
Sorry, I didn't understand your request.\n\
If you want to learn about stock prices, say:\n\
Please find me stock prices for INTC\n\
Can you show me stock prices for NYSE:INFY"

def stock_no_info(ticker_symbol):
	return "\
I could not find and stock information for %s"%(ticker_symbol)
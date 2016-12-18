
def welcome():
	return "\
Welcome to Asuka Console.\n\
I'm Asuka, I can perform basic tasks based on commands in simple English.\n\
Some basic commands include: calculate 56 + 72, find a pizza place near New York.\n\
Type 'quit' to exit."

def cannot_understand():
	return "\
Sorry, I didn't undertand your request."

def weather(data):
	return "\
Weather in %s is %s.\n\
Current temperature is %s, with minimum %s and maximum is %s.\n\
Humidity is %s and atmospheric pressure is %s."%(data['city'], data['weather_desc'], data['temp'], data['temp_min'], data['temp_max'], data['humidity'], data['pressure'])
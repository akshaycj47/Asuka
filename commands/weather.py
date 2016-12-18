import unirest
import resources.speech

def weather(string):
	#response = unirest.get("http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=873e47c1d02a6432870f10517eb4a38f")
	response = unirest.get("http://api.openweathermap.org/data/2.5/weather?id=5349705&appid=873e47c1d02a6432870f10517eb4a38f")

	print type(response.body)
	print response.body
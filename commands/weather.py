from datetime import datetime
from dateutil import tz
import unirest
import resources.speech

def kelvin_to_celsius(temp):
	return temp - 273.15

def kelvin_to_fahrenheit(temp):
	temp = kelvin_to_celsius(temp)
	return temp * 1.8 + 32

def get_local_timezone_id(timestamp, lat, lon):
	#response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg")
	response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg"%(lat, lon, timestamp))
	#response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=37.39,-122.08&timestamp=1458000000&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg")
	return response.body['timeZoneId']

def get_local_timezone_name(timestamp, lat, lon):
	response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg"%(lat, lon, timestamp))
	return response.body['timeZoneName']

def unix_to_utc(unix_time):
	utc_time = datetime.utcfromtimestamp(unix_time)
	return utc_time

def unix_to_local_time(unix_time, lat, lon):
	local_timezone = get_local_timezone_id(unix_time, lat, lon)
	from_zone      = tz.gettz('UTC')
	to_zone        = tz.gettz(local_timezone)

	utc = datetime.strptime(str(unix_to_utc(unix_time)), '%Y-%m-%d %H:%M:%S')

	# Tell the datetime object that it's in UTC time zone since 
	# datetime objects are 'naive' by default
	utc = utc.replace(tzinfo=from_zone)

	# Convert time zone
	local_time = utc.astimezone(to_zone)
	#print type(local_time.time())
	#print local_time.time(), local_time.tzinfo
	return local_time.time()

def process_weather_data(response):
	data                 = {}
	data['city']         = response.body['name']
	data['weather_desc'] = response.body['weather'][0]['description']
	data['temp'] 		 = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp']), kelvin_to_fahrenheit(response.body['main']['temp']))
	data['temp_min']     = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp_min']), kelvin_to_fahrenheit(response.body['main']['temp_min']))
	data['temp_max']     = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp_max']), kelvin_to_fahrenheit(response.body['main']['temp_max']))
	data['humidity']     = "%s%%"%(response.body['main']['humidity'])
	data['pressure']     = "%shPa"%(response.body['main']['pressure'])
	data['sunrise']      = unix_to_local_time(response.body['sys']['sunrise'], response.body['coord']['lat'], response.body['coord']['lon'])
	data['sunset']       = unix_to_local_time(response.body['sys']['sunset'], response.body['coord']['lat'], response.body['coord']['lon'])
	data['timezone']     = get_local_timezone_name(response.body['sys']['sunrise'], response.body['coord']['lat'], response.body['coord']['lon'])
	return data

def weather(string):
	response = unirest.get("http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=873e47c1d02a6432870f10517eb4a38f")
	#response = unirest.get("http://api.openweathermap.org/data/2.5/weather?id=5349705&appid=873e47c1d02a6432870f10517eb4a38f")

	#print response.body
	data = process_weather_data(response)
	print resources.speech.weather(data)
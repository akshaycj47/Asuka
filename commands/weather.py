from datetime import datetime
from dateutil import tz
import unirest
import resources.speech

def kelvin_to_celsius(temp):
	return temp - 273.15

def kelvin_to_fahrenheit(temp):
	temp = kelvin_to_celsius(temp)
	return temp * 1.8 + 32

def get_local_timezone(timestamp, lat, lon):
	#response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=38.908133,-77.047119&timestamp=1458000000&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg")
	response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg"%(lat, lon, timestamp))

	#response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=37.39,-122.08&timestamp=1458000000&key=AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg")
	print response.body
	return response.body['timeZoneId']

def unix_to_utc(unix_time):
	utc_time = datetime.utcfromtimestamp(unix_time)
	print utc_time
	print type(utc_time)
	return utc_time

def unix_to_local_time(unix_time, lat, lon):
	local_timezone = get_local_timezone(unix_time, lat, lon)
	local_timezone = tz.gettz(local_timezone)
	#utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')
	#central = utc.astimezone(local_timezone)


	from_zone = tz.gettz('UTC')
	to_zone = tz.gettz('America/New_York')

	# METHOD 2: Auto-detect zones:
	from_zone = tz.tzutc()
	to_zone = tz.tzlocal()

	# utc = datetime.utcnow()
	utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

	# Tell the datetime object that it's in UTC time zone since 
	# datetime objects are 'naive' by default
	utc = utc.replace(tzinfo=from_zone)

	# Convert time zone
	central = utc.astimezone(to_zone)
	print central

	#print unix_to_utc(unix_time).astimezone(local_timezone)
	#return unix_to_utc(unix_time).astimezone(local_timezone)

def process_weather_data(response):
	data                 = {}
	data['city']         = response.body['name']
	data['weather_desc'] = response.body['weather'][0]['description']
	data['temp'] 		 = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp']), kelvin_to_fahrenheit(response.body['main']['temp']))
	data['temp_min']     = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp_min']), kelvin_to_fahrenheit(response.body['main']['temp_min']))
	data['temp_max']     = "%sC (%sF)"%(kelvin_to_celsius(response.body['main']['temp_max']), kelvin_to_fahrenheit(response.body['main']['temp_max']))
	data['humidity']     = "%s%%"%(response.body['main']['humidity'])
	data['pressure']     = "%shPa"%(response.body['main']['pressure'])
	unix_to_utc(response.body['sys']['sunrise'])
	unix_to_local_time(response.body['sys']['sunrise'], response.body['coord']['lat'], response.body['coord']['lon'])
	return data

def weather(string):
	response = unirest.get("http://api.openweathermap.org/data/2.5/weather?zip=94040,us&appid=873e47c1d02a6432870f10517eb4a38f")
	#response = unirest.get("http://api.openweathermap.org/data/2.5/weather?id=5349705&appid=873e47c1d02a6432870f10517eb4a38f")

	#print type(response.body)
	print response.body
	data = process_weather_data(response)
	print resources.speech.weather(data)
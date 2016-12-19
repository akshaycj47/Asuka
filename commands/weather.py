from datetime import datetime
from dateutil import tz
import re
import unirest

import resources.speech

"""
App Id for Open Weather and Google Map API
"""
app_id = {
	'openweathermap': "873e47c1d02a6432870f10517eb4a38f",
	'google_map'    : "AIzaSyAhSNGhwvaBBZdrxcaiUFxGwGjT2a38pzg"
}

"""
Function that converts temperature from kelvin to celsius
@param {int} temp - Given temperature
@return {int} Temperature in celsius
"""
def kelvin_to_celsius(temp):
	return temp - 273.15

"""
Function that converts temperature from kelvin to fahrenheit
@param {int} temp - Given temperature
@return {int} Temperature in fahrenheit
"""
def kelvin_to_fahrenheit(temp):
	temp = kelvin_to_celsius(temp)
	return temp * 1.8 + 32

"""
Function that gets local timezone id using Google Maps API
@param {hex} timestamp - Unix timestamp for current time
@param {int} lat - Latitude
@param {int} lon - Longitude
@return {string} timezone id 
"""
def get_local_timezone_id(timestamp, lat, lon):
	response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=%s"%(lat, lon, timestamp, app_id['google_map']))
	return response.body['timeZoneId']

"""
Function that gets local timezone name using Google Maps API
@param {hex} timestamp - Unix timestamp for current time
@param {int} lat - Latitude
@param {int} lon - Longitude
@return {string} timezone name 
"""
def get_local_timezone_name(timestamp, lat, lon):
	response = unirest.get("https://maps.googleapis.com/maps/api/timezone/json?location=%s,%s&timestamp=%s&key=%s"%(lat, lon, timestamp, app_id['google_map']))
	return response.body['timeZoneName']

"""
Function that converts unix timestamp to UTC time
@param {hex} unix_time - Unix timestamp for current time
@return {time} UTC time
"""
def unix_to_utc(unix_time):
	utc_time = datetime.utcfromtimestamp(unix_time)
	return utc_time

"""
Function that converts unix timestamp to local time
@param {hex} unix_time - Unix timestamp for current time
@param {int} lat - Latitude
@param {int} lon - Longitude
@return {time} local time
"""
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
	return local_time.time()

"""
Function to process weather data obtained from Open Weather API
@param {http response} response - HTTP response obtained from API
@return {dict} Processed data
"""
def process_weather_data(response):
	data = {}
	if 'message' in response.body.keys() and response.body['message'] == "Error: Not found city":
		data['isValid']      = False
	else:
		data['isValid']      = True
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

"""
Function that provides weather information for a given location using Open
Weather API
@param {string} string - Input string from user. It will contain city name
or zip code
"""
def weather(string):
	if re.match("^.*(\d{5}).*$", string):
		re_weather = re.match("^.*(\d{5}).*$", string)
		response = unirest.get("http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=%s"%(re_weather.group(1), app_id['openweathermap']))
	elif re.match("^.*\"([\w\s]+)\".*", string):
		re_weather = re.match("^.*\"([\w\s]+)\".*", string)
		response = unirest.get("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s"%(re_weather.group(1), app_id['openweathermap']))
	else:
		print resources.speech.weather_incorrect_request()
		return

	# Process information obtained form Open Weather API
	data = process_weather_data(response)
	if data['isValid'] == True:
		print resources.speech.weather(data)
	else:
		print resources.speech.weather_no_info()
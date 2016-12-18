import json
import unirest

def joke(string):
	try:
		response = unirest.get("http://tambal.azurewebsites.net/joke/random")
		print response.body['joke']
	except:
		print "Could you be more specific?"

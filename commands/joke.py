import json
import unirest

"""
Function that tells a random joke from a website database
@param {string} string - Input string from user (not used)
"""
def joke(string):
	try:
		response = unirest.get("http://tambal.azurewebsites.net/joke/random")
		print response.body['joke']
	except:
		print "Could you be more specific?"

import re
import webbrowser

def google(string):
	try:
		query = re.findall("\"(.*)\"", string)
		webbrowser.open("https://www.google.com/search?q=%s"%(query[0]))
		return "Searching for %s on a new browser window."%(query[0])
	except:
		return "I could not understand your request."
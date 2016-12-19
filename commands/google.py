import re
import webbrowser

def google(string):
	try:
		query = re.findall("\"(.*)\"", string)
		print "Searching for %s on a new browser window."%(query[0])
		webbrowser.open("https://www.google.com/search?q=%s"%(query[0]))
	except:
		print "I could not understand your request."
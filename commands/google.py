import re
import webbrowser

def google(query):
	query = re.findall("\"(.*)\"", query)
	print "Searching for %s on a new browser window"%(query[0])
	webbrowser.open("https://www.google.com/search?q=%s"%(query[0]))
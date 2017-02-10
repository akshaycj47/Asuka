#!/usr/bin/python

import sys
import commands.calculate
import commands.google
import commands.joke
import commands.stock
import commands.weather
import resources.speech

import unirest

def console():
    print resources.speech.welcome()
    sys.path.append('.')
    while(1):
        string = raw_input("Asuka> ")
        string = string.strip()
        if string == 'quit':
            exit()
        asuka = Asuka()
        asuka.process_commands(string)

class Asuka(object):
    def __init__(self):
        self.commands = {
            'calculate': commands.calculate.calculate,
            'google'   : commands.google.google,
            'joke'     : commands.joke.joke,
            'jokes'    : commands.joke.joke,
            'stock'    : commands.stock.stock,
            'stocks'   : commands.stock.stock,
            'weather'  : commands.weather.weather
        }

    def process_commands(self, string):
        string = string.split()

        for word in string:
            if word in self.commands:
                string = (' ').join(string)
                print self.commands[word](string)

def main():

	if len(sys.argv) != 1:
		print "Wrong"
		sys.exit(1)
	console()

# Standard boiler plate to run the main() function
if __name__ == '__main__':
	main()
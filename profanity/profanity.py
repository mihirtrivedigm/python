import os
import urllib

def read_text():
	quotes = open("D:\coding venture\Python\udacity\doc.txt")
	contents_of_file = quotes.read()
	#print(contents_of_file)
	check_profanity(contents_of_file)
	quotes.close()

	
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.purgomalum.com/service/xml?text=this is some test input"+text_to_check)
	output = connection.read()
	#print(output)
	if output.find('*'):
		print "there is profanity"
	else:
		print "there is no profanity"
	connection.close()


read_text()
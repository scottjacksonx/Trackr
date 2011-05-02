try:
	import json
except:
	import simplejson as json
import urllib
import urllib2
import credentials
from xml.dom.minidom import parseString

def auth(username, password):
	url = "http://www.tumblr.com/api/authenticate"
	values = {"email": username,
	"password": password}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	return response.read()

def getLikes(username, password):
	auth(username, password)
	url = "http://www.tumblr.com/api/likes"
	likes = []
	for i in range(0,4):
		values = {"email": username,
		"password": password,
		"num": 50,
		"start": i*50}
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		for l in parseString(response.read()).getElementsByTagName("post"):
			likes.append(l.getAttribute("url"))
	return likes


# Testing Code #
details = credentials.getCredentials("~/.tumblr") # ~/.tumblr is username/password
print getLikes(details[0], details[1])


# Have ~/.flickr be a file containing your Flickr key.

try:
	import json
except:
	import simplejson as json
import urllib2
import urllib

import credentials


def getUserID(username):
	api_key = credentials.getCredentials("~/.flickr")[0].split()[0]
	url = "http://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key=" + api_key + "&nojsoncallback=1&format=json&username=" + username
	req = urllib2.urlopen(url)
	returnData = json.loads(req.read())
	return returnData["user"]["id"]

def getFavorites(user):
	api_key = credentials.getCredentials("~/.flickr")[0].split()[0]
	url = "http://api.flickr.com/services/rest/?method=flickr.favorites.getPublicList&api_key=" + api_key + "&nojsoncallback=1&format=json&user_id="
	url += getUserID(user)
	req = urllib2.urlopen(url)
	return json.loads(req.read())
	

# Testing Code #
print getFavorites("merlinmann")
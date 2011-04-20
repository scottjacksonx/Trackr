try:
	import json
except:
	import simplejson as json
import urllib2

def getFavorites(user, favs=200):
	"""
	"""
	url = "http://twitter.com/favorites/" + user + ".json?count=" + str(favs)
	try:
		req = urllib2.urlopen(url)
		return json.loads(req.read())
	except urllib2.HTTPError, e:
		if e.code == 401:
			return "nofaves"
		if e.code == 404:
			return "nofaves"
		return "400_status_code_received"

# Testing Code #
print getFavorites("scottjacksonx")
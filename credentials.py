import os

def getCredentials(path):
	expandedPath = os.path.expanduser(path)
	f = open(expandedPath, "r")
	return f.readlines()
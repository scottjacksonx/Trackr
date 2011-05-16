import os

def getCredentials(path):
	expandedPath = os.path.expanduser(path)
	lines = open(expandedPath, "r").read().splitlines()
	return lines

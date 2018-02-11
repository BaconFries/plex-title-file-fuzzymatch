#!/usr/bin/env python
import urllib2
import xmltodict
import dumper
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#curl 127.0.0.1:32400/library/sections/
section = '2'
requestURL = 'http://192.168.1.2:32400/library/sections/' + section + '/all'
data = xmltodict.parse(urllib2.urlopen(requestURL))
for a in data["MediaContainer"].get("Video"):
	title = a.get("@title")
	if not isinstance(a["Media"], dict):
		for b in a["Media"]:
			file = b["Part"]["@file"]
			score = fuzz.token_set_ratio( title, file ) 
			if score < 94:
				print "score: " + str(score) + " title: " + title + "\tfile: " + file
	else:
		file = a["Media"]["Part"]["@file"]
		score = fuzz.token_set_ratio( title, file ) 
		if score < 94:
			print "score: " + str(score) + " title: " + title + "\tfile: " + file

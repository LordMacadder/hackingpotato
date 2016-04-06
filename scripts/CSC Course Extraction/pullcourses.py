#!/usr/bin/python
import sys, os, argparse, urllib2, time, json
from urllib2 import Request
from multiprocessing import Pool

domain = 'https://pod.cybersecuritychallenge.org.uk'
page = '/lib/ajax/getnavbranch.php'
idrange = range(1, 200)
typenum = 10
output = 'output.csv'

fHandle = open(output,'a')
fHandle.write('\"categoryName\"' + ', ' + '\"categorylink\"' + ', ' + '\"courseName\"' + ', ' + '\"courseType\"' + ', ' + '\"courseLink\"' + ', ' + '\"courseHidden\"' + '\n')
fHandle.close()

for idnum in idrange:
	time.sleep(3) # Be nice lets not clog up CSC
	try:
		request = Request(domain + page + '?id=' + str(idnum) + '&type='+str(typenum))
		request = urllib2.urlopen(request)
		response = request.read()
		
	except urllib2.HTTPError:
		#invalid category so 500 error
		print 'N'
		continue

	#process response to json
	try:
		jsonresponse = json.loads(response);
	except ValueError:
		#It wasnt json
		print 'N'
		continue

	# Lets now try to process the json
	# No point doing this if it's an empty category
	if 'children' in jsonresponse:

		categoryname = jsonresponse['name']
		categorylink = jsonresponse['link']

		for child in jsonresponse['children']:
			if child['type'] == 20:
				fHandle = open(output,'a')
				fHandle.write('\"' + categoryname + '\", \"' + categorylink + '\", \"' + child['name'] + '\", \"' + str(child['type']) + '\", \"' + child['link'] + '\", \"' + str(child['hidden']) + '\"\n')
				fHandle.close()
				print 'C'
				
	


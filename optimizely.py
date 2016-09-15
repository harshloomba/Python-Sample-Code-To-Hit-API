import json
import sys
import requests
from urllib import urlopen,urlencode

startTime=raw_input("Enter Start-Time: ")
dataTableApi=raw_input("Enter which Dataset you want to have eg : orders or users: ")

mydict = {'start_time': startTime}
qstr = urlencode(mydict)
#url = "http://speedfeed.xyz/users/list.json/?" + qstr
if mydict['start_time'] =='':
	url = "http://speedfeed.xyz/"+dataTableApi.lower()+"/list.json"
else:
	url = "http://speedfeed.xyz/"+dataTableApi.lower()+"/list.json?"+qstr
print url
try:
	response = requests.get(url)
	p=json.loads(response)
	print p['users']
	#print response.json()
except URLError, e:
    print 'error while extracting Json Data'


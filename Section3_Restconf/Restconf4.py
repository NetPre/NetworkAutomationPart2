#!/usr/bin/env python

import json
import requests
from requests.auth import HTTPBasicAuth


#
auth = HTTPBasicAuth('user', 'password')
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}

#get all configureation 
url = 'https://192.168.0.200/restconf/data/Cisco-IOS-XE-native:native'


response = requests.get(url, headers=headers, auth=auth, verify=False)

print(response)

print(response.text)

response = json.loads(response.text)
print(json.dumps(response, indent=4))



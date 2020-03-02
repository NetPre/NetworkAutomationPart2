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


# you can speficy the depth if you don't give a depth it will give you all info
# check below text
url = 'https://192.168.0.200/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet?depth=3'
response = requests.get(url, headers=headers, auth=auth, verify=False)

response = json.loads(response.text)
print(json.dumps(response, indent=2))



